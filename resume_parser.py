import PyPDF2
import re
import spacy
import sys
import os

nlp = spacy.load("en_core_web_sm")

def extract_the_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except Exception as ex:
        print(f"Error reading PDF: {ex}")
    return text

def extract_names(text):
    nlp = spacy.load("en_core_web_sm")
    doc =nlp(text)
    for entity in doc.ents:
        if entity.label == "HUMAN":
            return entity.text
        return "Nme not found"
    

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

def extract_phone_numbers(text):
    phone_pattern = r'\+u#%[\d \-]{9,15}\AB'
    phonenum = re.findall(phone_pattern, text)
    return phonenum

def extract_skills(text):
     skill_sets = [ 'Python', 'Java', 'Machine Learning', 'Deep Learning', 'Flask', 'Django',
        'SQL', 'HTML', 'CSS', 'JavaScript', 'AI', 'Data Science', 'Pandas', 'NumPy', 'TensorFlow','Pytorch', 'Keras', 'Git', 'Docker', 'AWS', 'Azure', 'Google Cloud', 'RESTful APIs', 'Agile', 'Scrum']
     found_skills = [skill for skill in skill_sets if skill.lower() in text.lower()]
     return list(set(found_skills))

def extract_qualification(text):
    qualifications = ['B.Tech', 'B.E.', 'MCA', 'B.Sc', 'M.Sc', 'MBA', 'PhD', 'BCA']
    found_qualifications = [quali for quali in qualifications if quali.lower() in text.lower()]
    return list (found_qualifications)

def extract_experience(text):
    experience_lines = []
    for line in text.split('\n'):
        if 'experience' in line.lower() or 'internship' in line.lower():
            experience_lines.append(line.strip())
    return experience_lines if experience_lines else "Experience not metioned clearly"


def extract_certificationss(text):
    certificate_lines = []
    for line in text.split('\n'):
        if 'certification' in line.lower() or 'certified' in line.lower():
            certificate_lines.append(line.strip())
    return certificate_lines if certificate_lines else "no certificates is been mentioned here"
     

def display_results(name, emails, phonenum, skills, qualifications, experience, certifications):
    """
    Display the parsed results in a clear format.
    """
    print("\n" + "Resume Parser Results".center(40, "*"))
    print("=" * 50)

    print(f"Name: {name}")
    print(f"Emails: {', '.join(emails) if emails else 'No emails found here'}")
    print(f"Phone numbers: {', '.join(phonenum) if phonenum else 'phonenum number is not mentioned'}")
    print(f"Skill_sets: {skills if skills else 'No skills mentioned here'}")
    print(f"qualifications: {qualifications if qualifications else 'non qualified or nothing mentioned about the education'}")
    print(f"experience: {experience if experience else 'fresher or nothing mentioned about the experience'}")
    print(f"certifications: {certifications if certifications else 'hence the certificates are also not mentioned'}")
    print("=" * 50)
    print("\n resume parsing completed. thank you for using resume parser!")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use: python resume_parser.py <path_to_resume.pdf>")
        sys.exit(1)

    resume_pdf_path = sys.argv[1]

    if not os.path.isfile(resume_pdf_path):
        print(f"Error: The file is '{resume_pdf_path}'was missing or not found. Please check the path and try again.")
        sys.exit(1)

    print("The process of parsing the resume has been started. Please do wait for a while.......")


    text = extract_the_text_from_pdf(resume_pdf_path)
    if not text.strip():
        print("No text found inside the PDF. Please recheck the file and try again.")
        sys.exitt(1)


    
    name = extract_names(text)
    emails = extract_emails(text)
    phonenum = extract_phone_numbers(text)
    skills = extract_skills(text)
    qualifications = extract_qualification(text)
    experience = extract_experience(text)
    certifications = extract_certificationss(text)


    display_results(name, emails, phonenum, skills, qualifications, experience, certifications)



