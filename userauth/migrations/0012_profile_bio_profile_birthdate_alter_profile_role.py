# Generated by Django 5.1.3 on 2024-12-10 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0011_alter_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('doctor', 'Doctor'), ('admin', 'Admin')], default='user', max_length=10),
        ),
    ]
