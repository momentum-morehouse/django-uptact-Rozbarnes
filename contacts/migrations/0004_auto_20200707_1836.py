# Generated by Django 3.0.8 on 2020-07-07 18:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
