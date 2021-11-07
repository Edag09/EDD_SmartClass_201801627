import { Component, OnInit } from '@angular/core';
import { isEmpty } from 'rxjs-compat/operator/isEmpty';
import { ServiciosService } from '../services/servicios.service';

@Component({
  selector: 'app-cursos',
  templateUrl: './cursos.component.html',
  styleUrls: ['./cursos.component.css']
})
export class CursosComponent implements OnInit {
  public codigo:any = "";
  public mostrar:boolean = false
  public student: any = "";
  public carnet: any = "";
  constructor(private conexion:ServiciosService) { }

  ngOnInit(): void {
    this.student = localStorage.getItem("estudiante")?.toUpperCase();
    this.carnet = localStorage.getItem("carnet");
  }

  buscarCodigo(){
    if(this.codigo == ""){
      alert("No hay codigo para analizar")
    }else{
      this.conexion.cursoEstudiante(5, this.codigo).subscribe();
      alert("Codigo a analizar " + this.codigo)
      this.mostrar = true
    }
  }

}
