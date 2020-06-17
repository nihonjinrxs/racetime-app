# Generated by Django 3.0.7 on 2020-06-17 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racetime', '0035_auto_20200616_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug_words',
            field=models.TextField(blank=True, default=None, help_text='Set a number of words to be picked at random for race room names. If set, you must provide a minimum of 50 distinct words to use. Changing slug words will not impact existing race rooms.', null=True),
        ),
    ]
