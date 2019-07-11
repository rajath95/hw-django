# Generated by Django 2.0 on 2019-07-10 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hwd', '0002_auto_20190710_0611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='4', max_length=5)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
    ]
