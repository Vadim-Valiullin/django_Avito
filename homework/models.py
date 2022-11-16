from django.db import models


from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=250, blank=True)
    price = models.PositiveIntegerField(blank=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    is_published = models.BooleanField(default=False)
    # image = models.ImageField(upload_to='pictures/', null=True, blank=True)
    # category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    class Meta:

        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=80, db_index=True)

    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
