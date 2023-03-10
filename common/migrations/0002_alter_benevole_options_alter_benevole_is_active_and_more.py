# Generated by Django 4.1.6 on 2023-02-11 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="benevole",
            options={"verbose_name": "Bénévole", "verbose_name_plural": "Bénévoles"},
        ),
        migrations.AlterField(
            model_name="benevole",
            name="is_active",
            field=models.BooleanField(verbose_name="Compte activé"),
        ),
        migrations.AlterField(
            model_name="benevole",
            name="is_staff",
            field=models.BooleanField(verbose_name="Admin site"),
        ),
    ]
