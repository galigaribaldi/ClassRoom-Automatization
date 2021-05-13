##Propios
import ModulosInternos.modelsClassroom as cursos
import ModulosInternos.correo as enviar
import ModulosInternos.tables as tabla
import ModulosInternos.models as propios
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
                   
def resumen_individual(Clave):
    ###Dataframe Usuarios
    users = cursos.get_users_by_idCourse(listaGrados[Clave])
    ###Dataframe Resumen
    DatosResumen= pd.read_excel(Clave+'_Resumen.xlsx', sheet_name='Resumen', index_col=0)
    ###Dataframe Tareas
    DatosTarea = pd.read_excel(Clave+'_Resumen.xlsx', sheet_name='Tarea', index_col=0)
    ###Dataframe Examenes
    DatosExamen = pd.read_excel(Clave+'_Resumen.xlsx', sheet_name='Examenes', index_col=0)
    ###Dataframe Proyectos
    DatosProyectos = pd.read_excel(Clave+'_Resumen.xlsx', sheet_name='Proyectos', index_col=0)
    ###Dataframe Asistencia
    DatosAsistencia = pd.read_excel(Clave+'_Resumen.xlsx', sheet_name='Asistencia', index_col=0)
    ###########
    for i in users['StudentID']:
        l = []
        #######Ejees para formar la tabla
        ax = plt.subplot(111, frame_on=False) # no visible frame
        ax.xaxis.set_visible(False)  # hide the x axis
        ax.yaxis.set_visible(False)
        #########Dataframes
        Data1 = users[users.StudentID ==i] ###Dataframe Resumen
        Correos = DatosAsistencia[DatosAsistencia.StudentID == i]
        Correos = list(Correos['EmailStudent'])
        ##Join con Resumem
        Final = pd.merge(left=Data1, right=DatosResumen, left_on='StudentID', right_on='StudentID')
        ##Join con Tarea
        FinalTarea = pd.merge(left=Data1, right=DatosTarea, left_on='StudentID', right_on='StudentID')
        FinalTarea = FinalTarea.iloc[:,[5,14,10,11,7,8]]
        #Dataframe
        ###
        cadena = "Minimo en Tareas: "+str(FinalTarea['Calificacion'].min())
        l.append(cadena)
        cadena = "Maximo en Tareas: "+str(FinalTarea['Calificacion'].max())
        l.append(cadena)
        cadena = "Media en Tareas: "+str(round(FinalTarea['Calificacion'].mean(),2))
        l.append(cadena)
        ##Join con Examenes
        FinalExamenes = pd.merge(left=Data1, right=DatosExamen, left_on='StudentID', right_on='StudentID')        
        FinalExamenes = FinalExamenes.iloc[:,[5,14,10,11,7,8]]
        cadena = "Minimo en Examenes: "+str(FinalExamenes['Calificacion'].min())
        l.append(cadena)
        cadena = "Maximo en Examenes: "+str(FinalExamenes['Calificacion'].max())
        l.append(cadena)
        cadena = "Media en Examenes: "+str(FinalExamenes['Calificacion'].mean())        
        l.append(cadena)
        ##Join con Proyectos
        FinalProyecto = pd.merge(left=Data1, right=DatosProyectos, left_on='StudentID', right_on='StudentID')                
        FinalProyecto = FinalProyecto.iloc[:,[5,14,10,11,7,8]]
        cadena = "Minimo en Proyectos: "+str(FinalProyecto['Calificacion'].min())
        l.append(cadena)
        cadena = "Maximo en Proyectos: "+str(FinalProyecto['Calificacion'].max())
        l.append(cadena)
        cadena = "Media en Proyectos: "+str(FinalProyecto['Calificacion'].mean())
        l.append(cadena)
        ##Join con Asistencia
        FinalAsistencia = pd.merge(left=Data1, right=DatosAsistencia, left_on='StudentID', right_on='StudentID')
        FinalAsistencia = FinalAsistencia.iloc[:,[5,14,10,11,7,8]]
        ###Geeneracion de Tabla resumen
        Final.index = Final['Student_Name'].str[0:5]
        table(ax,  Final.iloc[:, 4:9], loc='center')
        plt.savefig('SalidaIMG/TablaIndividual.png')
        ###GRafica de barras 1
        g1 = Final.iloc[:, 4:9].plot.bar(title="Grafica Resumen PETA")
        fig = g1.get_figure()
        fig.savefig('SalidaIMG/GraficaIndividual.png')
        ###Generacion de Excel Resumen
        propios.data_2_excel("ResumenIndividual",FinalTarea,FinalExamenes,FinalProyecto,FinalAsistencia, Final)
        ##Nombre
        try:
            l.append("Nombre del Alumno: "+str(Final['Student_Name'][0]))
            print("Correo: ", Correos[0])
        except:
            l.append("Nombre del Alumno: Null")
        ###
        tabla.reporteIndividual(l)
        input()

#d = resumen_Total_tipo(1,2021,listaGrados['K3'],'K3')

#propios.graficas("6to_Resumen.xlsx", "Resumen")
#tabla.reporteGrupal()
resumen_individual('6to')
