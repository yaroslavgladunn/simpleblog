# Generated by Django 3.2.5 on 2021-07-25 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210725_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]