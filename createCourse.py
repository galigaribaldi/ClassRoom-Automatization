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
# Call the Classroom API
results = service.courses().list(pageSize=10).execute()
courses = results.get('courses', [])
for i in courses:
    print(i["id"], i["name"])

course = {
    'name': 'Curso Nuevo de Prueba',
    'section': 'Period 2',
    'descriptionHeading': 'Este es un curso de pruena',
    'description': """La descripcion mamalona""",
    'room': '301',
    'ownerId': 'me',
    'courseState': 'PROVISIONED'
    }
#course = service.courses().create(body=course).execute()
#print('Course created: %s %s' % (course.get('name'), course.get('id')))