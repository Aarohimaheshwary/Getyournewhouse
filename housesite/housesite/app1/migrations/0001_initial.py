# Generated by Django 3.0 on 2020-01-02 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images')),
                ('price', models.IntegerField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('desc', models.TextField(max_length=500)),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
