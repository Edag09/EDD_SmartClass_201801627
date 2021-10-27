import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdministradorComponent } from './administrador/administrador.component';
import { ApuntesComponent } from './apuntes/apuntes.component';
import { CursosComponent } from './cursos/cursos.component';
import { EstudianteComponent } from './estudiante/estudiante.component';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';
import { TareasComponent } from './tareas/tareas.component';

const routes: Routes = [
  { path: '', component: LoginComponent},
  //{ path: ':user/:password', component: LoginComponent},
  { path: 'apuntes', component: ApuntesComponent },
  { path: 'cursos', component: CursosComponent},
  { path: 'tareas', component: TareasComponent},
  { path: 'registro', component: RegistroComponent},
  { path: 'administrador', component: AdministradorComponent},
  { path: 'estudiante', component: EstudianteComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
