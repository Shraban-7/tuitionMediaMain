# Generated by Django 3.1.4 on 2020-12-07 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0005_auto_20201207_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='district',
            field=models.ForeignKey(default='select-area', on_delete=django.db.models.deletion.CASCADE, to='tuition.district'),
        ),
    ]