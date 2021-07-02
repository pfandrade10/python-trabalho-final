from django.db import models

# No caso, o Telefone realmente pode ser de várias pessoas
class Telefone(models.Model):
	ddd = models.IntegerField(default=0)
	numero = models.BigIntegerField(default=0)
	temWhatsapp = models.BooleanField()