# Generated by Django 4.2.10 on 2024-03-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_streem'),
    ]

    operations = [
        migrations.AddField(
            model_name='streem',
            name='grade',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='streem',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
