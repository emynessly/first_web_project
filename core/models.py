from django.db import models
from django.urls import reverse
from django.conf import settings

class Author(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ("name",)
    
    def __str__(self) -> str:
        return self.name
    
    
class Book(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    publish_year = models.PositiveIntegerField(null=False, blank=False, verbose_name="Год издания")
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
        null=True,
        related_name="books",
        verbose_name="Автор"
    )
    
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True
    )
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Стоимость",
        null=True,
        blank=True
    )
    
    writer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_books",
        verbose_name="Кто добавил"
    )
    
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ("name",)
        
    def __str__(self):
        return f"{self.author}: \"{self.name}\""
    
    def get_absolute_url(self):
        return reverse('core:book_detail', kwargs={'pk': self.pk})