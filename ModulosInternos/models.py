import pandas as pd
import matplotlib.pyplot as plt
##Generar las gràficas 
def graficas(nameExcel,nombreHoja):
    Datos = pd.read_excel(nameExcel, sheet_name=nombreHoja, index_col=0)
    Datos.index = Datos['Nombre Alumno'].str[0:5]
    ####Tabla
    df = Datos.iloc[:, 2:7]
    ax = plt.subplot(111, frame_on=False) # no visible frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)
    table(ax,  df, loc='center')
    plt.savefig('SalidaIMG/Tabla.png')
    ###GRafica de barras 1
    g1 = Datos.iloc[:, 2:6].plot.bar(subplots=True, title="Grafica Resumen PETA")
    fig = g1[1].get_figure()
    fig.savefig('SalidaIMG/grafica1.png')
    ###GRafica de barras 2
    g2 = Datos.iloc[:, 6:7].plot.bar(title="Grafica Prom Final")
    fig = g2.get_figure()
    fig.savefig('SalidaIMG/grafica2.png')
    ###Grafica Caja Bigotes
    g3 = Datos.plot.box(title="Grafica C-B")
    fig = g3.get_figure()
    fig.savefig('SalidaIMG/grafica3.png')
    ###Grafica Circular 1 = Proyecto
    g4 = Datos.iloc[:, 2:3].plot.pie(subplots=True,title="Grafica Circular Proyecto")
    fig = g4[0].get_figure()
    fig.savefig('SalidaIMG/grafica4.png')
    ###Grafica Circular 2 = Examenes
    g5 = Datos.iloc[:, 3:4].plot.pie(subplots=True,title="Grafica Circular Examenes")
    fig = g5[0].get_figure()
    fig.savefig('SalidaIMG/grafica5.png')
    ###Grafica Circular 2 = Examenes
    g6 = Datos.iloc[:, 4:5].plot.pie(subplots=True,title="Grafica Circular Tarea")
    fig = g6[0].get_figure()
    fig.savefig('SalidaIMG/grafica6.png')
    ###Grafica Circular 2 = Examenes
    g7 = Datos.iloc[:, 5:6].plot.pie(subplots=True,title="Grafica Circular Asistencia")
    fig = g7[0].get_figure()
    fig.savefig('SalidaIMG/grafica7.png')        
    
###Pasar datos a Excel
def data_2_excel(nombre, DataTarea,DataExamenes,DataProyectos,DataAsistencia,DataResumen):
    with pd.ExcelWriter('SalidaIMG/'+nombre+"_salida"+'.xlsx') as writer:
        ##
        if type(DataTarea) == str:
            pass
        else:
            DataTarea.to_excel(writer,sheet_name="Tarea")
        ##
        if type(DataExamenes) == str:
            pass
        else:
            DataExamenes.to_excel(writer,sheet_name="Examenes")
        ##
        if type(DataProyectos) == str:
            pass
        else:
            DataProyectos.to_excel(writer,sheet_name="Proyectos")
        ##
        if type(DataAsistencia) == str:
            pass
        else:
            DataAsistencia.to_excel(writer,sheet_name="Asistencia")
        ##
        if type(DataResumen) == str:
            pass
        else:
            DataResumen.to_excel(writer,sheet_name="Resumen")