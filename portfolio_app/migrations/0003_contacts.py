# Generated by Django 3.0.6 on 2020-12-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=300)),
                ('Messages', models.TextField(max_length=400)),
            ],
        ),
    ]