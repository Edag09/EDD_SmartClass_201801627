import re
from flask import Flask, request, redirect
from Analizadores import Analyzer

app = Flask(__name__)
app.config['DEBUG'] = True
data = Analyzer()


@app.route('/')
def home():
    return redirect('SERVER IS WORKING!!!')


@app.route('/Cargar', methods=['POST'])
def BulkLoad():
    Type = request.args.get('Tipo', 'No se ha encontrado algun documento')
    Path = request.args.get('Ruta', 'No se ha encontrado algun documento')
    if Type == 'estudiante':
        print('Nais')
    elif Type == 'recordatorio':
        print('Nais')
    elif Type == 'curso':
        data.Files_Pens_Upload(Path)
        return "Datos llenados"


if __name__ == '__main__':
    app.run(debug=True, port=3000)
