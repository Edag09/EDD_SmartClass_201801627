import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ServiciosService } from '../services/servicios.service';

@Component({
  selector: 'app-carga',
  templateUrl: './carga.component.html',
  styleUrls: ['./carga.component.css']
})
export class CargaComponent implements OnInit {
  public users : any = "";
  public student:any = "";
  public curso:any = "";
  public curEst:any = "";
  public apunte:any = "";
  constructor(private router: Router, private conexion: ServiciosService) { }

  ngOnInit(): void {
    this.users = localStorage.getItem("userAdmin");
  }

  cargarStudent(){
    if(this.student == ""){
      alert("Por favor ingresa un nombre de archivo en el campo requerido!")
    }else{
    this.conexion.cargarDatos('estudiante', this.student).subscribe();
    alert('Estudiantes Cargados')
    this.student = ""
    }
  }

  cargarCursos(){
    if(this.curso == ""){
      alert("Por favor ingresa un nombre de archivo en el campo requerido!")
    }else{
    this.conexion.cargarDatos('curso', this.curso).subscribe();
    alert('Cursos Cargados')
    this.curso = ""
    }
  }

  cargarCursoEstudiante(){
    if(this.curEst == "") {alert('Por favor ingresa un nombre de archivo en el campo requerido!')}
    else{
    this.conexion.cargarDatos('cursosEstudiantes', this.curEst).subscribe();
    alert('Cursos Estudiantes Cargados')
    this.curEst = ""
    }
  }

  cargarApuntes(){
    if(this.apunte == "") {alert('Por favor ingresa un nombre de archivo en el campo requerido!')}
    else{
    this.conexion.cargarDatos('apunte', this.apunte).subscribe();
    alert('Apuntes Cargados')
    this.apunte = ""
    }
  }
  

}
