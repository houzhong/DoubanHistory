# Generated by Django 2.0.2 on 2018-02-04 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('original_title', models.CharField(max_length=70)),
                ('sub_id', models.CharField(max_length=20)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('history_rating', models.CharField(max_length=300)),
                ('playing', models.IntegerField()),
                ('pub_date', models.DateTimeField()),
                ('created_time', models.DateTimeField()),
            ],
        ),
    ]
