# Generated by Django 4.0.1 on 2022-01-20 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('choice', models.CharField(max_length=5)),
                ('needs_recommendation', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.question')),
            ],
            options={
                'db_table': 'answers',
                'order_with_respect_to': 'question',
            },
        ),
    ]
