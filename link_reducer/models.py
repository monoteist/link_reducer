from django.db import models


class Link(models.Model):
    original_link = models.URLField()
    shortened_link = models.CharField("Короткий URL", max_length=50)
    redirect_count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.original_link

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
