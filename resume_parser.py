const fs = require('fs');

// Function to parse the resume text and convert to JSON
function parseResume(resumeText) {
    // Dummy implementation: Replace with actual parsing logic
    return {
        Name: "Kanshik1",
        ContactInformation: {
            PhoneNumber: "123-456-7890",
            Email: "Kanshik1@example.com"
        },
        Summary: "Lead Game Programer at GameDev+ club in VIT Pune",
        Experience: [
            {
                CompanyName: "GameDev+",
                Position: "Lead Programer",
                DatesOfEmployment: "Mar 2023 - Present",
                Responsibilities: ["Lead Game programmer at Game DeV+ clubof VIT Pune(2023-Present) responsible fordesigning and development of 3D games"]
            }
        ],
        Education: [
            {
                Degree: "B.Tech in Mechanical Engineering",
                Institution: "Vishwakarma Institute of Technology Pune",
                GraduationYear: "2025"
            }
        ],
        Skills: ["Java", "Python"],
        Certifications: ["Certification in python by IIT Kharagpur"]
    };
}

// Example resume text
const resumeText = `Name: Kanshik1
Contact Information: Phone Number: 123-456-7890, Email: kanshik@example.com
Summary:  Lead Game Programer at GameDev+ club in VIT Pune
Experience: GameDev+, Lead Programer, Jan 2023 - Present, Lead Game programmer at Game DeV+ clubof VIT Pune(2023-Present) responsible fordesigning and development of 3D games
Education: B.Tech in Mechanical Engineering, Vishwakarma Institute of Technology Pune, 2025
Skills: Java, Python
Certifications: Certification in python by IIT Kharagpur`;

// Parse the resume and print the JSON output
const parsedResume = parseResume(resumeText);
console.log(JSON.stringify(parsedResume, null, 4));
