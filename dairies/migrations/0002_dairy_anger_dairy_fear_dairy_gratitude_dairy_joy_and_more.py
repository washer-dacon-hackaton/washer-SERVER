# Generated by Django 5.0.7 on 2024-08-01 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dairy',
            name='anger',
            field=models.IntegerField(default=0, verbose_name='분노빈도'),
        ),
        migrations.AddField(
            model_name='dairy',
            name='fear',
            field=models.IntegerField(default=0, verbose_name='공포빈도'),
        ),
        migrations.AddField(
            model_name='dairy',
            name='gratitude',
            field=models.IntegerField(default=0, verbose_name='감사빈도'),
        ),
        migrations.AddField(
            model_name='dairy',
            name='joy',
            field=models.IntegerField(default=0, verbose_name='기쁨빈도'),
        ),
        migrations.AddField(
            model_name='dairy',
            name='love',
            field=models.IntegerField(default=0, verbose_name='사랑빈도'),
        ),
        migrations.AddField(
            model_name='dairy',
            name='sadness',
            field=models.IntegerField(default=0, verbose_name='슬픔빈도'),
        ),
        migrations.AlterField(
            model_name='dairy',
            name='dairy_feedback',
            field=models.TextField(default=0, verbose_name='왓셩 피드백'),
        ),
    ]
