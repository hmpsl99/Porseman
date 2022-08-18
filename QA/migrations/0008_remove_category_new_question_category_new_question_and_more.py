# Generated by Django 4.0.5 on 2022-08-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QA', '0007_rename_titel_category_new_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category_new',
            name='question',
        ),
        migrations.AddField(
            model_name='category_new',
            name='question',
            field=models.ManyToManyField(null=True, to='QA.question_new'),
        ),
        migrations.RemoveField(
            model_name='question_new',
            name='answer',
        ),
        migrations.AddField(
            model_name='question_new',
            name='answer',
            field=models.ManyToManyField(null=True, to='QA.answer_new'),
        ),
    ]