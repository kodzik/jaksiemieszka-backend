# Generated by Django 3.2.6 on 2022-04-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaksiemieszka', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentrating',
            name='air',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='commentrating',
            name='location',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='commentrating',
            name='noise',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='commentrating',
            name='traffic',
            field=models.IntegerField(),
        ),
    ]