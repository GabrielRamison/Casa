from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome} - {self.idade}"

class Casa(models.Model):
    endereco = models.CharField(max_length=100)
    numero_quartos = models.IntegerField(default=1)
    area = models.FloatField()
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Casa em {self.endereco}"
