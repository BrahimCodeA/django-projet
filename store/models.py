from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.views.generic import ListView

from DekuShopp.settings import AUTH_USER_MODEL

User = get_user_model()
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=128, choices=[("MHA", "MHA"), ("Naruto", "Naruto"), ("OnePiece", "OnePiece")])
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})
    
class Goodie(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=128, choices=[("MHA", "MHA"), ("Naruto", "Naruto"), ("OnePiece", "OnePiece")])
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("goodie", kwargs={"slug": self.slug})  
    
class MHACategoryView(ListView):
    model = Product  # Ou Goodie selon ce que vous voulez afficher
    template_name = 'mha_category.html'  # Créez ce fichier dans votre dossier templates

    def get_queryset(self):
        return self.model.objects.filter(category='MHA')

class NarutoCategoryView(ListView):
    model = Product  # Ou Goodie selon ce que vous voulez afficher
    template_name = 'naruto_category.html'  # Créez ce fichier dans votre dossier templates

    def get_queryset(self):
        return self.model.objects.filter(category='Naruto')

class OnePieceCategoryView(ListView):
    model = Product  # Ou Goodie selon ce que vous voulez afficher
    template_name = 'onepiece_category.html'  # Créez ce fichier dans votre dossier templates

    def get_queryset(self):
        return self.model.objects.filter(category='OnePiece')
 
    
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,  null=True, blank=True)
    goodie = models.ForeignKey(Goodie, on_delete=models.CASCADE,  null=True, blank=True)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        if self.product:
            return f"{self.product.name} ({self.quantity})"
        elif self.goodie:
            return f"{self.goodie.name} ({self.quantity})"
        else:
            return f"Order ({self.quantity})"
    
    
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)  # Assurez-vous que le modèle Order est correctement défini

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        # Marquer toutes les commandes comme "commandées"
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        # Retirer toutes les commandes du panier
        self.orders.clear()

        super().delete(*args, **kwargs)
        
    def calculate_total(self):
        total = sum(
            (order.product.price if order.product else order.goodie.price) * order.quantity
            for order in self.orders.filter(ordered=False)
        )
        return total
    


