# Generated by Django 4.2 on 2023-04-19 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_customuser_cover_photo_alter_note_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
    ]