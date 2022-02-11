import json
from fpdf import FPDF

# PDF format
pdf = FPDF("P", "mm", "Letter")
pdf.add_page()

with open('personal details.json') as personal_details:
    data = json.load(personal_details)

# input personal data
for details in data:
    pdf.ln(11)
    pdf.set_font('times', 'B', 14)
    pdf.cell(120, 10, details['Name'], ln=1, align="L")
    pdf.image('2x2.jpg', 150, 10, 50,)
    pdf.set_font('times', '', 12)
    pdf.cell(120, 10, details['Address'], ln=1)
    pdf.cell(120, 10, details['Contact Number'], ln=1)
    pdf.cell(120, 10, details['email'], ln=1)
    # career objective and skills
    pdf.ln(12)
    pdf.set_font('times', 'B', 14)
    pdf.cell(120, 10, "Career Objective", ln=1, align="L")
    pdf.set_font('times', '', 12)
    pdf.cell(120, 10, "To utilize my potential in designing new software and technology with latest requirement and advancements ", ln=1)
    pdf.cell(120, 10, "in the field of technology, thereby adding up to the reputation of the organization", ln=1)
    pdf.set_font('times', 'B', 14)
    pdf.cell(120, 10, "Skills", ln=1)
    pdf.cell(120, 10, "Soft Skills", ln=1)
    pdf.set_font('times', '', 12)
    pdf.cell(90, 10, details['Soft Skills'][0], ln=0, align="L")
    pdf.cell(12, 10, details['Soft Skills'][1], ln=1, align="R")
    pdf.cell(90, 10, details['Soft Skills'][2], ln=0, align="L")
    pdf.cell(12, 10, details['Soft Skills'][3], ln=1, align="R")
    pdf.cell(90, 10, details['Soft Skills'][4], ln=0, align="L")
    pdf.cell(12, 10, details['Soft Skills'][5], ln=1, align="R")
    pdf.cell(90, 10, details['Soft Skills'][6], ln=0, align="L")
    pdf.cell(12, 10, details['Soft Skills'][7], ln=1, align="R")
    pdf.set_font('times', 'B', 14)
    pdf.cell(120, 10, "Technical Skills", ln=1)
    pdf.set_font('times', '', 12)
    pdf.cell(90, 10, details['Technical Skills'][0], ln=0, align="L")
    pdf.cell(12, 10, details['Technical Skills'][1], ln=1, align="R")
    pdf.set_font('times', 'B', 14)
    pdf.cell(120, 10, "Educational Background", ln=1)
    # educational background
    for education in details['Educational Background']:
        pdf.set_font('times', '', 12)
        pdf.cell(120, 10, f"{education['school']}", ln=1)
        pdf.cell(120, 10, f"{education['year']}", ln=1)
    pdf.set_font('times', 'B', 14)
    pdf.cell(120, 10, "Awards and Recognition", ln=1)
    # Awards and recognition
    pdf.set_font('times', '', 12)
    pdf.cell(120, 10, details['Awards and Recognition'][0], ln=1)
    pdf.cell(120, 10, details['Awards and Recognition'][1], ln=1)
    pdf.cell(120, 10, details['Awards and Recognition'][2], ln=1)
    pdf.cell(120, 10, details['Awards and Recognition'][3], ln=1)
    # personal information
    pdf.set_font('times', 'B', 14)
    pdf.cell(120, 10, "Personal Information", ln=1)
    pdf.set_font('times', '', 12)
    pdf.cell(90, 10, "Age: " + details['Age'], ln=0, align="L")
    pdf.cell(12, 10, "Height: " + details['Height'], ln=1, align="R")
    pdf.cell(90, 10, "Date of Birth: " + details['Date of Birth'], ln=0, align="L")
    pdf.cell(12, 10, "Weight: " + details['Weight'], ln=1, align="R")
    pdf.cell(90, 10, "Gender: " + details['Sex'], ln=0, align="L")
    pdf.cell(12, 10, "Nationality: " + details['Nationality'], ln=1, align="R")
    pdf.cell(90, 10, "Civil Status: " + details['Civil Status'], ln=0, align="L")
    pdf.cell(12, 10, "Religion: " + details['Religion'], ln=1, align="R")


pdf.output('RUFFY_EROSCLOEDE.pdf')