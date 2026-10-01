from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    tempo_de_servico = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
<<<<<<< HEAD
    
#objetos = models.Manager()
=======

    objetos = models.Manager()
>>>>>>> 7f6ec5c5a66f13fd0113dd62430dc1b7a1923aef
