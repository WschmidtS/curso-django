# Generated by Django 3.1 on 2020-08-23 23:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('titulo', models.CharField(max_length=64)),
                ('publico', models.TextField()),
                ('descricao', models.TextField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
