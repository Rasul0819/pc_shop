# Generated by Django 3.2 on 2023-10-05 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_user_customuser_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ('username',), 'verbose_name': 'User', 'verbose_name_plural': 'Userler'},
        ),
    ]
