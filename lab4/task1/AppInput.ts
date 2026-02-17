import {Component, input} from '@angular/core';

@Component({
    selector: 'app-root',
    template: '<p> The user name is {{name()}}</p>'
})

export class App {
    readonly name=input <string>();
}