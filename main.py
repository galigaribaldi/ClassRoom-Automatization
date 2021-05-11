##Propios
import ModulosInternos.modelsClassroom as cursos
import ModulosInternos.correo as enviar
import ModulosInternos.tables as tabla
##
import matplotlib.pyplot as plt
##Sistema
import pandas as pd
import numpy as np
from pandas.plotting import table

def convert_allCourses():
    c = cursos.get_all_courses()
    print(c)
    c.to_excel("Cursos.xlsx")

listaGrados = {"K2":126380062908,"K3":126382145220,"1ro":126382145238,"2do":126382430010,
               "3ro":126382430032,
                "4to":126382430048,
                "5to":126382430066,
                "6to":126383120623,
                "CM":283913077412,
                }
data = [
        ['Nombre Del Alumno', 'Asistencia', 'Tareas', 'Proyecto' ]
    ]

def resumen_Actividades(mes,anio, Grado):
    d = cursos.courses_list_activities(Grado, mes,anio)
    users = cursos.get_users_by_idCourse(Grado)
    Final = pd.DataFrame()
    for i in d['CourseWorkID']:
        actividades = cursos.sumbiss_student_courseWork(Grado,i)
        Final = pd.concat([actividades, Final])
        #Final = pd.merge(left=d, right=actividades, left_on='CourseWorkID', right_on='CourseWorkID')
    Final2 = pd.merge(left=Final, right=d, left_on='CourseWorkID', right_on='CourseWorkID')
    Final3 = pd.merge(left=Final2, right=users, left_on='StudentID', right_on='StudentID')
    return Final3

def resumen_Actividades_tipo(mes,anio, Grado,tipo_actividad):
    n = cursos.courses_list_activities(Grado, mes,anio)
    act = cursos.return_themes_by_name(Grado, tipo_actividad)
    d = pd.merge(left=n, right=act, left_on='TopicId', right_on='TopicId')
    #input()
    users = cursos.get_users_by_idCourse(Grado)
    Final = pd.DataFrame()
    for i in d['CourseWorkID']:
        actividades = cursos.sumbiss_student_courseWork(Grado,i)
        Final = pd.concat([actividades, Final])
        #Final = pd.merge(left=d, right=actividades, left_on='CourseWorkID', right_on='CourseWorkID')
    Final2 = pd.merge(left=Final, right=d, left_on='CourseWorkID', right_on='CourseWorkID')
    Final3 = pd.merge(left=Final2, right=users, left_on='StudentID', right_on='StudentID')
    return Final3

def resumen_Total_tipo(mes,anio, Grado, GradoStr):
    ###Primera parte
    allThemes = cursos.return_all_themes(Grado)
    with pd.ExcelWriter(GradoStr+"_Resumen"+'.xlsx') as writer:
        for i in allThemes['name']:
            Resumen = pd.DataFrame()
            print(i)
            data = resumen_Actividades_tipo(mes,anio, Grado,i)
            data.to_excel(writer,sheet_name=i)
    #####Segunda parte
    #input("Segunda parte")
    ###Leer el Dataframe
    datosProyectos = pd.read_excel(GradoStr+"_Resumen"+".xlsx",sheet_name="Proyectos")
    datosExamenes = pd.read_excel(GradoStr+"_Resumen"+".xlsx",sheet_name="Examenes")
    datosTarea = pd.read_excel(GradoStr+"_Resumen"+".xlsx",sheet_name="Tarea")
    datosAsistencia = pd.read_excel(GradoStr+"_Resumen"+".xlsx",sheet_name="Asistencia")
    ### Usuarios
    users = cursos.get_users_by_idCourse(Grado)
    ###Generar Resumen
    DataframeFinal = pd.DataFrame(columns=['StudentID', 'Nombre Alumno', 'Proyecto','Examenes','Tareas','Asistencia', 'Promedio Final'], index=range(len(users['StudentID'])))
    cont=0
    for i in range(len(users['StudentID'])):
        l=[]
        ########Leyendo y Filtrando Dataframes
        proyectos = datosProyectos[datosProyectos.StudentID == users['StudentID'][i]]
        examenes = datosExamenes[datosExamenes.StudentID == users['StudentID'][i]]
        Tarea = datosTarea[datosTarea.StudentID == users['StudentID'][i]]
        asistencia = datosAsistencia[datosAsistencia.StudentID == users['StudentID'][i]]
        ##Agregando valores Generales
        l.append(users['StudentID'][i]); l.append(users['Student_Name'][i])
        ###Proyecto (2)
        l.append(proyectos['Calificacion'].mean())
        ###Examenes (3)
        l.append(examenes['Calificacion'].mean())
        ###Tareas (4)
        l.append(round(Tarea['Calificacion'].mean(),2))
        ###Asistencia (5)
        l.append(asistencia['Calificacion'].mean())
        ###PromedioFinal
        PF = (l[2]*.5)+(l[3]*.2)+(l[4]*.15)+(l[5]*.15)
        l.append(round(PF,2))
        ###
        DataframeFinal.iloc[cont] = l
        cont = cont+1
    with pd.ExcelWriter(GradoStr+"_Resumen"+'.xlsx') as writer:
        ###
        datosProyectos.drop(datosProyectos.filter(regex="Unnamed"),axis=1, inplace=True)
        datosProyectos.to_excel(writer,sheet_name="Proyectos")
        ###
        datosExamenes.drop(datosExamenes.filter(regex="Unnamed"),axis=1, inplace=True)
        datosExamenes.to_excel(writer,sheet_name="Examenes")
        ###
        datosTarea.drop(datosTarea.filter(regex="Unnamed"),axis=1, inplace=True)
        datosTarea.to_excel(writer,sheet_name="Tarea")
        ###
        datosAsistencia.drop(datosAsistencia.filter(regex="Unnamed"),axis=1, inplace=True)
        datosAsistencia.to_excel(writer,sheet_name="Asistencia")
        ###
        DataframeFinal.to_excel(writer,sheet_name="Resumen")
                   
