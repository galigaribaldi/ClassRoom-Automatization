def generar_tabla(data, name):
    fileName = str(name)+'.pdf'

    from reportlab.platypus import SimpleDocTemplate
    from reportlab.lib.pagesizes import letter

    pdf = SimpleDocTemplate(
        fileName,
        pagesize=letter
    )

    from reportlab.platypus import Table
    table = Table(data)

    # add style
    from reportlab.platypus import TableStyle
    from reportlab.lib import colors

    style = TableStyle([
        ('BACKGROUND', (0,0), (3,0), colors.green),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),

        ('ALIGN',(0,0),(-1,-1),'CENTER'),

        ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 14),

        ('BOTTOMPADDING', (0,0), (-1,0), 12),

        ('BACKGROUND',(0,1),(-1,-1),colors.beige),
    ])
    table.setStyle(style)

    # 2) Alternate backgroud color
    rowNumb = len(data)
    for i in range(1, rowNumb):
        if i % 2 == 0:
            bc = colors.burlywood
        else:
            bc = colors.beige
        
        ts = TableStyle(
            [('BACKGROUND', (0,i),(-1,i), bc)]
        )
        table.setStyle(ts)

    # 3) Add borders
    ts = TableStyle(
        [
        ('BOX',(0,0),(-1,-1),2,colors.black),

        ('LINEBEFORE',(2,1),(2,-1),2,colors.red),
        ('LINEABOVE',(0,2),(-1,2),2,colors.green),

        ('GRID',(0,1),(-1,-1),2,colors.black),
        ]
    )
    table.setStyle(ts)

    elems = []
    elems.append(table)

    pdf.build(elems)

def pruebas():
    import os
    from reportlab.pdfgen import canvas
    c=canvas.Canvas("test.pdf")
    #drawImage(archivo, x, y, width=None, height=None)
    c.drawImage("../SalidaIMG/grafica.png", 0, A4[1]/2, width=400, height=400)
    c.showPage()
    c.save()
    os.system("test.pdf")
#pruebas()