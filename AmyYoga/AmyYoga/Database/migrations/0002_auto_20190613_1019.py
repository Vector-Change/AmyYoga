# Generated by Django 2.2.2 on 2019-06-13 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainerpublish',
            name='nownumber',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
