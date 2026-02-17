import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  template: ` @if (isServerRunning)
  {
    <span> Server is running </span>
  }
  @else {
  <span>Server is stopped </span>
  }
  `,
})
export class App {
 isServerRunning=true;
}
