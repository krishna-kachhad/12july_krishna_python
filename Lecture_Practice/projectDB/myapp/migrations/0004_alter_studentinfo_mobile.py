# Generated by Django 4.2.6 on 2023-11-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_studentinfo_created_studentinfo_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
