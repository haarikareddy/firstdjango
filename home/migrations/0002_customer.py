# Generated by Django 2.2.2 on 2019-06-21 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(help_text='Customer Name', max_length=100, null=True)),
                ('bname', models.CharField(help_text='Book_ Name', max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('booktook', models.DateField(blank=True, null=True, verbose_name='Return')),
                ('bookret', models.DateField(blank=True, null=True, verbose_name='Return')),
            ],
        ),
    ]
