# Generated by Django 2.0.3 on 2018-05-05 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('payment_period', models.IntegerField()),
                ('payment_amount', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member')),
            ],
        ),
    ]