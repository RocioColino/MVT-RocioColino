from django.db import models

class Informacion(models.Model):
    nombre=models.CharField("Nombre", max_length=50)
    OPCIONES=(
        (1, "<1.60"),
        (2, "1.60 - 1.65"),
        (3, "1.65 - 1.70"),
        (4, "1.70 - 1.75"),
        (5, "1.75 - 1.80"),
        (6, "1.80 - 1.85"),
        (7, "> 1.85")
    )
    altura=models.FloatField("Altura",choices=OPCIONES)
    nacimiento=models.DateField("Fecha de nacimiento")
      
