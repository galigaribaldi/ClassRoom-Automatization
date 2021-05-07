#from __future__ import print_function
#from googleapiclient import errors
from googleapiclient.discovery import build
import os.path
import pickle
#####
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
        
service = build('classroom', 'v1', credentials=creds)
def vCoursers(numId):
    # Call the Classroom API
    course = service.courses().get(id=numId).execute()
    print('Course Name: %s found.' % course.get('name'))
    print('Course ID: %s found.' % course.get('id'))
    print('Course Section: %s found.' % course.get('section'))
    print('Course Room: %s found.' % course.get('room'))
    print('Course Description: %s found.' % course.get('description'))
    #course['section'] = 'Period 3'
print("Curso Original")
numId = 275450839438
vCoursers(numId)

def uCourses(numId):
    course = service.courses().get(id=numId).execute()
    course['name'] = "Curso creado desde 0 again"
    course['section'] = 'Period 30'
    course['room'] = '302sa'
    course['description'] = 'Descripcion del curso Again'
    course = service.courses().update(id=numId, body=course).execute()
    print('Course %s updated.' % course.get('name'))

numId = 275450839438
uCourses(numId)
print("Curso Modificado")
vCoursers(numId)    