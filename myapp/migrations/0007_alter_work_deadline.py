# Generated by Django 4.0.5 on 2022-07-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_work_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='deadline',
            field=models.CharField(max_length=50),
        ),
    ]