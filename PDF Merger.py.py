from PyPDF2 import PdfFileMerger

pdfs = ['pygame1.pdf', 'pygame2.pdf', 'pygame3.pdf',  'pygame4.pdf', 'pygame5.pdf' ]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("pygame.pdf")
merger.close()