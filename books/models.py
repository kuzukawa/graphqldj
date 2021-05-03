from django.db import models
from django.utils.translation import ugettext_lazy  as _

class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Book (models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    author = models.ForeignKey(
        "books.Author", related_name="books",on_delete=models.CASCADE)
    published_date = models.DateField()
    
    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
