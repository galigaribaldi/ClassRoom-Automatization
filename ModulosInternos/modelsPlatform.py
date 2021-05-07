import psycopg2

##Calificaciones para le bimestre 1
def insertarcalificacion_Bimestre1(campo1_B1,campo2_B1,campo3_B1, campo4_B1, campo5_B1, promedio, estudiante_ID, materia_ID, profesor_ID):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("UPDATE inscripcion_grado SET campo1_B1=%s ,campo2_B1=%s, campo3_B1=%s, campo4_B1=%s, campo5_B1=%s,calificacion_B1=%s WHERE estudiante_ID =%s AND materia_ID=%s AND profesor_ID=%s", (campo1_B1,campo2_B1,campo3_B1, campo4_B1, campo5_B1, promedio, estudiante_ID, materia_ID, profesor_ID))
    print("Lo hace")
    conexion.commit()
    cursor.close()
    conexion.close()

#Calificaciones para el bimestre 2
def insertarcalificacion_Bimestre2(campo1_B2,campo2_B2,campo3_B2, campo4_B2, campo5_B2, promedio, estudiante_ID, materia_ID, profesor_ID):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("UPDATE inscripcion_grado SET campo1_B2=%s ,campo2_B2=%s, campo3_B2=%s, campo4_B2=%s, campo5_B2=%s,calificacion_B2=%s WHERE estudiante_ID =%s AND materia_ID=%s AND profesor_ID=%s", (campo1_B2,campo2_B2,campo3_B2, campo4_B2, campo5_B2, promedio, estudiante_ID, materia_ID, profesor_ID))
    conexion.commit()
    cursor.close()
    conexion.close()

#3Calificaciones para el bimestre 3
def insertarcalificacion_Bimestre3(campo1_B3,campo2_B3,campo3_B3, campo4_B3, campo5_B3, promedio, estudiante_ID, materia_ID, profesor_ID):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("UPDATE inscripcion_grado SET campo1_B3=%s ,campo2_B3=%s, campo3_B3=%s, campo4_B3=%s, campo5_B3=%s,calificacion_B3=%s WHERE estudiante_ID =%s AND materia_ID=%s AND profesor_ID=%s", (campo1_B3,campo2_B3,campo3_B3, campo4_B3, campo5_B3, promedio, estudiante_ID, materia_ID, profesor_ID))
    conexion.commit()
    cursor.close()
    conexion.close()
##Calificaciones para el bimestre 4
def insertarcalificacion_Bimestre4(campo1_B4,campo2_B4,campo3_B4, campo4_B4, campo5_B4, promedio, estudiante_ID, materia_ID, profesor_ID):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("UPDATE inscripcion_grado SET campo1_B4=%s ,campo2_B4=%s, campo3_B4=%s, campo4_B4=%s, campo5_B4=%s,calificacion_B4=%s WHERE estudiante_ID =%s AND materia_ID=%s AND profesor_ID=%s", (campo1_B4,campo2_B4,campo3_B4, campo4_B4, campo5_B4, promedio, estudiante_ID, materia_ID, profesor_ID))
    conexion.commit()
    cursor.close()
    conexion.close()