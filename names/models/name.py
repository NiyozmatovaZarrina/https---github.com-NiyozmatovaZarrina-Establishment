from django.db import models


class Name(models.Model):

    title = models.CharField("Название", max_length=150)
    address= models.CharField("Адрес", max_length=150)
    city = models.ForeignKey("cities.city", related_name="city", on_delete=models.CASCADE)
    category = models.ForeignKey("categories.category", related_name="category", on_delete=models.CASCADE)
    
    @property
    def rating(self):
        return 10

    class Meta:
        verbose_name = "Название_завидения"
        verbose_name_plural = "Название_завидении"
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title