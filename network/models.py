from django.db.models import Model, EmailField, CharField, DateField, DateTimeField, \
    DecimalField, ForeignKey, CASCADE, SET_NULL, TextChoices


NULLABLE = {"null": True, "blank": True}


class NetworkElementName(TextChoices):
    factory = "Factory"
    retail_chain = "Retail chain"
    individual_entrepreneur = "Individual entrepreneur"


class Company(Model):
    name = CharField(max_length=150, verbose_name="Название")
    supplier = ForeignKey('Company', on_delete=SET_NULL, verbose_name="Поставщик", related_name='customers',
                          **NULLABLE)
    indebtedness = DecimalField(max_digits=15, decimal_places=2,
                                verbose_name="Задолженность перед поставщиком в денежном выражении", **NULLABLE)
    created_at = DateTimeField(verbose_name="Время создания", auto_now_add=True)

    company_type = CharField(max_length=50, choices=NetworkElementName)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Contact(Model):
    email = EmailField(max_length=100, verbose_name="Email", unique=True)
    country = CharField(max_length=100, verbose_name="Страна")
    city = CharField(max_length=100, verbose_name="Город")
    street = CharField(max_length=100, verbose_name="Улица")
    building = CharField(max_length=10, verbose_name="Номер дома")

    company = ForeignKey(Company, on_delete=CASCADE, verbose_name="Компания", related_name="contacts")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Product(Model):
    name = CharField(verbose_name="Название")
    model = CharField(verbose_name="Модель")
    launch_date = DateField(verbose_name="Дата выхода продукта на рынок")

    company = ForeignKey(Company, on_delete=CASCADE, verbose_name="Компания", related_name="products")

    def __str__(self):
        return f'{self.name} ({self.model})'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
