# Generated by Django 3.1.4 on 2021-07-29 19:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myfolio', '0002_auto_20210728_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Querry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subect', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='tags',
            name='tag_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='age',
            field=models.IntegerField(),
        ),
    ]
