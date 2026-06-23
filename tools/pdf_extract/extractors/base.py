from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple


BBox = Tuple[float, float, float, float]


@dataclass
class Block:
    """A positioned chunk of content extracted from one PDF page.

    type: "text" | "heading" | "table" | "image" | "math"
    bbox: (x0, y0, x1, y1) in PDF point units; origin at top-left.
    content: for text/heading/table this is the markdown text;
             for image/math this is the relative path to the saved asset.
    """

    type: str
    page: int
    bbox: BBox
    content: str
    metadata: dict = field(default_factory=dict)


class BaseExtractor(ABC):
    """Subclass and implement extract(). Each extractor owns one concern."""

    def __init__(self, pdf_path: Path, output_dir: Optional[Path] = None):
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir) if output_dir else None

    @abstractmethod
    def extract(self) -> List[Block]:
        ...
