from django.db import models
from django.urls import reverse
        
class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
       return self.name
    

    def get_absolute_url(self):
        return reverse('home:product_list_by_category',args=[self.slug])
    
class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='product',
                                 on_delete=models.CASCADE)
    
    name = models.CharField(max_length=50,db_index=True)    
    slug = models.CharField(max_length=50,db_index=True,unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)  
    description = models.TextField(max_length=100,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        indexes = [
            models.Index(fields=['id', 'slug']),
        ]

    
    def __str__(self):
        return self.name    
    

    def get_absolute_url(self):
        return reverse('home:product_detail', args=[self.id , self.slug])
    