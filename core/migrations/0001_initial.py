# Generated by Django 3.2.25 on 2024-11-29 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Продукты питания', 'Продукты питания'), ('Стекло', 'Стекло'), ('Электроника', 'Электроника'), ('Мебель', 'Мебель')], max_length=50)),
                ('type', models.CharField(choices=[('Легкий', 'Легкий'), ('Тяжелый', 'Тяжелый'), ('Хрупкий', 'Хрупкий'), ('Опасный', 'Опасный')], max_length=50)),
                ('weight', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
