# Generated by Django 4.0.4 on 2022-05-01 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0005_remove_order_time_frame_remove_regulation_time_frame_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hall',
            name='price',
        ),
        migrations.AddField(
            model_name='hall',
            name='dateofo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wedding.dateoforganization'),
        ),
    ]
