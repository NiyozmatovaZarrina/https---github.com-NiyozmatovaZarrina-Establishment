# Generated by Django 4.2.3 on 2023-08-15 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('names', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(verbose_name='Номер_телефона')),
                ('homephone', models.IntegerField(verbose_name='Номер_телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
                ('image', models.ImageField(upload_to=None, verbose_name='Фото')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='names.name')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
                'ordering': ['phone'],
            },
        ),
    ]
