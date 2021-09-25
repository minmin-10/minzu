# Generated by Django 3.2.7 on 2021-09-25 14:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('place_id', models.IntegerField(primary_key=True, serialize=False)),
                ('place_name', models.TextField(max_length=50)),
                ('open_time', models.TimeField(blank=True, null=True)),
                ('close_time', models.TimeField(blank=True, null=True)),
                ('place_address', models.TextField(max_length=100)),
                ('wifi', models.BooleanField()),
                ('charge', models.BooleanField()),
                ('personal_space', models.BooleanField()),
                ('place_cost', models.PositiveIntegerField(blank=True, null=True)),
                ('place_category', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('reviews_id', models.IntegerField(primary_key=True, serialize=False)),
                ('review_comment', models.TextField(max_length=150)),
                ('review_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('review_place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.places')),
                ('review_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favo',
            fields=[
                ('favo_id', models.IntegerField(primary_key=True, serialize=False)),
                ('favo_place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.places')),
                ('favo_usr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Evals',
            fields=[
                ('evals_id', models.IntegerField(primary_key=True, serialize=False)),
                ('concentrations', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('silence', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('cost_pafo', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('conges', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.places')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
