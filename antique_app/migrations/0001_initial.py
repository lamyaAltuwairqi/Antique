# Generated by Django 2.2.3 on 2019-07-27 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='images')),
                ('details', models.TextField()),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='antique_app.Category')),
            ],
        ),
    ]