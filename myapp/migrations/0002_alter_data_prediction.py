# Generated by Django 4.2.4 on 2024-05-25 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='prediction',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
