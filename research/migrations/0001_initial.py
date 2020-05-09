# Generated by Django 3.0.5 on 2020-05-08 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0001_initial'),
        ('recipient', '0001_initial'),
        ('answer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateField()),
                ('hasresponded', models.IntegerField()),
                ('date_responded', models.DateField()),
                ('file_name', models.CharField(max_length=50)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipient.Recipient')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='answer.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipient.Recipient')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research.Survey')),
            ],
        ),
    ]
