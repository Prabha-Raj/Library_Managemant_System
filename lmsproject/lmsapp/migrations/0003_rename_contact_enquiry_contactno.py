# Generated by Django 4.2.4 on 2023-09-07 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0002_enquiry_address_enquiry_enquirytext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='contact',
            new_name='contactno',
        ),
    ]