# Generated by Django 4.0.4 on 2022-05-23 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='GenericName', max_length=50),
            preserve_default=False,
        ),
    ]