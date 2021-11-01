import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-carga',
  templateUrl: './carga.component.html',
  styleUrls: ['./carga.component.css']
})
export class CargaComponent implements OnInit {
  public users : any = "";
  constructor() { }

  ngOnInit(): void {
    this.users = localStorage.getItem("userAdmin");
  }

  cargarEstudiante(){
  document.getElementById("fileInput")?.click()
  }

  readFile(event:any){
    let input = event.target;
    let reader = new FileReader();
    reader.onload = () =>{
      var json = reader.result;
      if (json){
        console.log(json)
      }
    }
    reader.readAsText(input.files[0]);
    alert('Cargados')
  }


}
