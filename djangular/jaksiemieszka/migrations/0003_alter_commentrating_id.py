# Generated by Django 3.2.6 on 2022-04-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaksiemieszka', '0002_auto_20220403_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentrating',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False),
        ),
    ]
