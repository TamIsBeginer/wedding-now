# Generated by Django 4.0.4 on 2022-05-01 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0008_alter_hall_dateofo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regulation',
            name='change_price',
        ),
        migrations.AddField(
            model_name='regulation',
            name='morning_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='regulation',
            name='night_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='regulation',
            name='noon_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='regulation',
            name='weekend_price',
            field=models.FloatField(null=True),
        ),
    ]