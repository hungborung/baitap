# Generated by Django 3.1 on 2021-01-12 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('fullname', models.CharField(blank=True, max_length=255)),
                ('birthday', models.DateTimeField()),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date_joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last_login')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('id_superuser', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('profile_image', models.ImageField(blank=True, upload_to='static/user/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
