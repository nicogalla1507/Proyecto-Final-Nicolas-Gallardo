# Generated by Django 4.2.5 on 2023-10-12 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0004_acercademi_delete_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='acercademi',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
