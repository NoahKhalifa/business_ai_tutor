"""PDF extraction toolkit — modular components for text, tables, images, math.

Public API:
    extract_pdf(pdf_path, output_dir, components, ...) -> dict

Individual components (use directly if you only need one):
    TextExtractor, ImageExtractor, TableExtractor, MathExtractor
    Each exposes .extract() -> list[Block]
"""
from .pipeline import extract_pdf, render_markdown, DEFAULT_COMPONENTS
from .extractors.base import Block, BaseExtractor
from .extractors.text import TextExtractor
from .extractors.images import ImageExtractor
from .extractors.tables import TableExtractor
from .extractors.math import MathExtractor

__all__ = [
    "extract_pdf",
    "render_markdown",
    "DEFAULT_COMPONENTS",
    "Block",
    "BaseExtractor",
    "TextExtractor",
    "ImageExtractor",
    "TableExtractor",
    "MathExtractor",
]
