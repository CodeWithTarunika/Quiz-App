# Generated by Django 4.1.4 on 2022-12-26 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('opt_1', models.CharField(max_length=200)),
                ('opt_2', models.CharField(max_length=200)),
                ('opt_3', models.CharField(max_length=200)),
                ('opt_4', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=100)),
                ('time_limit', models.IntegerField()),
                ('right_opt', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quizcategory')),
            ],
        ),
    ]
