# Generated by Django 4.2.5 on 2023-10-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_informacionagregada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('biografia', models.TextField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='autor_fotos/')),
            ],
        ),
        migrations.DeleteModel(
            name='InformacionAgregada',
        ),
    ]
