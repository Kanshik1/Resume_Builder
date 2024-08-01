import json

def parse_resume(resume_text):
    # Dummy implementation: Replace with actual parsing logic
    return {
        "Name": "Kanshik1",
        "Contact Information": {
            "Phone Number": "123-456-7890",
            "Email": "Kanshik@example.com"
        },
        "Summary": "Lead Game Programer at GameDev+ club in VIT Pune",
        "Experience": [
            {
                "Company Name": "GameDev+",
                "Position": "Lead Programer",
                "Dates of Employment": "Mar 2023 - Present",
                "Responsibilities": ["Lead Game programmer at Game DeV+ clubof VIT Pune(2023-Present) responsible fordesigning and development of 3D games"]
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
Summary: Lead Game Programer at GameDev+ club in VIT Pune
Experience: GameDev+, Lead Programer, Jan 2023 - Present, Lead Game programmer at Game DeV+ clubof VIT Pune(2023-Present) responsible fordesigning and development of 3D games.
Education: B.Tech in Mechanical Engineering, Vishwakarma Institute of Technology Pune, 2025
Skills: Java, Python
Certifications: Certification in python by IIT Kharagpur"""

parsed_resume = parse_resume(resume_text)
print(json.dumps(parsed_resume, indent=4))
