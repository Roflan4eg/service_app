# Generated by Django 3.2.16 on 2023-08-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_subscription_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='field_a',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='subscription',
            name='field_b',
            field=models.CharField(default='', max_length=255),
        ),
    ]
