# Generated by Django 3.1.6 on 2022-02-19 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_accountaudit_auditors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountaudit',
            old_name='auditors',
            new_name='auditor',
        ),
    ]
