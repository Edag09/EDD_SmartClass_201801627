import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-cursos',
  templateUrl: './cursos.component.html',
  styleUrls: ['./cursos.component.css']
})
export class CursosComponent implements OnInit {
  public student: any = "";
  public carnet: any = "";
  constructor() { }

  ngOnInit(): void {
    this.student = localStorage.getItem("estudiante")?.toUpperCase();
    this.carnet = localStorage.getItem("carnet");
  }

}
