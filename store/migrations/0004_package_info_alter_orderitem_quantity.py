# Generated by Django 4.1.1 on 2023-01-18 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='info',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
