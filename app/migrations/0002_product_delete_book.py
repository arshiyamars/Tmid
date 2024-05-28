# Generated by Django 5.0.4 on 2024-05-27 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
