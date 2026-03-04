import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import fonts
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet

# Read CSV file
data = pd.read_csv("student_data.csv")

# Calculate average marks
data["Average"] = data[["Math", "Science", "English"]].mean(axis=1)

# Create PDF
pdf = SimpleDocTemplate("Student_Report.pdf")
elements = []

styles = getSampleStyleSheet()
title = Paragraph("<b>Student Marks Report</b>", styles["Title"])
elements.append(title)
elements.append(Spacer(1, 0.5 * inch))

# Convert dataframe to list
table_data = [data.columns.tolist()] + data.values.tolist()

table = Table(table_data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

elements.append(table)

pdf.build(elements)

print("PDF Report Generated Successfully!")