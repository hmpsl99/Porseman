# Generated by Django 4.0.5 on 2022-08-16 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QA', '0011_category_new_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_new',
            name='text',
        ),
    ]
