# Generated by Django 2.0.2 on 2018-08-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0012_institution_funding_database_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='allows_rse_requests',
            field=models.BooleanField(default=False),
        ),
    ]
