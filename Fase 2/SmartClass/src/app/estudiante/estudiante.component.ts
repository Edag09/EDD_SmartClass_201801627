import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-estudiante',
  templateUrl: './estudiante.component.html',
  styleUrls: ['./estudiante.component.css']
})
export class EstudianteComponent implements OnInit {
  public student: any = "";
  public carnet: any = "";
  constructor() { }

  ngOnInit(): void {
    this.student = localStorage.getItem("estudiante")?.toUpperCase();
    this.carnet = localStorage.getItem("carnet");
  }

}
