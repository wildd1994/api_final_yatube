# Generated by Django 3.1.3 on 2020-11-30 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201126_1509'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_list',
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_posts', to='api.group', verbose_name='Группа'),
        ),
    ]
