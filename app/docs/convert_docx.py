from docx import Document

def read_docx(path: str) -> str:
    doc = Document(path)
    lines = [p.text for p in doc.paragraphs]
    return "\n".join(lines)
