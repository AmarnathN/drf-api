# Generated by Django 3.0.7 on 2020-06-14 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0005_auto_20200526_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetflixProfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.User')),
            ],
            options={
                'ordering': ['user'],
                'unique_together': {('user', 'profile')},
            },
        ),
    ]
