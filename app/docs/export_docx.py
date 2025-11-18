from docx import Document
import uuid

def export_docx(text: str) -> str:
    filename = f"{uuid.uuid4()}.docx"
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    doc.save(filename)
    return filename
