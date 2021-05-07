#from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient import errors
import os.path
import pickle
###Modulo propio
import ModulosInternos.modelsInit as model
##Pandas
import pandas as pd
##Retorna Dataframe: id Curso, nombre Curso, Descripcion Curso
def get_all_courses():
    service = model.returns_service()
    results = service.courses().list(pageSize=20).execute()
    #courses = []
    cont = 0
    df = pd.DataFrame(columns=['ID_Curso', 'Nombre_Curso', 'Descripcion'], index=range(len(results['courses'])))
    for i in results['courses']:
        l = []
        l.append(i['id'])
        l.append(i['name'])
        l.append(i['descriptionHeading'])
        df.iloc[cont] = l
        cont = cont+1
    return df

###Retorna Dataframe: ID, nombre, email
def get_users_by_idCourse(Courses_id):
    service = model.returns_service()
    results = service.courses().students().list(courseId=Courses_id)
    studentCourses =results.execute()
    df = pd.DataFrame(columns=['StudentID', 'Student_Name', 'EmailStudent'], index=range(len(studentCourses['students'])))
    cont = 0
    for i in studentCourses['students']:
        l = []
        #print(i['userId']);print(i['profile']['name']['fullName']);print(i['profile']['emailAddress'])
        try:
            l.append(i['userId'])
        except KeyError:
            l.append("NULL")
        try:
            l.append(i['profile']['name']['fullName'])
        except KeyError:
            l.append("NULL")
        try:
            l.append(i['profile']['emailAddress'])            
        except KeyError:
            l.append("NULL")
        df.iloc[cont] = l
        cont =cont+1
    return df
#c = get_users_by_idCourse(126383120623)
#print(c)

##Retorna Dataframe: Titulo, Descripcion, FechaCreacion, Maxpuntos,Fechaentrega
def courses_list_activities(course_id, mesFiltro, anioFiltro):
    service = model.returns_service()
    results = service.courses().courseWork().list(courseId=course_id).execute()
    list_activities = []
    df = pd.DataFrame(columns=['CourseWorkID', 'TopicId','Titulo', 'Descripcion','FechaCreacion','PuntosMaximos','FechaEntrega'], index=range(len(results['courseWork'])))
    cont = 0
    for i in results['courseWork']:
        l = []
        #print(i)
        ##print(i.keys())
        #input()
        try:
            if i['dueDate']['month'] >mesFiltro and i['dueDate']['year'] == anioFiltro:
                l.append(i['id'])
                try:
                    l.append(i['topicId'])
                except:
                    l.append("Sin Tema Asignado")                
                try:
                    l.append(i['title'])
                except:
                    l.append("Sin Titulo")
                try:
                    l.append(i['description'])
                except:
                    l.append("Sin decripcion")
                try:
                    l.append(i['creationTime'])
                except:
                    l.append("Sin hora")
                try:
                    l.append(i['maxPoints'])
                except KeyError:
                    l.append("Sin puntaje")
                try:
                    d = str(i['dueDate']['day']) + '/' +str(i['dueDate']['month']) +'/' +str(i['dueDate']['year'])
                    l.append(d)
                except KeyError:
                    l.append("Fecha")
                df.iloc[cont] = l
                cont = cont+1
        except KeyError:
            pass
    df = df.dropna()
    return df
#c = courses_list_activities(126383120623, 1,2021)
#print(c)

def sumbiss_student_courseWork(course_id, course_work_id):
    service = model.returns_service()
    results = service.courses().courseWork().studentSubmissions().list(courseId=course_id, courseWorkId=course_work_id).execute()
    df = pd.DataFrame(columns=['CourseID', 'CourseWorkID', 'StudentID','FechaCreacion','State','ArchivoEntrega','Calificacion'], index=range(len(results['studentSubmissions'])))
    cont = 0
    for i in results['studentSubmissions']:
        l = []
        #print(i)
        #input()
        try:
            l.append(i["courseId"]);l.append(i["courseWorkId"])
        except:
            l.append("NULL")
        try:
            l.append(i["userId"]);l.append(i["creationTime"])
        except:
            l.append("NULL")
        try:
            l.append(i["state"])
        except:
            l.append("NULL")
        try:
            l.append(i["assignmentSubmission"]['attachments'][0]['driveFile']['title'])
        except:
            l.append("NULL")
        try:
            l.append(int(i["draftGrade"])/10)
        except:
            l.append(0)
        df.iloc[cont] = l
        cont = cont+1
    return df
#c = get_course_by_id(275450839438)
#c = get_users_by_idCourse(275450839438)
#c = get_all_courses()
##Retorna un DF con El curso ID, el nombre del tema y la fecha de creacion
def return_all_themes(course_id):
    service = model.returns_service()
    results = service.courses().topics().list(courseId=course_id).execute()    
    df = pd.DataFrame(columns=['CourseId', 'TopicId', 'name','UpdateTime'], index=range(len(results['topic'])))
    cont = 0
    for i in results['topic']:
        l = []
        try:
            l.append(i["courseId"]);l.append(i["topicId"])
        except:
            l.append("NULL")
        try:
            l.append(i["name"])
        except:
            l.append("NULL")
        try:
            l.append(i["updateTime"])
        except:
            l.append("NULL")
        df.iloc[cont] = l
        cont = cont+1
    df = df[df.name != 'Material']
    df = df[df.name != 'Materiales']
    return df

def return_themes_by_name(course_id,names):
    service = model.returns_service()
    results = service.courses().topics().list(courseId=course_id).execute()    
    df = pd.DataFrame(columns=['CourseId', 'TopicId', 'name','UpdateTime'], index=range(len(results['topic'])))
    cont = 0
    for i in results['topic']:
        l = []
        try:
            l.append(i["courseId"]);l.append(i["topicId"])
        except:
            l.append("NULL")
        try:
            l.append(i["name"])
        except:
            l.append("NULL")
        try:
            l.append(i["updateTime"])
        except:
            l.append("NULL")
        df.iloc[cont] = l
        cont = cont+1
    df = df[df.name == names]
    return df
CourseworkId=274276159449
StudentId=113580004965193682564
CourseId = 126383120623
#c = return_all_themes(126382430048)
#print(c)
#c = return_themes_by_name(CourseId, 'Tarea')