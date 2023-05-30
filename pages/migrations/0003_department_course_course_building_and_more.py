# Generated by Django 4.2.1 on 2023-05-23 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_lecturer_lecturer_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('department_code', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_building',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='course_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.department'),
        ),
    ]
