# Generated by Django 3.1.2 on 2020-11-01 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zoo', '0004_auto_20201101_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zookeeper',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
