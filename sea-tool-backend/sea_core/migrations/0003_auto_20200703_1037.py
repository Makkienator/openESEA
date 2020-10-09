# Generated by Django 2.2.7 on 2020-07-03 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sea_core', '0002_stakeholdergroup_survey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='parent_topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_topics', to='sea_core.Topic'),
        ),
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=128, null=True)),
                ('finished', models.BooleanField(default=False)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sea_core.Survey')),
                ('user_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_responses', to='sea_core.UserOrganization')),
            ],
            options={
                'verbose_name': 'survey_response',
                'verbose_name_plural': 'survey_responses',
            },
        ),
        migrations.CreateModel(
            name='QuestionResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direct_indicator_id', models.IntegerField()),
                ('value', models.TextField()),
                ('survey_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_responses', to='sea_core.SurveyResponse')),
            ],
            options={
                'verbose_name': 'question_response',
                'verbose_name_plural': 'question_responses',
            },
        ),
    ]
