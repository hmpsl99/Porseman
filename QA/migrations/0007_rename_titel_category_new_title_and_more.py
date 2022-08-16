# Generated by Django 4.0.5 on 2022-08-16 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QA', '0006_alter_category_new_question_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category_new',
            old_name='titel',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='category_new',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QA.question_new'),
        ),
    ]
