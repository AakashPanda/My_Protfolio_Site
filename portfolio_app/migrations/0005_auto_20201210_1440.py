# Generated by Django 3.0.6 on 2020-12-10 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
