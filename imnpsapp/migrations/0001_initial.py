# Generated by Django 5.1.4 on 2024-12-09 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imnps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('rollno', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
