import io
import PyPDF2


def extract_resume_text(uploaded_file):
    """
    Extract text from an uploaded PDF file.
    """

    pdf_reader = PyPDF2.PdfReader(
        io.BytesIO(uploaded_file.read())
    )

    text = ""

    for page in pdf_reader.pages:
        text += (page.extract_text() or "") + "\n"

    return text