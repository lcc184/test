# Generated by Django 2.2.6 on 2020-07-29 11:44

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goodtext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(0, '下架'), (1, '上架')], verbose_name='商品的状态')),
                ('detail', tinymce.models.HTMLField(verbose_name='商品的详情')),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': '商品SKU',
                'verbose_name_plural': '商品SKU',
                'db_table': 'df_goods_text',
            },
        ),
    ]