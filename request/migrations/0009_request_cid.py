# Generated by Django 4.2 on 2023-04-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0008_alter_request_response_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='cid',
            field=models.CharField(blank=True, db_index=True, max_length=36, null=True, verbose_name='correlation id'),
        ),
    ]