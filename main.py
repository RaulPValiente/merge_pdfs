# You must include the pdfs you want to merge in the project directory and include their names in the "pdfs" array

from PyPDF2 import PdfMerger

pdfs = ['pdf1.pdf', 'pdf2.pdf', 'pdf3.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)
    
merger.write('final_pdf.pdf')
merger.close()