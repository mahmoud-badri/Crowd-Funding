# Generated by Django 4.2.6 on 2023-10-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_alter_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_featured',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
