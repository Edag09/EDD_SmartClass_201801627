import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AdministradorComponent } from './administrador/administrador.component';
import { EstudianteComponent } from './estudiante/estudiante.component';
import { ApuntesComponent } from './apuntes/apuntes.component';
import { TareasComponent } from './tareas/tareas.component';
import { CursosComponent } from './cursos/cursos.component';
import { CargaComponent } from './carga/carga.component';
import { ReportesComponent } from './reportes/reportes.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegistroComponent,
    AdministradorComponent,
    EstudianteComponent,
    ApuntesComponent,
    TareasComponent,
    CursosComponent,
    CargaComponent,
    ReportesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent],

})
export class AppModule { }
