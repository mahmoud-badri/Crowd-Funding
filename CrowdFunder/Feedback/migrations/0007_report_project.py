# Generated by Django 4.2.6 on 2023-10-27 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_alter_project_tags'),
        ('Feedback', '0006_remove_report_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='project',
            field=models.ForeignKey(blank=True, null=True,default='', on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='projects.project'),
            preserve_default=False,
        ),
    ]
