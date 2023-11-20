from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_in_stock = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='products',default='defaults/aa.png')

    class Meta:
        verbose_name = "ÜRÜN"
        verbose_name_plural = "ÜRÜNLER"

    def __str__(self):
        return f"{self.name} - {self.slug}"
    

class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='riviews')
    review = models.TextField()
    is_released = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"{self.product.name} - {self.review}"