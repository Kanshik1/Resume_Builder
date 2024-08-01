import json

def parse_resume(resume_text):
    # Dummy implementation: Replace with actual parsing logic
    return {
        "Name": "Kanshik1",
        "Contact Information": {
            "Phone Number": "123-456-7890",
            "Email": "Kanshik@example.com"
        },
        "Summary": "Experienced software developer.",
        "Experience": [
            {
                "Company Name": "Tech Solutions Inc.",
                "Position": "Senior Developer",
                "Dates of Employment": "Jan 2020 - Present",
                "Responsibilities": ["Led the development of web applications."]
            }
        ],
        "Education": [
            {
                "Degree": "B.Tech in Mechanical Engineering",
                "Institution": "Vishwakarma Institute of Technology Pune",
                "Graduation Year": "2025"
            }
        ],
        "Skills": ["Java", "Python"],
        "Certifications": ["Certification in python by IIT Kharagpur"]
    }

resume_text = """Name: Kanshik1
Contact Information: Phone Number: 123-456-7890, Email: kanshik@example.com
Summary: Experienced software developer.
Experience: Tech Solutions Inc., Senior Developer, Jan 2020 - Present, Led the development of web applications.
Education: B.Tech in Mechanical Engineering, Vishwakarma Institute of Technology Pune, 2025
Skills: Java, Python
Certifications: Certification in python by IIT Kharagpur"""

parsed_resume = parse_resume(resume_text)
print(json.dumps(parsed_resume, indent=4))
