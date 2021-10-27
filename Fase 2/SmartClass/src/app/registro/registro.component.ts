import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ServiciosService } from '../services/servicios.service';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit {
  public Carnet: any = "";
  public Dpi: any = "";
  public Nombre: any = "";
  public Carrera: any = "";
  public Correo: any = "";
  public Password: any = "";
  public Creditos: any = "";
  public Edad: any = "";

  constructor(private router: Router, private conexion: ServiciosService) { }

  ngOnInit(): void {
  }

  Registrarse(){
      this.conexion.setStudent(this.Carnet, this.Dpi, this.Nombre, this.Carrera, this.Correo, this.Password, this.Creditos, this.Edad).subscribe();
      alert("Inscrito "+this.Nombre+" de carnet "+this.Carnet+" de la carrera de "+this.Carrera)
      this.Carnet = "";
      this.Dpi = "";
      this.Nombre = "";
      this.Carrera = "";
      this.Correo = "";
      this.Password = "";
      this.Creditos = "";
      this.Edad = "";
      this.router.navigate(['']);
    }

}
