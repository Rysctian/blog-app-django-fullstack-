# Generated by Django 5.0 on 2024-01-26 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0005_alter_category_options_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_post',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='created',
        ),
    ]
