import pdfplumber


# Path of the pdf file
pdf_path="compiled-conservation-measures-and-resolutions.pdf"


# Function to load and extract text from pdf
def text_extracter(path):
    content=""
    with pdfplumber.open(path) as pdf:
        total_pages=len(pdf.pages)
        for page_num, page in enumerate(pdf.pages):
            text=page.extract_text()
            content+=text
            print(f"Extracted text from page {page_num + 1}/{total_pages}")
    return content


# Extract text from pdf
pdf_text=text_extracter(pdf_path)


# Save extracted text to a file to verify the full content
with open("extracted_text_1.txt", "w", encoding="utf-8") as f:
    f.write(pdf_text)



