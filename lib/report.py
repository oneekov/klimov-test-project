from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
import io

from lib.models import User

def create_pdf_report(surname, name, patronymic, content: str):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=landscape(A4))
    width, height = A4
    
    c.setFont("Inter", 32)

    c.drawImage("web/static/cert.png", 0, 0)

    c.drawCentredString(421, 325, f"{surname} {name}")
    c.drawCentredString(421, 290, patronymic)

    c.drawCentredString(421, 185, content)

    c.save()

    return buffer.getvalue()


