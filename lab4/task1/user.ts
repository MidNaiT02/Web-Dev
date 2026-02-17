import { Component } from '@angular/core';
import { NgOptimizedImage } from '@angular/common';

@Component({
  selector: 'app-user',
  standalone: true,
  imports: [NgOptimizedImage],
  template: `
    <p>Username: {{ username }}</p>
    <p>Preferred Framework:</p>

    <ul>
      <li>
        Static Image:
        <img ngSrc="/logo.svg" alt="Angular logo" width="32" height="32" />
      </li>

      <li>
        Dynamic Image:
        <img [ngSrc]="logoUrl" [alt]="logoAlt" width="32" height="32" />
      </li>
    </ul>

    <div class="image-container">
      <img ngSrc="https://www.example.com/image.png" fill />
    </div>

    <img 
      ngSrc="https://www.example.com/image.png" 
      height="600" 
      width="800" 
      priority 
    />
  `,
  styles: [`
    .image-container {
      position: relative;
      width: 300px;
      height: 200px;
    }
  `]
})
export class User {
  logoUrl = '/logo.svg';
  logoAlt = 'Angular logo';
  username = 'youngTech';
}
