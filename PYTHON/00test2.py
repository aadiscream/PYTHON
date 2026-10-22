import pdfplumber

# Open the PDF
pdf_path = "D:\\DOWNLOAD\\understanding india.pdf"  # Replace with your PDF's location
questions_answers = []

with pdfplumber.open(pdf_path) as pdf:
    for page_num in range(2, 6):  # Extract text from pages 2 to 5
        page = pdf.pages[page_num - 1]  # Pages are 0-indexed
        text = page.extract_text()
        lines = text.split("\n")  # Split text into lines
        
        for line in lines:
            # Example to format questions (requires parsing logic based on PDF layout)
            if "Answer:" in line:  # Assuming answers are labeled with "Answer:"
                question_part = line.split("Answer:")[0].strip()
                answer_part = line.split("Answer:")[1].strip()
                options = ["A) Option1", "B) Option2", "C) Option3", "D) Option4"]  # Replace with actual options from the PDF
                formatted_qa = {
                    "question": question_part,
                    "options": options,
                    "correct_answer": answer_part[0]  # Assuming the correct answer starts with A/B/C/D
                }
                questions_answers.append(formatted_qa)

# Display the structured questions and answers
for qa in questions_answers:
    print(qa)
