from django.db import models

class Food(models.Model):
    name = models.CharField("Наименование блюда", max_length=200)
    description = models.CharField("Описание", max_length=255)
    image = models.CharField("Ссылка на фото", max_length=300)
    price = models.IntegerField("Цена")

    def __str__(self):
        return self.name
