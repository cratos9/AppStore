# Generated by Django 4.2.16 on 2024-10-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='Imagen', upload_to='media/products'),
        ),
    ]