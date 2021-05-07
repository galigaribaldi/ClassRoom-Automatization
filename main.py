##Propios
import ModulosInternos.modelsClassroom as cursos
import ModulosInternos.correo as enviar
import ModulosInternos.tables as tabla
##Sistema
import pandas as pd


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
    #print(act.head)
    #print(n.head)
    d = pd.merge(left=n, right=act, left_on='TopicId', right_on='TopicId')
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
    allThemes = cursos.return_all_themes(Grado)
    users = cursos.get_users_by_idCourse(Grado)
    Resumen = pd.DataFrame()
    with pd.ExcelWriter(GradoStr+"_Resumen"+'.xlsx') as writer:
        for i in allThemes['name']:
            data = resumen_Actividades_tipo(mes,anio, Grado,i)
            for j in users['StudentID']:
                nuevo = pd.merge(left=users, right=data,left_on='StudentID', right_on='StudentID')
                Promedio = nuevo['Calificacion'].mean()
                print(i, j, "Promedio: ", Promedio)
            data.to_excel(writer,sheet_name=i)
        

d = resumen_Total_tipo(1,2021,listaGrados['4to'],'4to')


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
            

