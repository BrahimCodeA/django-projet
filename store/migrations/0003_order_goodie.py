# Generated by Django 4.2.5 on 2023-12-27 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_goodie'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='goodie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.goodie'),
        ),
    ]