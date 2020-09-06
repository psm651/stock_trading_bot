# Generated by Django 3.1.1 on 2020-09-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(help_text='user email', max_length=254)),
                ('password', models.TextField(help_text='encrypted text')),
                ('name', models.CharField(max_length=20)),
                ('level', models.IntegerField()),
                ('active', models.CharField(help_text='userId active status Y 사용중, H 휴면, N 삭제', max_length=5)),
                ('tendency_id', models.IntegerField(help_text='stock tendency key')),
                ('created', models.DateField(auto_now_add=True, help_text='created id date')),
                ('updated', models.DateField(auto_now=True, help_text='update id date')),
            ],
        ),
    ]
