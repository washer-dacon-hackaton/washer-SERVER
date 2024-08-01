# Generated by Django 5.0.7 on 2024-08-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hexagonal',
            name='emo1',
        ),
        migrations.RemoveField(
            model_name='hexagonal',
            name='emo2',
        ),
        migrations.RemoveField(
            model_name='hexagonal',
            name='emo3',
        ),
        migrations.RemoveField(
            model_name='hexagonal',
            name='emo4',
        ),
        migrations.RemoveField(
            model_name='hexagonal',
            name='emo5',
        ),
        migrations.RemoveField(
            model_name='hexagonal',
            name='emo6',
        ),
        migrations.AddField(
            model_name='hexagonal',
            name='anger',
            field=models.IntegerField(default=0, verbose_name='분노'),
        ),
        migrations.AddField(
            model_name='hexagonal',
            name='fear',
            field=models.IntegerField(default=0, verbose_name='공포'),
        ),
        migrations.AddField(
            model_name='hexagonal',
            name='gratitude',
            field=models.IntegerField(default=0, verbose_name='감사'),
        ),
        migrations.AddField(
            model_name='hexagonal',
            name='joy',
            field=models.IntegerField(default=0, verbose_name='기쁨'),
        ),
        migrations.AddField(
            model_name='hexagonal',
            name='love',
            field=models.IntegerField(default=0, verbose_name='사랑'),
        ),
        migrations.AddField(
            model_name='hexagonal',
            name='sadness',
            field=models.IntegerField(default=0, verbose_name='슬픔'),
        ),
    ]
