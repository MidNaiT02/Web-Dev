import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Category } from './models/category.model';
import { Product } from './models/product.model';
import { ProductService } from './services/product.service';
import { ProductListComponent } from './components/product-list/product-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, ProductListComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  categories: Category[] = [];
  allProducts: Product[] = [];
  selectedCategory: Category | null = null;
  visibleProducts: Product[] = [];

  constructor(private productService: ProductService) {}

  ngOnInit(): void {
    this.categories = this.productService.getCategories();
    this.allProducts = this.productService.getProducts();
  }

  selectCategory(category: Category): void {
    this.selectedCategory = category;
    this.visibleProducts = this.allProducts.filter(
      (p) => p.categoryId === category.id
    );
  }

  onProductDeleted(productId: number): void {
    this.visibleProducts = this.visibleProducts.filter((p) => p.id !== productId);
    this.allProducts = this.allProducts.filter((p) => p.id !== productId);
  }
}