from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from app.docs.convert_docx import read_docx
from app.docs.export_docx import export_docx
from app.docs.export_pdf import export_pdf
import aiofiles

router = APIRouter()

@router.post("/open_docx")
async def open_docx(file: UploadFile):
    temp_path = f"temp_{file.filename}"

    async with aiofiles.open(temp_path, "wb") as out:
        content = await file.read()
        await out.write(content)

    text = read_docx(temp_path)
    return {"text": text}

@router.post("/export_docx")
def export_to_docx(text: str):
    file_path = export_docx(text)
    return FileResponse(file_path, filename="document.docx")

@router.post("/export_pdf")
def export_to_pdf(text: str):
    docx_path = export_docx(text)
    pdf_path = export_pdf(docx_path)
    return FileResponse(pdf_path, filename="document.pdf")
