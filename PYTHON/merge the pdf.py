from PyPDF2 import PdfWriter
import os
merger=PdfWriter()
location="D:\PROGRAMMING\PYTHON\png"
files=[file for file in os.listdir(location) if file.endswith(".pdf")]
for pdf in files:
    merger.append(os.path.join(location, pdf))
merger.write("D:\PROGRAMMING\PYTHON\png\merged.pdf")
merger.close()