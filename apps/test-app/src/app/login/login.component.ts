import { Component, OnInit } from '@angular/core';
import {User} from "../User";

@Component({
  selector: 'front-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  user: User = {
    login: "admin",
    password: 'admin'
  };

  constructor() { }

  ngOnInit(): void {
  }

}
