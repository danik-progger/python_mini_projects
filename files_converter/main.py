import jpg2pdf
from pdf2docx import parse

parse('pdf/all.pdf', 'docx/all.docx')
parse('pdf/bmw.pdf', 'docx/bmw.docx')

with jpg2pdf.create('pdf/bmw.pdf') as pdf:
    pdf.add('img/bmw.jpg')


with jpg2pdf.create('pdf/all.pdf') as pdf:
    pdf.add('img/bmw.jpg')
    pdf.add('img/kobe.jpg')
    pdf.add('img/lake.jpg')

