# Resume Parser

A simple Python web application that extracts useful information from resumes in PDF format. Users can upload a resume through a web interface, and the application automatically extracts details such as name, email address, phone number, and resume text.

## 🚀 Features

- Upload resumes in PDF format
- Extract text from PDF files
- Extract email addresses automatically
- Extract phone numbers using Regular Expressions (Regex)
- Identify candidate name from resume text
- Simple web interface using Flask
- Display extracted resume information

## 🛠️ Technologies Used

- **Python** – Core programming language
- **Flask** – Web framework
- **pdfplumber** – PDF text extraction
- **Regular Expressions (Regex)** – Email and phone number detection
- **HTML** – Upload interface

## ⚙️ How It Works

1. User uploads a resume PDF.
2. Flask receives the uploaded file.
3. pdfplumber extracts text from the PDF.
4. Regular expressions identify email addresses and phone numbers.
5. The application displays the extracted information.

## 📂 Project Structure

```text
ResumeParserV2/
│
├── app.py
├── resume_parser_pdf.py
├── resume.pdf
├── resume_output.json
└── README.md
```

## ▶️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/hxcodes1/ResumeParserV2.git
```

### 2. Navigate into the project folder

```bash
cd ResumeParserV2
```

### 3. Install dependencies

```bash
pip install flask pdfplumber
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

Visit:

```text
http://127.0.0.1:5000
```

Upload your PDF resume to test the application.

## 🎯 Project Objective

The objective of this project is to automate basic resume information extraction and demonstrate the use of Python, PDF processing, regular expressions, and Flask in building a web-based application.

## 🔮 Future Improvements

- Extract skills automatically
- Extract education details
- Extract work experience
- Improve resume information detection
- Add resume scoring
- Add AI-powered resume analysis and recommendations

## 👨‍💻 Author

**Himanshu Singh**

B.Tech – Computer Science & Engineering

---

*Built as a learning project to explore Python development, web applications, and automation.*
