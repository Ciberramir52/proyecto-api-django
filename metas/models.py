from django.db import models

# Create your models here.
PERIODO = [
    ('dia', 'Dia'),
    ('semana', 'Semana'),
    ('mes', 'Mes'),
    ('anio', 'Anio')
]

class Metas(models.Model):
    id = models.IntegerField(primary_key=True)
    detalles = models.TextField()
    periodo = models.CharField(max_length=6, choices=PERIODO)
    eventos = models.IntegerField()
    icono = models.TextField(null=True)
    meta = models.IntegerField(null=True)
    plazo = models.DateField()
    completado = models.IntegerField(default=0)
    cuenta_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'metas'
    
    def dict(self):
        return {
            'id': self.id,
            'detalles': self.detalles,
            'periodo': self.periodo,
            'eventos': self.eventos,
            'icono': self.icono,
            'meta': self.meta,
            'plazo': self.plazo,
            'completado': self.completado
        }
