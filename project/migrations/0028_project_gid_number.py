# Generated by Django 2.0.2 on 2018-06-19 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0027_auto_20180617_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='gid_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='OpenLDAP GID Number'),
        ),
    ]
