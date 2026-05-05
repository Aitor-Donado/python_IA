from PyPDF2 import PdfReader

reader1 = PdfReader("pdfs/339741.pdf")
reader2 = PdfReader("pdfs/FDS 2023 - SALFUMAN - AGUA FUERTE.pdf")
reader3 = PdfReader("pdfs/SDB-9277-ES-ES.pdf")
"""
number_of_pages = len(reader.pages)
text = ""
for page in reader.pages:
    text += page.extract_text()
print(text)
"""
print(reader2.pages[0].extract_text())