# Generated by Django 2.0.2 on 2018-06-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0031_auto_20180620_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectusermembership',
            name='previous_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Awaiting Authorisation'), (1, 'Authorised'), (2, 'Declined'), (3, 'Revoked'), (4, 'Suspended')], default=0, verbose_name='Previous Status'),
        ),
        migrations.AlterField(
            model_name='projectusermembership',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Awaiting Authorisation'), (1, 'Authorised'), (2, 'Declined'), (3, 'Revoked'), (4, 'Suspended')], default=0, verbose_name='Current Status'),
        ),
    ]
