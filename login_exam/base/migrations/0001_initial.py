# Generated by Django 5.1.7 on 2025-03-25 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
