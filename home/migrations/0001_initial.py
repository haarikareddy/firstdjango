# Generated by Django 2.2.2 on 2019-06-19 10:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(help_text='Name of Author', max_length=100, null=True)),
                ('total_book_written', models.CharField(choices=[('1', 'one'), ('2', 'two')], max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Birth')),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Death')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Book Name', max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='uique id', primary_key=True, serialize=False, verbose_name='Book Id')),
                ('name', models.CharField(help_text='Book Name', max_length=100, null=True)),
                ('purchase_date', models.DateField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(help_text='Book Author', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Author')),
                ('genre', models.ManyToManyField(help_text='genre of book', to='home.Genre')),
            ],
        ),
    ]
