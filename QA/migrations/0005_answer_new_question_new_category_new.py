# Generated by Django 4.0.5 on 2022-08-16 11:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('QA', '0004_alter_answer_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('score', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QA.answer_new')),
            ],
        ),
        migrations.CreateModel(
            name='Category_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=500)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QA.question')),
            ],
        ),
    ]
