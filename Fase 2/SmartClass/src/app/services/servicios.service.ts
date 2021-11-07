import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from "rxjs/Observable";
import { LoginStudent } from '../Controller/login-student';
import { CargaEstudiante } from '../Controller/CargaEstudiante';
import { Apuntes } from '../Controller/Apuntes';
import { AlumCurso } from '../Controller/CursoEstudiateReporte';

@Injectable({
  providedIn: 'root'
})
export class ServiciosService {
  constructor( private http: HttpClient) { }

  getUser(user:any, contra:any):Observable<LoginStudent>{
    return this.http.get<LoginStudent>("http://localhost:3000//EstudianteGet?Carnet="+user+"&Password="+contra);
  }
  
  setStudent(carnet:any, dpi:any, nombre:any, carrera:any, correo:any, password:any, creditos:any, edad:any){
    return this.http.post("http://localhost:3000/EstudianteAgregar", {
        Carnet: carnet,
        DPI: dpi,
        Nombre: nombre,
        Carrera: carrera,
        Correo: correo,
        Password: password,
        Creditos: creditos,
        Edad: edad
    });
  }

  cargarDatos(Tipo:any, Ruta:any):Observable<CargaEstudiante>{
    return this.http.post<CargaEstudiante>("http://localhost:3000/Cargas", {Tipo: Tipo, Ruta: Ruta});
  }

  reportStudents(type:any){
    return this.http.post("http://localhost:3000/Reportes", {Tipo: type});
  }

  setApuntes(carnet:any, titulo:any, contenido:any):Observable<Apuntes>{
    return this.http.post<Apuntes>("http://localhost:3000/Apuntes", {Carnet:carnet, Titulo:titulo, Contenido:contenido})
  }

  cursoEstudiante(tipo:any, codigo:any):Observable<AlumCurso>{
    return this.http.post<AlumCurso>('http://localhost:3000/Reportes',{Tipo:tipo, Codigo:codigo})
  }

}


