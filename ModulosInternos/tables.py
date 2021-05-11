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
    #Importamos los modulos necesarios
    from reportlab.pdfgen import canvas
    doc = canvas.Canvas("SalidaIMG/ReporteCalif.pdf")
    #Inseratmos la imagen en el documento
    ###Primera Hoja
    doc.drawImage("SalidaIMG/Tabla.png", 15, 350,600,500)##(nombre,posicionx,posiciony, ancho, alto)
    doc.drawImage("SalidaIMG/grafica3.png", -20, 50,320,380)##(nombre,posicionx,posiciony, ancho, alto)
    doc.drawImage("SalidaIMG/grafica2.png", 290, 70,320,350)##(nombre,posicionx,posiciony, ancho, alto)
    ####
    doc.showPage()
    #### Segunda Hoja
    doc.drawImage("SalidaIMG/grafica4.png", -50, 450,390,290)##(nombre,posicionx,posiciony, ancho, alto)
    doc.drawImage("SalidaIMG/grafica5.png", 260, 450,390,290)##(nombre,posicionx,posiciony, ancho, alto)
    doc.drawImage("SalidaIMG/grafica6.png", -50, 70,390,290)##(nombre,posicionx,posiciony, ancho, alto)
    doc.drawImage("SalidaIMG/grafica7.png", 260, 70,390,290)##(nombre,posicionx,posiciony, ancho, alto)
    #### 
    doc.showPage()
    #### Tercera Hoja
    doc.drawImage("SalidaIMG/grafica1.png", -15, 100,600,600)##(nombre,posicionx,posiciony, ancho, alto)
    #doc.drawImage("../SalidaIMG/grafica3.png", 0, 450,300,300)##(nombre,posicionx,posiciony, ancho, alto)
    #Guardamos el documento
    doc.save()