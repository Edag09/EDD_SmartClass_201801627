import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-estudiante',
  templateUrl: './estudiante.component.html',
  styleUrls: ['./estudiante.component.css']
})
export class EstudianteComponent implements OnInit {
  public student: any = "";
  public carnet: any = "";
  public condicion : boolean = true;
  constructor() { }

  ngOnInit(): void {
    this.student = localStorage.getItem("estudiante")?.toUpperCase();
    localStorage.setItem("estudiante", this.student);
    this.carnet = localStorage.getItem("carnet");
    localStorage.setItem("carnet", this.carnet)
  }


}
