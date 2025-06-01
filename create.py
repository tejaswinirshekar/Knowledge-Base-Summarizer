from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

lines = [
    "Regulation Document - Environmental Protection Act",
    "",
    "Section 1: Purpose",
    "This regulation is intended to reduce pollution and protect natural habitats.",
    "",
    "Section 2: Scope",
    "Applies to all industrial facilities operating within the region.",
    "",
    "Section 3: Requirements",
    "- Facilities must monitor emissions quarterly.",
    "- Reporting to environmental agencies is mandatory.",
    "",
    "Section 4: Penalties",
    "Non-compliance may result in fines up to $10,000.",
]

for line in lines:
    pdf.cell(0, 10, line, ln=True)

pdf.output("docs/Sample1_regulations.pdf")
print("PDF file created at docs/Sample1_regulations.pdf")