#d = resumen_Total_tipo(1,2021,listaGrados['K3'],'K3')

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
    

graficas("5to_Resumen.xlsx", "Resumen")
tabla.pruebas()
def generar_resumen(Clave):
    users = cursos.get_users_by_idCourse(listaGrados[Clave])
    c = resumen_Actividades(1,2021, listaGrados[Clave])
    for i in range(len(users['StudentID'])):
        try:
            ##Enviar Explicacion
            #users[EmailStudent]
            enviar.enviar_correo_PDF(users['EmailStudent'][i],"Calificacion B3 (Archivo Explicacion)","Explicacion.xlsx")
            ###Generacion de PDF
            resumen = []
            resumen2=[['Nombre Del Alumno', 'Asistencia', 'Tareas', 'Proyecto','Promedio Final' ]]
            ###Generacion de Excel
            print(users['StudentID'][i])
            nuevo = c[c['StudentID'] == users['StudentID'][i]]
            nuevo = nuevo.drop(['CourseID','CourseWorkID','StudentID','FechaCreacion_x'], axis=1)
            Promedio = nuevo['Calificacion'].mean()
            print("Promedio: "+str(Promedio))
            ###Generacion de Excel
            nuevo.to_excel("Resumen.xlsx")
            ##Enviar Excel
            enviar.enviar_correo_PDF(users['EmailStudent'][i],"Calificacion B3 (Archivo de Resumen Excel)","Resumen.xlsx")
            ###Generacion de PDF
            asistencia = int(input("Inserte Asistencia para "+ users['Student_Name'][i]+": "))
            proyectos = int(input("Inserte proyectos para "+ users['Student_Name'][i]+": "))
            resumen.append(users['Student_Name'][i]);resumen.append(str(asistencia))
            resumen.append(str(Promedio));resumen.append(str(proyectos))
            resumen.append(str((Promedio+proyectos+asistencia)/3))
            resumen2.append(resumen)
            tabla.generar_tabla(resumen2, "Tabla1")
            enviar.enviar_correo_PDF(users['EmailStudent'][i],"Calificacion (Resumen PDF)","Tabla1.pdf")
        except ValueError:
            ##Enviar Explicacion
            #users[EmailStudent]
            enviar.enviar_correo_PDF(users['EmailStudent'][i],"Calificacion B3 (Archivo Explicacion)","Explicacion.xlsx")
            ###Generacion de PDF
            resumen = []
            resumen2=[['Nombre Del Alumno', 'Asistencia', 'Tareas', 'Proyecto','Promedio Final' ]]
            ###Generacion de Excel
            print(users['StudentID'][i])
            nuevo = c[c['StudentID'] == users['StudentID'][i]]
            nuevo = nuevo.drop(['CourseID','CourseWorkID','StudentID','FechaCreacion_x'], axis=1)
            Promedio = nuevo['Calificacion'].mean()
            print("Promedio: "+str(Promedio))
            ###Generacion de Excel
            nuevo.to_excel("Resumen.xlsx")
            ##Enviar Excel
            enviar.enviar_correo_PDF(users['EmailStudent'][i],"Calificacion B3 (Archivo de Resumen Excel)","Resumen.xlsx")
            ###Generacion de PDF
            asistencia = int(input("Inserte Asistencia para "+ users['Student_Name'][i]+": "))
            proyectos = int(input("Inserte proyectos para "+ users['Student_Name'][i]+": "))
            resumen.append(users['Student_Name'][i]);resumen.append(str(asistencia))
            resumen.append(str(Promedio));resumen.append(str(proyectos))
            resumen.append(str((Promedio+proyectos+asistencia)/3))
            resumen2.append(resumen)
            tabla.generar_tabla(resumen2, "Tabla1")
            enviar.enviar_correo_PDF(users['EmailStudent'][i],"Calificacion (Resumen PDF)","Tabla1.pdf")            
            

