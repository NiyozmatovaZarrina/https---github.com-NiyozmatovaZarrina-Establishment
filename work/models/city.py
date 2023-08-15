from django.db import models


class City(models.Model):

    name = models.CharField("Название_города", max_length=150)
    
    @property
    def rating(self):
        return 10

    class Meta:
        verbose_name = "Название_города"
        verbose_name_plural = "Название_городов"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
