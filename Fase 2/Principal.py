from flask import Flask, request, redirect, jsonify
from Analizadores import Analyzer
from ThreeAVLStudent import ThreeAVL
from NodeThreeAVL_Student import NSThreeAVL
from flask_cors import CORS
from ArbolB.Tree_B import TreeB


app = Flask(__name__)
app.config['DEBUG'] = True
data = Analyzer()
avl = ThreeAVL()
pens = TreeB()
CORS(app)


@app.route('/')
def home():
    return redirect('SERVER IS WORKING!!!')


# Carga Masiva
@app.route('/Cargar', methods=['POST'])
def BulkLoad():
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
def report():
    Data = request.json
    Type = int(Data['Tipo'])
    if Type == 0:
        avl.Graph_AVL(avl.root)
        return 'Alumnos listo'
    elif Type == 1:
        return 'Aqui deberia de ir la matriz, deberia :C'
    elif Type == 2:
        avl.Go_Graph_HomeworksAVL(Data['Carnet'], Data['Año'], Data['Mes'], Data['Dia'], Data['Hora'], avl.root)
        return 'Tareas listas'
    elif Type == 3:
        pens.show()
        return 'Cursos mostrados'
    elif Type == 4:
        return 'Aqui deberian de ir los cursos, deberian x2 :c'


# *------------------------------------------- //*** CRUD STUDENT ***// -----------------------------------------------*
@app.route('/Estudiante', methods=['POST'])
def createStudent():
    student = request.json
    avl.insertThree(NSThreeAVL(student['Carnet'], student['DPI'], student['Nombre'], student['Carrera'], student['Correo'], student['Password'], student['Creditos'], student['Edad']))
    return 'Estudiante Creado'


@app.route('/Estudiante', methods=['PUT'])
def updateStudent():
    updStudent = request.json
    avl.Update_Student(updStudent, avl.root)
    return 'Estudiante modificado'


@app.route('/Estudiante', methods=['GET'])
def showStudent():
    Id = request.args.get('Carnet', 'No se ha encontrado un estudiante con dicho carnet')
    student = avl.ShowStudentJSON(avl.root, Id)
    return jsonify(student)


# ----------------------------------------- //**** CRUD HOMEWORKS **** // ----------------------------------------------
@app.route('/Recordatorio', methods=['POST'])
def createTask():
    homework = request.json
    enlaces = homework['Fecha'].split('/')
    avl.Together(avl.root, homework, enlaces)
    return 'Tarea Creada'


@app.route('/Recordatorio', methods=['PUT'])
def UpdateTask():
    homework = request.json
    date = homework['Fecha'].split('/')
    avl.update_homework_AVL(homework['Carnet'], date[2], date[1], date[0], homework['Hora'], homework['ID'], avl.root, 'Actualizar', homework)
    return 'Tarea Actualizada'


@app.route('/Recordatorio', methods=['GET'])
def GetHomework():
    homework = request.json
    date = homework['Fecha'].split('/')
    view = avl.get_Homework_AVL(homework['Carnet'], date[2], date[1], date[0], homework['Hora'], homework['ID'], avl.root, 'Obtener')
    return jsonify(view)


@app.route('/Recordatorio', methods=['DELETE'])
def delete_homework():
    homework = request.json
    date = homework['Fecha'].split('/')
    delete = avl.get_Homework_AVL(homework['Carnet'], date[2], date[1], date[0], homework['Hora'], homework['ID'], avl.root, 'Eliminar')
    return delete


# --------------------------------------- //**** CREATE CURSE ****// ---------------------------------------------------
@app.route('/cursosEstudiante', methods=['POST'])
def cruse_Student():
    curseStudent = request.json
    for student in curseStudent['Estudiantes']:
        # se toman los carnets
        for years in student['Años']:
            # se toman los anios
            avl.insert_year(student['Carnet'], years['Año'], avl.root)
            for semester in years['Semestres']:
                avl.findS(student['Carnet'], years['Año'], int(semester['Semestre']), avl.root)
                for curse in semester:
                    avl.insertCurse(student['Carnet'], years['Año'], int(semester['Semestre']), curse['Codigo'], curse['Nombre'], curse['Creditos'], curse['Prerequisitos'], curse['Obligatorio'], avl.root)
    return 'Cursos estuiantes ingresados'


@app.route('/cursosPensum', methods=['POST'])
def curse_pensum():
    pensum = request.json
    pens.InsertDataB(pensum['Codigo'], pensum['Nombre'], pensum['Creditos'], pensum['Prerequisitos'], pensum['Obligatorio'])
    return 'Cursos Creados'


if __name__ == '__main__':
    app.run(debug=True, port=3000)
