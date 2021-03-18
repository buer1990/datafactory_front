# Generated by Django 3.1 on 2020-10-29 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
               da ('tool_name', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField(verbose_name='Create time')),
            ],
        ),
        migrations.CreateModel(
            name='ToolAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr_describe', models.CharField(max_length=200)),
                ('attr_value', models.CharField(blank=True, max_length=200)),
                ('attr_type', models.IntegerField(choices=[(0, 'text'), (1, 'number'), (2, 'date'), (3, 'tel'), (4, 'time'), (5, 'email'), (6, 'datetime-local')], default=0)),
                ('tool_path', models.CharField(max_length=200)),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datafactory.tool')),
            ],
        ),
    ]