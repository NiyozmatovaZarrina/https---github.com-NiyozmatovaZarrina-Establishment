from django.db import models


class Category(models.Model):

    name = models.CharField("Название", max_length=150)
    
    
    @property
    def rating(self):
        return 10

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Котегории"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name