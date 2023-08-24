# Generated by Django 4.2.4 on 2023-08-23 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CopperAssetGraphData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("open", models.DecimalField(decimal_places=3, max_digits=10)),
                ("high", models.DecimalField(decimal_places=3, max_digits=10)),
                ("low", models.DecimalField(decimal_places=3, max_digits=10)),
                ("vol", models.CharField(max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="GoldAssetGraphData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("open", models.DecimalField(decimal_places=3, max_digits=10)),
                ("high", models.DecimalField(decimal_places=3, max_digits=10)),
                ("low", models.DecimalField(decimal_places=3, max_digits=10)),
                ("vol", models.CharField(max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="NaturalGasAssetGraphData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("open", models.DecimalField(decimal_places=3, max_digits=10)),
                ("high", models.DecimalField(decimal_places=3, max_digits=10)),
                ("low", models.DecimalField(decimal_places=3, max_digits=10)),
                ("vol", models.CharField(max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OilAssetGraphData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("open", models.DecimalField(decimal_places=3, max_digits=10)),
                ("high", models.DecimalField(decimal_places=3, max_digits=10)),
                ("low", models.DecimalField(decimal_places=3, max_digits=10)),
                ("vol", models.CharField(max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PlatinumAssetGraphData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("open", models.DecimalField(decimal_places=3, max_digits=10)),
                ("high", models.DecimalField(decimal_places=3, max_digits=10)),
                ("low", models.DecimalField(decimal_places=3, max_digits=10)),
                ("vol", models.CharField(max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SilverAssetGraphData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("open", models.DecimalField(decimal_places=3, max_digits=10)),
                ("high", models.DecimalField(decimal_places=3, max_digits=10)),
                ("low", models.DecimalField(decimal_places=3, max_digits=10)),
                ("vol", models.CharField(max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]