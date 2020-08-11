# Generated by Django 3.0.8 on 2020-08-19 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("transactions", "0003_remove_transaction_budget"),
    ]

    operations = [
        migrations.RemoveField(model_name="transaction", name="account",),
        migrations.RemoveField(model_name="transaction", name="category",),
        migrations.AddField(
            model_name="transaction",
            name="from_account",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="transaction",
            name="to_account",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="transaction",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
