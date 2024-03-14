from django.db import models

class Dados(models.Model):
    Sensor = models.BooleanField(default=False)
    Botao = models.BooleanField(default=False)
    LigaRobo = models.BooleanField(default=False)
    ResetContador = models.BooleanField(default=False)
    ValorContagem = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        
        if self.Sensor or self.Botao:
            self.LigaRobo = True
            self.ValorContagem += 1
        else:
            self.LigaRobo = False
        
        if self.ResetContador:
            self.ValorContagem = 0  
        
        super(Dados, self).save(*args, **kwargs)

