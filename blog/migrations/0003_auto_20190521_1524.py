# Generated by Django 2.2.1 on 2019-05-21 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_save'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
