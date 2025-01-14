# Generated by Django 5.1.4 on 2025-01-12 21:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Garment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.PositiveSmallIntegerField(choices=[(1, 'Extra Small'), (2, 'Small'), (3, 'Medium'), (4, 'Large'), (5, 'Extra Large')])),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Shirt'), (2, 'Pants')])),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='garments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'garment',
            },
        ),
    ]