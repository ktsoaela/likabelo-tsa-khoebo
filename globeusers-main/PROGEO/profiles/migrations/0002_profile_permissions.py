# Generated by Django 4.2.1 on 2023-05-10 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='profile_set', related_query_name='profile', to='auth.permission', verbose_name='permissions'),
        ),
    ]
