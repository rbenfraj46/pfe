from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    is_mail_verified = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), blank=False,
                              max_length=255,
                              null=True, unique=True)


class Devise(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    value = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)
    coefficient = models.FloatField(default=1)
    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)
    order_key = models.IntegerField(null=True)
    unit = models.IntegerField(default=1)

    def __str__(self):
        return self.name + " (" + str(self.value) + ")"

    class Meta:
        db_table = "currency"

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name=_("User"), null=True)
    devise = models.ForeignKey(Devise, on_delete=models.SET_NULL, verbose_name=_("Devise"), null=True)
    class Meta:
        db_table = "user_preference"


class State(models.Model):
    name = models.CharField(max_length=100)
    order_key = models.IntegerField(null=True)
    position = gis_models.PointField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("states")
        db_table = "state"


class Delegation(models.Model):
    name = models.CharField(max_length=100)
    order_key = models.IntegerField(null=True)
    position = gis_models.PointField()
    state = models.ForeignKey(State, on_delete=models.SET_NULL, verbose_name=_("State"), null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "delegation"


class City(models.Model):
    name = models.CharField(max_length=100)
    zipcode = models.IntegerField(null=True)
    order_key = models.IntegerField(null=True)
    position = gis_models.PointField()
    delegation = models.ForeignKey(Delegation, on_delete=models.SET_NULL, verbose_name=_("Delegation"), null=True)

    class Meta:
        verbose_name_plural = _("cities")
        db_table = "city"


class Agences(models.Model):
    agency_name = models.CharField(max_length=4096, verbose_name=_('Agency Name'))
    ceo_name = models.CharField(max_length=150, verbose_name=_('CEO Name'))
    tax_number = models.CharField(max_length=150, verbose_name=_('Tax registration Number'))
    adress_agency = models.CharField(max_length=4096, verbose_name=_('Adress'))
    governorate = models.CharField(max_length=200, verbose_name=_('Governorate'))
    city = models.CharField(max_length=200, verbose_name=_('City'))
    email = models.EmailField(_('email address'), blank=False, max_length=255, null=True, unique=True)
    phone_number = models.CharField(max_length=200, verbose_name=_('Phone'))
    agency_image = models.ImageField(upload_to='agency_images/', null=True, blank=True, verbose_name=_('Agency Image'))
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    is_mail_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name=_("Creator"), null=True)

    class Meta :
        db_table= 'agence'


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('User Name'))
    email = models.EmailField(_('email address'), blank=True, max_length=255, null=True)
    phone = models.CharField(max_length=255, verbose_name=_('User Phone'), null=True, blank=True)
    subject = models.CharField(max_length=255, verbose_name=_('Subject'), null=True, blank=True)
    message = models.CharField(max_length=255, verbose_name=_('Message'), null=True, blank=True)

    is_read = models.BooleanField(default=False, verbose_name=_('Is Read'))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Last Updated"))

    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name=_("User"), null=True)

    class Meta :
        db_table= 'contact'
