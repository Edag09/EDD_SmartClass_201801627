import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-administrador',
  templateUrl: './administrador.component.html',
  styleUrls: ['./administrador.component.css'] 
})
export class AdministradorComponent implements OnInit {
  public users : any = "";
  constructor() { }

  ngOnInit(): void {
    this.users = localStorage.getItem("userAdmin");
  }

}
