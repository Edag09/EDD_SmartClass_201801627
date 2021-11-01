import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-apuntes',
  templateUrl: './apuntes.component.html',
  styleUrls: ['./apuntes.component.css']
})
export class ApuntesComponent implements OnInit {
  public student: any = "";
  public carnet: any = "";
  public titulo:any = "";
  public contenido:any = "";
  public apuntes : boolean = true;
  public verapuntes : boolean = false;
  public aps:any = ["Apunte 1 ", "Apunte 2", "Apunte 3", "Apunte 4"];
  public cont:any = ["Aqui el apunte 1", "Aqui el apunte 2", "Aqui el apunte 3", "Aqui el apunte 4",];
  constructor() { }

  ngOnInit(): void {
    this.student = localStorage.getItem("estudiante")?.toUpperCase();
    this.carnet = localStorage.getItem("carnet");
  }

  Anotar(){
    if (this.titulo == "" || this.contenido == "") {
      alert("Por favor llena los campos restantes")
    }else{
      console.log(this.titulo)
      console.log(this.contenido)
      this.titulo ="";
      this.contenido="";
    }
  }

  desaparece(){
    this.apuntes = false
    this.verapuntes = true
  }

  aparece(){
    this.apuntes = true
    this.verapuntes = false
  }



}
