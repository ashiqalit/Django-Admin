# Generated by Django 4.2.7 on 2023-11-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_heading_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='heading',
            name='desc',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='heading',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]