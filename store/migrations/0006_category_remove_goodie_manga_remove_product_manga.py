# Generated by Django 4.2.5 on 2024-01-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_goodie_manga_product_manga'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='products')),
            ],
        ),
        migrations.RemoveField(
            model_name='goodie',
            name='manga',
        ),
        migrations.RemoveField(
            model_name='product',
            name='manga',
        ),
    ]
