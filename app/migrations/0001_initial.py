# Generated by Django 4.2.6 on 2023-12-08 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('D_name', models.CharField(max_length=100, unique=True)),
                ('E_deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('D_Loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('E_name', models.CharField(max_length=100, unique=True)),
                ('E_job', models.CharField(max_length=100)),
                ('E_Hiredate', models.DateField()),
                ('E_sal', models.IntegerField()),
                ('E_deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
    ]
