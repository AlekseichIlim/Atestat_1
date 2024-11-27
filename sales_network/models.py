from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название продукта")
    model = models.CharField(max_length=50, verbose_name='Модель продукта')
    release_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class NetworkLink(models.Model):

    LEVEL_CHOICES = [
        ('ZERO', 0),
        ('ONE', 1),
        ('TWO', 2)
    ]
    level = models.CharField(max_length=4, choices=LEVEL_CHOICES, default=0, verbose_name="Уровень в сети")
    title = models.CharField(max_length=100, verbose_name="Название")
    email = models.EmailField()
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=50, verbose_name='Улица', **NULLABLE)
    house_number = models.IntegerField(verbose_name='Номер дома', **NULLABLE)
    product = models.ManyToManyField(Product, verbose_name='Продукт')
    provider = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name="Поставщик", **NULLABLE)
    arrears = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Долг перед поставщиком", **NULLABLE)
    # url = models.URLField(verbose_name="Ссылка")
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
