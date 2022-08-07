# Generated by Django 4.0.5 on 2022-08-05 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evaluation', '0004_alter_evaluation_id_alter_relationship_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation_id', models.CharField(max_length=100)),
                ('reviewee_last_name', models.CharField(max_length=100)),
                ('question_category', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=30000)),
                ('reviewee_own_answer', models.CharField(max_length=30000)),
                ('reviewee_own_answer_score', models.FloatField()),
                ('other_avg', models.FloatField()),
                ('difference', models.FloatField()),
                ('department_avg', models.FloatField()),
            ],
            options={
                'db_table': 'results',
                'managed': False,
            },
        ),
    ]