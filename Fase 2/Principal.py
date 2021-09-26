from flask import Flask, request, redirect, jsonify
from Analizadores import Analyzer
from ThreeAVLStudent import ThreeAVL
from NodeThreeAVL_Student import NSThreeAVL
from flask_cors import CORS
from NodeHomework import Nodehomework

app = Flask(__name__)
app.config['DEBUG'] = True
data = Analyzer()
avl = ThreeAVL()
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


# CRUD STUDENT
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


# CRUD HOMEWORKS
@app.route('/Recordatorio', methods=['POST'])
def createTask():
    homework = request.json
    enlaces = homework['Fecha'].split('/')
    avl.Together(avl.root, homework, enlaces)
    return 'Tarea Creada'


@app.route('/Recordatorio', methods=['PUT'])
def updateTask():
    updHome = request.json


if __name__ == '__main__':
    app.run(debug=True, port=3000)
