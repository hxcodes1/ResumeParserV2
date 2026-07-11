from flask import Flask, request
import pdfplumber
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        file = request.files["resume"]

        with pdfplumber.open(file) as pdf:
            text = ""

            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        lines = text.split("\n")
        name = lines[0] if lines else "Not Found"

        email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
        phone = re.findall(r'\+?\d[\d\s-]{8,}\d', text)

        result = f"""
        <h2>Resume Details</h2>

        <p><b>Name:</b> {name}</p>
        <p><b>Email:</b> {email[0] if email else "Not Found"}</p>
        <p><b>Phone:</b> {phone[0] if phone else "Not Found"}</p>

        <hr>

        <h3>Resume Text</h3>
        <pre>{text}</pre>

        <a href="/">Upload Another Resume</a>
        """

        return result

    return """
    <h1>Resume Parser</h1>

    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="resume" accept=".pdf">
        <button type="submit">Upload</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)