# Generated by Django 3.0.6 on 2020-12-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0005_auto_20201210_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
    ]
