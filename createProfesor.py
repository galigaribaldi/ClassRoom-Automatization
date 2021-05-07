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
#####
def addTeachers(numId, teacher_email):    
    #teacher_email = 'galigaribaldi70@gmail.com'
    teacher = {
        'userId': teacher_email
    }
    try:
        teachers = service.courses().teachers()
        teacher = teachers.create(courseId=numId,
                                body=teacher).execute()
        print('User %s was added as a teacher to the course with ID %s'
            % (teacher.get('profile').get('name').get('fullName'),
                numId))
    except errors.HttpError as error:
        print('User "{%s}" is already a member of this course.'
            % teacher_email)
#addTeachers(275450839438, 'galigaribaldi70@gmail.com')

def addStudent(numId, student_email):
    enrollment_code = '3kvxmue'
    student = {
        'userId': student_email
    }
    try:
        student = service.courses().students().create(
            courseId=numId,
            enrollmentCode=enrollment_code,
            body=student).execute()
        print(
            '''User {%s} was enrolled as a student in
            the course with ID "{%s}"'''
            % (student.get('profile').get('name').get('fullName'),
            numId))
    except HttpError as error:
        print('You are already a member of this course.')    

#addStudent(275450839438,'galigaribaldi@live.com')

def viewStudents(numId, user_Id):
    student = service.courses().students()
    student1 = service.userProfiles().get()
    #student1 = service.userProfiles().get(userId = user_Id).execute()
    print("ID Alumno: ", student1['id'])
    print("Nombre Alumno: ", student1['name']['fullName']) 
    print("Email: ", student1['emailAddress'])
    print("\n")
viewStudents(275450839438,100905005032845497156)
#viewStudents(275450839438,102278109585891765381)
#viewStudents(275450839438,113580004965193682564)
#viewStudents(275450839438,105429210421642055860)