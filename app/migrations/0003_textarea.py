# Generated by Django 5.0.4 on 2024-05-27 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Textarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
    ]