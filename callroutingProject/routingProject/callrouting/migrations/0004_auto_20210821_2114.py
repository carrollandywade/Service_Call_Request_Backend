# Generated by Django 3.1.8 on 2021-08-22 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('callrouting', '0003_auto_20210821_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractedcopier',
            name='customers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='callrouting.customer'),
        ),
    ]
