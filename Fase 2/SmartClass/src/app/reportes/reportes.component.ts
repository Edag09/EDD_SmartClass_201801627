import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-reportes',
  templateUrl: './reportes.component.html',
  styleUrls: ['./reportes.component.css']
})
export class ReportesComponent implements OnInit {
  public users : any = "";
  constructor() { }

  ngOnInit(): void {
    this.users = localStorage.getItem("userAdmin");
  }

}