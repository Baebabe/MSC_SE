# Generated by Django 2.1.7 on 2024-07-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_auto_20240718_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignsubjectteacher',
            name='semester',
            field=models.CharField(choices=[('Second', 'Second'), ('Third', 'Third'), ('First', 'First'), ('Fourth', 'Fourth')], max_length=40),
        ),
        migrations.AlterField(
            model_name='expert',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Mrs.', 'Mrs'), ('Ms.', 'Ms'), ('Prof Dr.', 'Prof Dr'), ('Mr.', 'Mr'), ('Dr.', 'Dr')], max_length=40),
        ),
        migrations.AlterField(
            model_name='expert',
            name='upper_degree',
            field=models.CharField(choices=[('Bachelors', 'Bachelors'), ('Diploma', 'Diploma'), ('Masters', 'Masters'), ('PhD', 'PhD')], default='MSc', max_length=30),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_name',
            field=models.CharField(blank=True, choices=[('Second', 'Second'), ('Third', 'Third'), ('First', 'First'), ('Fourth', 'Fourth')], max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='aff_type',
            field=models.CharField(choices=[('Contract', 'Contract'), ('Visiting', 'Visiting'), ('Permanent', 'Permanent')], default='Permanent', max_length=30),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Mrs.', 'Mrs'), ('Ms.', 'Ms'), ('Prof Dr.', 'Prof Dr'), ('Mr.', 'Mr'), ('Dr.', 'Dr')], max_length=40),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='upper_degree',
            field=models.CharField(choices=[('Bachelors', 'Bachelors'), ('Diploma', 'Diploma'), ('Masters', 'Masters'), ('PhD', 'PhD')], default='MSc', max_length=30),
        ),
    ]