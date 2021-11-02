import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from "rxjs/Observable";
import { LoginStudent } from '../Controller/login-student';
import { CargaEstudiante } from '../Controller/CargaEstudiante';

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

}


