# Generated by Django 4.0.5 on 2022-07-06 15:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='ali', max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, default='ali', max_length=30, null=True)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee.employee')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.position')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.team')),
            ],
        ),
    ]