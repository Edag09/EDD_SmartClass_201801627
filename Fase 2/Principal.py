import re
from flask import Flask, request, redirect, jsonify, render_template, Response
from flask_cors import CORS
from Analizadores import Analyzer
from ThreeAVLStudent import ThreeAVL
from NodeThreeAVL_Student import NSThreeAVL
import Analizadores

app = Flask(__name__)
app.config['DEBUG'] = True
cors = CORS(app, resourse={r"/*": {"origin*": "*"}})
CORS(app)

data = Analyzer()
avl = ThreeAVL()


@app.route('/')
def home():
    return render_template('index.html')


# Carga Masiva
@app.route('/Cargar', methods=['POST'])
def Cargar():
    Type = request.args.get('Tipo', 'No se ha encontrado algun documento')
    Path = request.args.get('Ruta', 'No se ha encontrado algun documento')
    if Type == 'estudiante':
        data.File_Entry(Path)
        data.insert()
        data.insert_H()
        return 'Estudiante y Tareas yes ' + Path
    elif Type == 'recordatorio':
        data.File_Student_Curse(Path)
        return 'Cursos estudiantes yes ' + Path
    elif Type == 'curso':
        data.Files_Pens_Upload(Path)
        return 'Cursos Pensumn yes ' + Path


# Reportes Generados
@app.route('/Reportes', methods=['GET'])
def Reportes():
    # Ready
    Data = request.json
    Type = int(Data['Tipo'])
    if Type == 0:
        avl.Graph_AVL(Analizadores.avl.root)
        return 'Alumnos listo'
    elif Type == 1:
        return 'Aqui deberia de ir la matriz, deberia :C'
    elif Type == 2:
        # Ready
        avl.Go_Graph_HomeworksAVL(Data['Carnet'], Data['Año'], Data['Mes'], Data['Dia'], Data['Hora'],
                                  Analizadores.avl.root)
        return 'Tareas listas'
    elif Type == 3:
        # Ready
        Analizadores.pensum.show()
        return 'Cursos mostrados'
    elif Type == 4:
        return 'Aqui deberian de ir los cursos, deberian x2 :C'


# *------------------------------------------- //*** CRUD STUDENT ***// -----------------------------------------------*
# Ready
@app.route('/EstudianteAgregar', methods=['POST'])
def EstudianteAgregar():
    student = request.json
    Analizadores.avl.insertThree(NSThreeAVL(student['Carnet'], student['DPI'], student['Nombre'], student['Carrera'], student['Correo'], student['Password'], student['Creditos'], student['Edad']))
    return Response(response='Alumno Creado', content_type='text/plain', mimetype='text/plain')


# Ready
@app.route('/Estudianteput', methods=['PUT'])
def Estudianteput():
    updStudent = request.json
    Analizadores.avl.Update_Student(updStudent, Analizadores.avl.root)
    return 'Estudiante modificado'


# Ready
@app.route('/EstudianteGet', methods=['GET'])
def EstudianteGet():
    Carnet = request.args.get('Carnet', 'No se ha encontrado un estudiante con dicho carnet')
    Password = request.args.get('Password', 'No se ha encontrado un estudiante con dicho carnet')
    student = Analizadores.avl.ShowStudentJSON(Analizadores.avl.root, Carnet, Password)
    return jsonify(student)


@app.route('/ValidarEstudiante', methods=['POST'])
def ValidarEstudiante():
    user = request.json['user']
    passo = request.json['password']
    print(user)
    print(passo)
    student = Analizadores.avl.ShowStudentJSON(Analizadores.avl.root, user, passo)
    return jsonify(student)


# ----------------------------------------- //**** CRUD HOMEWORKS **** // ----------------------------------------------
# Ready
@app.route('/Recordatorio', methods=['POST'])
def Recordatorio():
    homework = request.json
    enlaces = homework['Fecha'].split('/')
    Analizadores.avl.Together(Analizadores.avl.root, homework, enlaces)
    return 'Tarea Creada'


# Ready
@app.route('/Recordatorio', methods=['PUT'])
def Recordatorioput():
    homework = request.json
    date = homework['Fecha'].split('/')
    tar = Analizadores.avl.update_homework_AVL(homework['Carnet'], date[2], date[1], date[0], homework['Hora'],
                                               homework['ID'], Analizadores.avl.root, 'Actualizar', homework)
    return jsonify(tar)


# Ready
@app.route('/Recordatorio', methods=['GET'])
def Recordatorioget():
    homework = request.json
    date = homework['Fecha'].split('/')
    view = Analizadores.avl.get_Homework_AVL(homework['Carnet'], date[2], date[1], date[0], homework['Hora'],
                                             homework['ID'], Analizadores.avl.root, 'Obtener')
    return jsonify(view)


# Ready
@app.route('/Recordatorio', methods=['DELETE'])
def Recordatoriodelete():
    homework = request.json
    date = homework['Fecha'].split('/')
    delete = Analizadores.avl.get_Homework_AVL(homework['Carnet'], date[2], date[1], date[0], homework['Hora'],
                                               homework['ID'], Analizadores.avl.root, 'Eliminar')
    return delete


# --------------------------------------- //**** CREATE CURSE ****// ---------------------------------------------------
# Ready
@app.route('/cursosEstudiante', methods=['POST'])
def cursosEstudiante():
    curseStudent = request.json
    for student in curseStudent['Estudiantes']:
        # se toman los carnets
        for years in student['Años']:
            # se toman los anios
            Analizadores.avl.insert_year(student['Carnet'], years['Año'], avl.root)
            for semester in years['Semestres']:
                Analizadores.avl.findS(student['Carnet'], years['Año'], int(semester['Semestre']), avl.root)
                for curse in semester:
                    Analizadores.avl.insertCurse(student['Carnet'], years['Año'], int(semester['Semestre']),
                                                 curse['Codigo'], curse['Nombre'], curse['Creditos'],
                                                 curse['Prerequisitos'], curse['Obligatorio'], avl.root)
    return 'Cursos estuiantes ingresados'


@app.route('/cursosPensum', methods=['POST'])
def cursosPensum():
    pensum = request.json
    Analizadores.pensum.InsertDataB(pensum['Codigo'], pensum['Nombre'], pensum['Creditos'], pensum['Prerequisitos'],
                                    pensum['Obligatorio'])
    return 'Cursos Creados'


if __name__ == '__main__':
    app.run(debug=True, port=3000)
