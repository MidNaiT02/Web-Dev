import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  styleUrls: ['app.css'],
  template: ` <div [contentEditable]="isEditable">
    <img alt="photo" [src]="imageURL" />
  </div> `,
})
export class App {
  isEditable=true;
  imageURL="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRO7lWp0y5h-DjbStErtxnSngZfSZdf04PY31YzbcyCOVMTfiBU76wkHmAZ7V6aY-l7VLxnk74-VWoAzcpPnTsaiFGUZ6X8U0-dXCdDYR9v&s=10";
}
