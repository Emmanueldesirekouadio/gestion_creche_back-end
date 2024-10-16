# Generated by Django 5.1.2 on 2024-10-16 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allergiesmodel',
            name='enfant',
        ),
        migrations.RemoveField(
            model_name='specifiedneedsmodel',
            name='enfant',
        ),
        migrations.AddField(
            model_name='allergiesmodel',
            name='enfant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='child.childmodel'),
        ),
        migrations.AddField(
            model_name='specifiedneedsmodel',
            name='enfant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='child.childmodel'),
        ),
    ]
