import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ServiciosService } from '../services/servicios.service';

@Component({
  selector: 'app-reportes',
  templateUrl: './reportes.component.html',
  styleUrls: ['./reportes.component.css']
})
export class ReportesComponent implements OnInit {
  public users : any = "";
  public alumno:boolean = false;
  public curso:boolean = false;
  public cursoAlumno:boolean = false;
  public apuntes:boolean = false;
  constructor(private router:Router, private conexion:ServiciosService) { }

  ngOnInit(): void {
    this.users = localStorage.getItem("userAdmin");
  }

  reportarAlumnos(){
    this.conexion.reportStudents(1).subscribe();
    alert("Estudiantes Reportados")
    this.alumno = true
    this.apuntes = false
    this.curso = false
    this.cursoAlumno = false
  }

  reportarApuntes(){
    this.conexion.reportStudents(2).subscribe();
    alert('Apuntes Cargados')
    this.apuntes = true
    this.alumno = false
    this.curso = false
    this.cursoAlumno = false
  }

  Malla(){
    this.conexion.reportStudents(4).subscribe();
    alert('Así es nuestra vida universitaria :D!')
    this.curso = true
  }

}
