# Generated by Django 3.0.6 on 2020-05-25 22:01

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_auto_20200518_0313"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserMail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_mail", django.contrib.postgres.fields.jsonb.JSONField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.User"
                    ),
                ),
            ],
        ),
    ]