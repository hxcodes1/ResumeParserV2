import pdfplumber

text = ""

with pdfplumber.open(r"C:\project\ResumeParserV2\resume.pdf") as pdf:
   

    for page in pdf.pages:
        text+= page.extract_text() + "\n"
print(text)