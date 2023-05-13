# Generated by Django 3.0.8 on 2023-05-05 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20230502_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Выберите автора книги', to='catalog.Author', verbose_name='Aвтop  книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Выберите язык книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Language', verbose_name='Язык книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='Введите название книги', max_length=200, null=True, verbose_name='Название  книги'),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='imprint',
            field=models.CharField(help_text='Введите издательство и год выnуска', max_length=200, null=True, verbose_name='Издательство'),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='inv_nom',
            field=models.CharField(help_text='Введите инвентарный  номер  экземпляра', max_length=20, null=True, verbose_name='Инвентарный  номер'),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='status',
            field=models.ForeignKey(help_text='Изменить состояние экземпляра', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Status', verbose_name='Cтaтyc экземпляра книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(help_text='Введите краткое  описание книги', max_length=1000, verbose_name='Аннотация  книги'),
        ),
    ]
