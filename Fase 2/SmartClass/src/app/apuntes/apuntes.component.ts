import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-apuntes',
  templateUrl: './apuntes.component.html',
  styleUrls: ['./apuntes.component.css']
})
export class ApuntesComponent implements OnInit {
  public student: any = "";
  public carnet: any = "";
  constructor() { }

  ngOnInit(): void {
    this.student = localStorage.getItem("estudiante")?.toUpperCase();
    this.carnet = localStorage.getItem("carnet");
  }

}
