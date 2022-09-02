# Generated by Django 4.0.3 on 2022-03-25 18:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monument', '0008_monument_saved'),
    ]

    operations = [
        migrations.AddField(
            model_name='monument',
            name='city',
            field=models.CharField(blank=True, default='Casablanca', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='monument',
            name='saved',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
