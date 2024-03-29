# Generated by Django 4.2.7 on 2024-02-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business_emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Series_reference', models.CharField(max_length=100)),
                ('Period', models.FloatField(blank=True, null=True)),
                ('Data_value', models.IntegerField(blank=True, null=True)),
                ('Suppressed', models.CharField(blank=True, max_length=100, null=True)),
                ('STATUS', models.CharField(blank=True, max_length=100, null=True)),
                ('UNITS', models.CharField(blank=True, max_length=100, null=True)),
                ('Magnitude', models.IntegerField(blank=True, null=True)),
                ('Subject', models.CharField(blank=True, max_length=100, null=True)),
                ('Group', models.CharField(blank=True, max_length=100, null=True)),
                ('Series_title_1', models.CharField(blank=True, max_length=100, null=True)),
                ('Series_title_2', models.CharField(blank=True, max_length=100, null=True)),
                ('Series_title_3', models.CharField(blank=True, max_length=100, null=True)),
                ('Series_title_4', models.CharField(blank=True, max_length=100, null=True)),
                ('Series_title_5', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
