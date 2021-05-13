#Importamos los modulos necesarios
import os
from reportlab.pdfgen import canvas

def reporteGrupal():
    doc = canvas.Canvas("SalidaIMG/ReporteCalifGrupal.pdf")
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
    #Guardamos el documento
    doc.save()

def reporteIndividual(listaPalabras):
    doc = canvas.Canvas("SalidaIMG/ReporteCalifIndividual.pdf")
    #Inseratmos la imagen en el documento
    ###Primera Hoja
    ##Tabla
    doc.drawImage("SalidaIMG/TablaIndividual.png", 15, 500,600,500)##(nombre,posicionx,posiciony, ancho, alto)
    ###Grafica
    doc.drawImage("SalidaIMG/GraficaIndividual.png", 0, 100,600,500)##(nombre,posicionx,posiciony, ancho, alto)
    ##Texto Tareas
    doc.drawString(30,700,listaPalabras[0])##(x,y,texto)
    doc.drawString(230,700,listaPalabras[1])##(x,y,texto)
    doc.drawString(430,700,listaPalabras[2])##(x,y,texto)
    ##Texto Examenes
    doc.drawString(30,670,listaPalabras[3])##(x,y,texto)
    doc.drawString(230,670,listaPalabras[4])##(x,y,texto)
    doc.drawString(430,670,listaPalabras[5])##(x,y,texto)
    ##Texto Proyectos
    doc.drawString(30,640,listaPalabras[6])##(x,y,texto)
    doc.drawString(230,640,listaPalabras[7])##(x,y,texto)
    doc.drawString(430,640,listaPalabras[8])##(x,y,texto)    
    ##Texto Nombre
    doc.drawString(25,800,listaPalabras[9])##(x,y,texto)    
    #Guardamos el documento
    doc.save()