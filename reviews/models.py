from django.db import models


class Review(models.Model):
    image = models.ImageField(upload_to='reviews/', verbose_name='Фото отзыва')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        db_table = 'reviews'

    def __str__(self):
        return f'Отзыв #{self.id}'
