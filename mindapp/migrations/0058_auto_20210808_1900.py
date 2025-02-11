# Generated by Django 2.2.10 on 2021-08-08 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mindapp', '0057_auto_20210807_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='completed_or_dead',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='visited_nodes',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='situationtimer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mindapp.Player'),
        ),
    ]
