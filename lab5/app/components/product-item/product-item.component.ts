import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-item',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css'],
})
export class ProductItemComponent {
  @Input() product!: Product;
  @Output() deleteProduct = new EventEmitter<number>();

  currentImageIndex = 0;
  showConfirm = false;

  nextImage(): void {
    this.currentImageIndex =
      (this.currentImageIndex + 1) % this.product.images.length;
  }

  prevImage(): void {
    this.currentImageIndex =
      (this.currentImageIndex - 1 + this.product.images.length) %
      this.product.images.length;
  }

  setImage(index: number): void {
    this.currentImageIndex = index;
  }

  like(): void {
    this.product.likes++;
  }

  requestDelete(): void {
    this.showConfirm = true;
  }

  confirmDelete(): void {
    this.showConfirm = false;
    this.deleteProduct.emit(this.product.id);
  }

  cancelDelete(): void {
    this.showConfirm = false;
  }

  shareWhatsApp(): void {
    const url = encodeURIComponent(this.product.link);
    window.open(`https://wa.me/?text=Check out this product: ${url}`, '_blank');
  }

  shareTelegram(): void {
    const url  = encodeURIComponent(this.product.link);
    const text = encodeURIComponent(this.product.name);
    window.open(`https://t.me/share/url?url=${url}&text=${text}`, '_blank');
  }
}
