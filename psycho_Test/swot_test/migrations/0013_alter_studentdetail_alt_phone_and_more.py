# Generated by Django 5.1.2 on 2024-11-07 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swot_test', '0012_remove_question_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetail',
            name='alt_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='studentdetail',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
