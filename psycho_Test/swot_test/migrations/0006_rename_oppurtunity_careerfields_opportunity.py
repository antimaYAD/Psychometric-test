# Generated by Django 5.1.2 on 2024-11-06 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swot_test', '0005_strengthweakness_delete_srengthweakness'),
    ]

    operations = [
        migrations.RenameField(
            model_name='careerfields',
            old_name='oppurtunity',
            new_name='opportunity',
        ),
    ]
