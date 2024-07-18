# Generated by Django 2.1.7 on 2024-07-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_auto_20240718_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignsubjectteacher',
            name='semester',
            field=models.CharField(choices=[('Third', 'Third'), ('Fourth', 'Fourth'), ('Second', 'Second'), ('First', 'First')], max_length=40),
        ),
        migrations.AlterField(
            model_name='expert',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Dr.', 'Dr'), ('Ms.', 'Ms'), ('Mr.', 'Mr'), ('Prof Dr.', 'Prof Dr'), ('Mrs.', 'Mrs')], max_length=40),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_name',
            field=models.CharField(blank=True, choices=[('Third', 'Third'), ('Fourth', 'Fourth'), ('Second', 'Second'), ('First', 'First')], max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='aff_type',
            field=models.CharField(choices=[('Visiting', 'Visiting'), ('Permanent', 'Permanent'), ('Contract', 'Contract')], default='Permanent', max_length=30),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salutation',
            field=models.CharField(blank=True, choices=[('Dr.', 'Dr'), ('Ms.', 'Ms'), ('Mr.', 'Mr'), ('Prof Dr.', 'Prof Dr'), ('Mrs.', 'Mrs')], max_length=40),
        ),
    ]
