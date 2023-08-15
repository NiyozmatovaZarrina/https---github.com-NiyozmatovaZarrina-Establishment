from django.db import models

# Create your models here.
from django.db import models


class Commit(models.Model):

    title = models.TextField("Название")
    name = models.ForeignKey("work.name", related_name="commit", on_delete=models.CASCADE)
    
    
    @property
    def rating(self):
        return 10

    class Meta:
        verbose_name = "Коментария"
        verbose_name_plural = "Коментарии"
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
