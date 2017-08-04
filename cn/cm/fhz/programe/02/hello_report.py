from reportlab.graphics.shapes import Drawing,String
from reportlab.graphics import renderPDF

d = Drawing(100,100)

s = String(50,50,'Hello,world!',TextAnchor = 'moddle')

d.add(s)

renderPDF.drawToFile(d,r'D:\test\hello.pdf','A simple PDF file')