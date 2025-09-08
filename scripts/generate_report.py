"""
Generate a simple PDF report for the repository. Requires `reportlab`.
Run: python scripts/generate_report.py
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def generate_report(output_path="docs/report.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 80, "Hiring Assistant Chatbot - Project Report")

    # Body text
    c.setFont("Helvetica", 11)
    text_lines = [
        "Overview:",
        "This project implements a Hiring Assistant chatbot using Streamlit.",
        "",
        "Components:",
        "- Streamlit UI (app.py)",
        "- Chatbot logic (chatbot.py, prompts.py)",
        "- Utils (validators, question generator, context manager)",
        "- Data handler (simulated storage)",
        "",
        "How to run:",
        "1. pip install -r requirements.txt",
        "2. streamlit run app.py",
        "",
        "This PDF was generated using reportlab.",
    ]

    y = height - 120
    for line in text_lines:
        # Simple text wrapping for long lines
        if len(line) > 90:
            line_chunks = [line[i:i+90] for i in range(0, len(line), 90)]
        else:
            line_chunks = [line]

        for chunk in line_chunks:
            c.drawString(50, y, chunk)
            y -= 16
            if y < 50:  # page break
                c.showPage()
                c.setFont("Helvetica", 11)
                y = height - 50

    # Footer with page number
    c.setFont("Helvetica-Oblique", 9)
    c.drawRightString(width - inch, 20, f"Page {c.getPageNumber()}")

    c.save()
    print(f"✅ Report generated at {output_path}")
    return output_path

if __name__ == "__main__":
    generate_report()
