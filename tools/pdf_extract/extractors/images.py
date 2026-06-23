"""Image extractor — saves embedded raster images to <output_dir>/assets/."""
from typing import List

import fitz  # PyMuPDF

from .base import BaseExtractor, Block


class ImageExtractor(BaseExtractor):
    """Extract embedded images. Skips icons smaller than MIN_DIMENSION pixels.

    Output: PNG files at <output_dir>/assets/page_<NNN>_img_<NN>.png.
    Block.content holds the path relative to output_dir (forward slashes).
    """

    MIN_DIMENSION = 50

    def extract(self) -> List[Block]:
        if self.output_dir is None:
            return []
        assets_dir = self.output_dir / "assets"
        assets_dir.mkdir(parents=True, exist_ok=True)

        doc = fitz.open(self.pdf_path)
        out: List[Block] = []
        try:
            for page_idx, page in enumerate(doc, start=1):
                for img_idx, img in enumerate(page.get_images(full=True), start=1):
                    xref = img[0]
                    block = self._save_image(doc, page, page_idx, img_idx, xref, assets_dir)
                    if block is not None:
                        out.append(block)
            return out
        finally:
            doc.close()

    def _save_image(self, doc, page, page_idx, img_idx, xref, assets_dir):
        try:
            pix = fitz.Pixmap(doc, xref)
        except Exception:
            return None

        try:
            if pix.width < self.MIN_DIMENSION or pix.height < self.MIN_DIMENSION:
                return None

            # Normalize colorspace for PNG
            if pix.colorspace is None or pix.colorspace.n > 3 or pix.alpha:
                pix = fitz.Pixmap(fitz.csRGB, pix)

            rects = page.get_image_rects(xref) or []
            bbox = tuple(rects[0]) if rects else (0.0, 0.0, 0.0, 0.0)

            fname = f"page_{page_idx:03d}_img_{img_idx:02d}.png"
            fpath = assets_dir / fname
            pix.save(str(fpath))

            rel = fpath.relative_to(self.output_dir).as_posix()
            return Block(
                type="image",
                page=page_idx,
                bbox=bbox,
                content=rel,
                metadata={"filename": fname, "width": pix.width, "height": pix.height},
            )
        finally:
            pix = None
