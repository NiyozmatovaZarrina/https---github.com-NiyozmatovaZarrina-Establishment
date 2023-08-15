from django.db import models

# Create your models here.

class Contact(models.Model):

    phone = models.IntegerField("Номер_телефона")
    homephone = models.IntegerField("Номер_телефона")
    email = models.EmailField("Почта")
    time=models.DateTimeField("Время", auto_now=False, auto_now_add=True)
    image=models.ImageField("Фото", upload_to=None, height_field=None, width_field=None, max_length=None)
    name = models.ForeignKey("names.name", related_name="contact", on_delete=models.CASCADE)
    
    
    @property
    def rating(self):
        return 10
        
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["phone"]

    def __int__(self) -> str:
        return self.phone
