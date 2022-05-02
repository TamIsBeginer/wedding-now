# Generated by Django 4.0.4 on 2022-05-01 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0006_remove_hall_price_hall_dateofo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regulation',
            name='price',
        ),
        migrations.AddField(
            model_name='dateoforganization',
            name='regulation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wedding.regulation'),
        ),
        migrations.AddField(
            model_name='hall',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='regulation',
            name='change_price',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='hall',
            name='dateofo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wedding.dateoforganization'),
        ),
    ]
