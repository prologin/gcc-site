from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class Partner(models.Model):

    STATUS_CHOICES = (
        ('avant', 'Avant'),
        ('financement', 'Financement'),
        ('accueil','Accueil'),
    )

    name = models.CharField(
        verbose_name="Nom",
        max_length=256,
    )

    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True,
    )

    website_url = models.URLField(
        verbose_name="URL du site",
        blank=True,
        null=True,
    )


    def upload_to(instance, filename):
        return 'static/img/sponsors/{}'.format(filename)


    #Ne pas mettre une image trop grande
    logo = models.FileField(
        verbose_name="Logo",
        default="",
        upload_to=upload_to,
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])],
    )


    status = models.CharField(
        verbose_name="Statut",
        choices=STATUS_CHOICES,
        max_length=20,
        default='public',
    )




    def __str__(self):
        return self.name