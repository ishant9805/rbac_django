# Generated by Django 5.1.6 on 2025-02-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_test_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('school', 'School'), ('parent', 'Parent'), ('student', 'Student')], max_length=7),
        ),
    ]
