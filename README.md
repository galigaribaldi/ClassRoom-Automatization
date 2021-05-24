# Classroom Automatization
Este repositorio está pensado para optimizar el resumen de las calificaciones en la plataforma Classroom. De manera análoga, se trabaja con la API que proporciona Google Classroom como motor de información.

Para poder obtener los permisos necesarios, se necesita primero sacar la licencia de desarrollador en Google, el cual se puede obtener en el siguiente enlace: [ENLACE GOOGLE](https://console.cloud.google.com/home/dashboard?project=prueba3-1614630276346&hl=es-419&pli=1). Es importante destacar que los permisos son de tipo **Aplicación de Escritorio**.

Una vez teniendo las credenciales de acceso, se deben descargar y meter en la carpeta *ModulosInternos*, en ella se guardaran las credenciales bajo el nombre *credentials.json*, bajo este nombre se guardarán las credenciales, a través de estas credenciales, se generará un Token de acceso para nuestra aplicación, se muestra código que genera dicho Token:

**Este Código se llama *modelsInit.py***, el cual retorna un servicio que hace posible la automatización de classroom. [CODE](https://github.com/galigaribaldi/ClassRoom-Automatization/blob/main/ModulosInternos/modelsInit.py)

```python
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/classroom.courses',
          'https://www.googleapis.com/auth/classroom.courses.readonly',
          'https://www.googleapis.com/auth/classroom.rosters',
          'https://www.googleapis.com/auth/classroom.rosters.readonly',
          'https://www.googleapis.com/auth/classroom.topics',
          'https://www.googleapis.com/auth/classroom.topics.readonly',
          'https://www.googleapis.com/auth/classroom.coursework.me',
          'https://www.googleapis.com/auth/classroom.coursework.students',
          #'https://www.googleapis.com/auth/classroom.coursework.students.readonly',
          'https://www.googleapis.com/auth/classroom.announcements',
          'https://www.googleapis.com/auth/classroom.announcements.readonly',
          'https://www.googleapis.com/auth/classroom.guardianlinks.students',
          'https://www.googleapis.com/auth/classroom.guardianlinks.students.readonly',
          'https://www.googleapis.com/auth/classroom.guardianlinks.me.readonly',
          'https://www.googleapis.com/auth/classroom.profile.emails',
          'https://www.googleapis.com/auth/classroom.push-notifications',
          'https://www.googleapis.com/auth/classroom.profile.photos'
          ]
def returns_service():
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('ModulosInternos/token.json'):
        creds = Credentials.from_authorized_user_file('ModulosInternos/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'ModulosInternos/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('classroom', 'v1', credentials=creds)
    return service
#c= returns_service()
```

## Notas importantes

### Módulos de Terceros

Para hacer posible la automatización de las calificaciones en classroom, es necesario descargar los siguientes módulos

- Google API: Módulo de terceros, el cual nos permite obtener información directamente de Classroom

  ```shell
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  ```

  

- Pandas: Módulo para el manejo de datos a través de Dataframe's

  ```shell
  pip install pandas
  ```

  

- ReportLab: Módulo que hace posible la creación y generación de reportes en PDF

  ```shell
  pip install reportlab
  ```

  

- MatplotLib: Módulo que hace posible la generación de gráficas y manejos visuales de información

  ```shell
  pip install matplotlib
  ```

### Módulos Propios

En esta sección se explora los módulos creados por el desarrollador, las cuales hacen posible el funcionamiento del mismo. Sólo se mencionará el uso de los mismos, no se explicará el código a detalle.

- models.py: Módulo que hace posible la generación de gráficas. **Importante: Este módulo genera imágenes de salida, las cuales se guardan en la carpeta de *SalidaImg***
- modelsClassroom.py: Módulo que hace posible la descarga y transformación de datos a Dataframes
- modelsInit.py: Módulo que hace posible la creación del servicio
- tables.py: Módulo que hace posible la generación de reportes en PDF
- correo.py: Módulo que hace posible el envío y adjunto de correo.

### Documentación de Terceros

Se adjunta los links para poder consultar la documentación de los módulos de terceros

[Documentación de la API de Google Classroom](https://developers.google.com/classroom/guides/manage-courses)

[Documentación módulo Pandas](https://pandas.pydata.org/)

[Documentación Matplotlib](https://matplotlib.org/)

[Reportlab](https://www.reportlab.com/docs/reportlab-userguide.pdf)

### Demo Propio

Se adjunta un google Colab con el demo de el funcionamiento de Classroom, éste demo se hace gracias a a automatización de un grupo llamado *4to*.

[Google Colab](https://github.com/galigaribaldi/ClassRoom-Automatization/blob/main/Classroom_Demo.ipynb)