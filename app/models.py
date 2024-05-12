from django.db import models
from django.contrib.auth import get_user_model


class Note(models.Model):
    name = models.CharField(max_length=80, verbose_name='Название')
    date_create = models.DateField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    is_active = models.BooleanField(default=True, verbose_name='Состояние')

    def __str__(self) -> str:
        return self.name
