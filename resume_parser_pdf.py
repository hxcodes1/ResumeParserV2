import pdfplumber
import re
import json
text = ""

with pdfplumber.open(r"C:\project\ResumeParserV2\resume.pdf") as pdf:
    for page in pdf .pages:
        page_text= page.extract_text()
        if page_text:
            text += page_text + "\n"
#Name (first line of resume)
name=text.split("\n")[0]

#Email
email= re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}', text)

#Phone
phone=re.search(r'\d{10}',text)

#Skills
skills=["python","C","C++","Java","SQL","Machine Learning"]

found_skills=[]
for skill in skills:
    if skill.lower() in text.lower():
        found_skills.append(skill)

print("===== Resume Details =====")
print("Name: ", name)
print("Skills: ", ", ".join(found_skills))

if email:
    print("Email: ", email.group())

if phone:
    print("Phone: ", phone.group())

resume_data = {
    "name":name,
    "email":email.group() if email else"",
    "phone":phone.group() if phone else"",
    "skills":found_skills
}

with open("resume_output.json", "w") as f:
    json.dump(resume_data, f, indent=4)
print("Data saved to resume_output.json ")