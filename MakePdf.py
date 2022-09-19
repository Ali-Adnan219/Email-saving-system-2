from dataclasses import replace
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
import backend
from bidi.algorithm import get_display
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from reportlab.pdfbase import pdfmetrics
doc = SimpleDocTemplate("MydataPdf.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
doc.pagesize = landscape(A4)
elements = []


pdfmetrics.registerFont(TTFont('Arabic', './Bahij_Janna-Bold.ttf'))





arabic_text_style = ParagraphStyle(
    'My Para style',
 
    
    fontName="Arabic",
   
)


def savepdf():

    newdata=backend.View()
    lists=[]
    for x in newdata:
        y = [str(xy) for xy in x]
        lists.append(y)

    #print(lists)

    data =lists
    style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                        ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                        ('VALIGN',(0,0),(0,-1),'TOP'),
                        ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                        ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                        ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                        ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                            ('FONTNAME', (0, 0), (-1, -1), "Arabic")
                        ])

    #Configure style and word wrap
    s = arabic_text_style
    #s = s["BodyText"]
    s.wordWrap = 'CJK'
    data2 = [[Paragraph(get_display(arabic_reshaper.reshape(cell)), s) for cell in row] for row in data]
    t=Table(data2)
    t.setStyle(style)

    #Send the data and build the file
    elements.append(t)
    doc.build(elements)



