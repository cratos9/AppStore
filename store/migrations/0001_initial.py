# Generated by Django 4.2.16 on 2024-10-03 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(db_index=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_auth.user')),
            ],
        ),
    ]
