# Generated by Django 4.2.2 on 2024-11-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sales_network", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="networklink",
            name="arrears",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Долг перед поставщиком",
            ),
        ),
        migrations.AlterField(
            model_name="networklink",
            name="level",
            field=models.CharField(
                choices=[("ZERO", 0), ("ONE", 1), ("TWO", 2)],
                default=0,
                max_length=4,
                verbose_name="Уровень в сети",
            ),
        ),
    ]
