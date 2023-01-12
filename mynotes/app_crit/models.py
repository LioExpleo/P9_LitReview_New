import django.db.models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


from django.db.models import DateTimeField
import datetime


class Abonnement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #description = models.TextField(max_length=2048, blank=True)

    #time_created = models.DateField(auto_now_add=False, auto_now=False, default=django.utils.timezone.now())

    def __str__(self):
        return self.title
'''
class Flux(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
'''
class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateField(auto_now_add=True) #, auto_now=False, default=django.utils.timezone.now())
    #time_created = models.DateTimeField(default=datetime.date.today())
    # bodytest = models.TextField(max_length=8192, blank=True, verbose_name="Commentaire")

class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True, verbose_name="Commentaire")
    #time_created = models.DateField(auto_now_add=False, auto_now=False, default=django.utils.timezone.now())
    #time_created = models.DateField(auto_now_add=True)
    #time_created = models.DateField(default=datetime.date.today())

class Review2(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True, verbose_name="Commentaire")
    time_created = models.DateField(auto_now_add=True)

class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

    class Meta :
        unique_together = ('user', 'followed_user')
