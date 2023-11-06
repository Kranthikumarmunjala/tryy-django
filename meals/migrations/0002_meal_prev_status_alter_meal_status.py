# Generated by Django 4.1.5 on 2023-11-06 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='prev_status',
            field=models.CharField(choices=[('p', 'Pending'), ('c', 'Completed'), ('eExpired', 'Expired'), ('aAborted', 'Aborted'), ("[('a', 'Aborted')]", 'Meal Choices')], default=None, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='status',
            field=models.CharField(choices=[('p', 'Pending'), ('c', 'Completed'), ('eExpired', 'Expired'), ('aAborted', 'Aborted'), ("[('a', 'Aborted')]", 'Meal Choices')], default='p', max_length=18),
        ),
    ]
