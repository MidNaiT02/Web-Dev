
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../../models/product.model';
import { ProductCardComponent } from '../product-card/product-card.component';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [CommonModule, ProductCardComponent],
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {

  products: Product[] = [
    {
      id: 1,
      name: 'iPhone 15 Pro',
      description: 'Latest Apple smartphone with A17 Pro chip and titanium body.',
      price: 649990,
      rating: 4.9,
      image: 'https://resources.cdn-kaspi.kz/img/m/p/h1.jpg',
      images: [
        'https://resources.cdn-kaspi.kz/img/m/p/h1.jpg',
        'https://resources.cdn-kaspi.kz/img/m/p/h2.jpg',
        'https://resources.cdn-kaspi.kz/img/m/p/h3.jpg'
      ],
      link: 'https://kaspi.kz/shop/p/apple-iphone-15-pro-113138130/'
    },
    {
      id: 2,
      name: 'Samsung Galaxy S24',
      description: 'Flagship Samsung smartphone with AI camera system.',
      price: 559990,
      rating: 4.8,
      image: 'https://resources.cdn-kaspi.kz/img/m/p/s1.jpg',
      images: [
        'https://resources.cdn-kaspi.kz/img/m/p/s1.jpg',
        'https://resources.cdn-kaspi.kz/img/m/p/s2.jpg',
        'https://resources.cdn-kaspi.kz/img/m/p/s3.jpg'
      ],
      link: 'https://kaspi.kz/shop/p/samsung-galaxy-s24-113138128/'
    }
  ];
}
