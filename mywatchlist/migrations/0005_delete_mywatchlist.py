# Generated by Django 4.1 on 2022-09-21 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mywatchlist", "0004_mywatchlistmodel"),
    ]

    operations = [
        migrations.DeleteModel(
            name="MyWatchList",
        ),
    ]