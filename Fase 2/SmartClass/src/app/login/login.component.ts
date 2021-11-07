import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { ServiciosService } from '../services/servicios.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public user : any = "";
  public password: any = "";
  public existe: boolean = false;
  public data: any = "";
  constructor(private router: Router, private conexion: ServiciosService, private activador: ActivatedRoute) { }

  ngOnInit(): void {}

  login(){
      if(this.user.toLocaleLowerCase() == "admin" && this.password.toLocaleLowerCase() == "admin"){
        console.log(this.user);
        console.log(this.password);
        alert("Bienvenido"+" "+this.user)
        this.router.navigate(['/administrador']);
        localStorage.setItem("userAdmin", this.user);
      }else if(this.user.toLocaleLowerCase() == 'risas' && this.password.toLocaleLowerCase() == 'risas'){
        alert("Bienvenido"+" "+this.user)
        localStorage.setItem("estudiante", this.user);
        localStorage.setItem("carnet", '201801627')
        this.router.navigate(['/estudiante']);
      }else{
        console.log(this.user);
        console.log(this.password);
        alert("No se encuentra ninuguna conincidencia")
      }
  }

  prueba(){
      this.conexion.getUser(this.user, this.password).subscribe({
        next:(info)=>{
          console.log(info)
          if(info.Status == 'Yes'){
            localStorage.setItem("estudiante", info.Nombre)
            localStorage.setItem("carnet", info.Carnet)
            this.router.navigate(['/estudiante'])
            alert("Iniciaste sesion")
            this.user = ""
            this.password =""
          }else if(info.Status == 'admin'){
            alert("Bienvenido"+" "+this.user)
            this.router.navigate(['/administrador']);
            localStorage.setItem("userAdmin", this.user)
          }else if (info.Status == 'No'){
            alert("Correo o Contraseña incorrecto")
          }else{
            alert("Ingresa los campos requeridos")
          }
        }
      });
  }
  
  /*login(){
    console.log(this.user)
    console.log(this.password)

    this.conexion.getUser().subscribe(
      res =>{
        this.data = res;
        for (let i: number = 0; i<this.data.length; i++){
          if(this.user == this.data[i].Carnet && this.password == this.data[i].Password){
            localStorage.setItem("estudiante", this.data[i].Nombre)
            this.router.navigate(['/estudiante'])
            this.existe = true;
            break
          }
        }
        if (!this.existe){
          localStorage.setItem("estudiante", "")
          alert('No coincide ningun dato')
        } 
      }, error => {
        console.log(error);
      }
    );
  }*/
    /*if(this.user.toLocaleLowerCase() == "admin" && this.password.toLocaleLowerCase() == "admin"){
      console.log(this.user);
      console.log(this.password);
      alert("Bienvenido"+" "+this.user)
      this.router.navigate(['/administrador']);
      localStorage.setItem("userAdmin", this.user);
    }else if(this.user.toLocaleLowerCase() == 'risas' && this.password.toLocaleLowerCase() == 'risas'){
      alert("Bienvenido"+" "+this.user)
      localStorage.setItem("estudiante", this.user);
      this.router.navigate(['/estudiante']);
    }else{
      console.log(this.user);
      console.log(this.password);
      alert("No se encuentra ninuguna conincidencia")
    }*/

}
