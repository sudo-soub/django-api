# Generated by Django 4.0.3 on 2022-03-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(max_length=3, primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
