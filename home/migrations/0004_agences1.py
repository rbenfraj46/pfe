# Create this file as home/migrations/xxxx_add_agency_image.py (Django will auto-number)

from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_agences'),  # Make sure this matches your last migration
    ]

    operations = [
        migrations.AddField(
            model_name='agences',
            name='agency_image',
            field=models.ImageField(blank=True, null=True, upload_to='agencies/', verbose_name='Agency Image'),
        ),
    ]