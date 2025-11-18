from docx2pdf import convert
import uuid

def export_pdf(docx_file: str) -> str:
    """
    Converts the given DOCX file to PDF.
    NOTE: On Windows, docx2pdf requires Microsoft Word installed.
    """
    pdf_file = f"{uuid.uuid4()}.pdf"
    convert(docx_file, pdf_file)
    return pdf_file
