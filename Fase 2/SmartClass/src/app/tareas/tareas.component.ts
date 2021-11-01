import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-tareas',
  templateUrl: './tareas.component.html',
  styleUrls: ['./tareas.component.css']
})
export class TareasComponent implements OnInit {
  public student: any = "";
  public carnet: any = "";
  constructor() { }

  ngOnInit(): void {
    this.student = localStorage.getItem("estudiante")?.toUpperCase();
    this.carnet = localStorage.getItem("carnet");
  }

}
