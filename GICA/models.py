from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.utils import timezone
from datetime import datetime
from datetime import date
from django.db.models.enums import TextChoices
from django.urls import reverse
from django_composite_auto_field.fields import CompositeAutoField
import random, string
from django.db.models import Field
from django.core.exceptions import ValidationError
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import storages
from django.contrib.auth.models import User
from dynamic_filenames import FilePattern
upload_to_pattern = FilePattern(
    filename_pattern='{app_label:.25}/{model_name:.30}/{uuid:base32}{ext}'
)

# Create your models here.
class New(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    #class Meta:  
        #db_table = "New"

    def __str__(self):
        return self.title


fs = FileSystemStorage(location="media/")


def file_generate_upload_path(instance, filename):
    # Both filename and instance.file_name should have the same values
    return f"files/{instance.file_name}"
def file_upload_path(instance, filename):
    return f'{instance.id}/{filename}'
class IncrementalIDField(Field):
    def __init__(self, prefix='GAIA-', *args, **kwargs):
        self.prefix = prefix
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value is None:
            return None
        return f"{self.prefix}{value}"

    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        return value

    def validate(self, value, model_instance):
        if not isinstance(value, str):
            raise ValidationError(f'The value of the field "{self.name}" must be a string.')
        if len(value) < len(self.prefix):
            raise ValidationError(f'The value of the field "{self.name}" must be at least {len(self.prefix)} characters long.')
        if value[:len(self.prefix)] != self.prefix:
            raise ValidationError(f'The value of the field "{self.name}" must start with the prefix "{self.prefix}".')

# Create your models here.
def return_date_time():
    return timezone.now() + timezone.timedelta(days=10)

class Member(models.Model):
    MID = CompositeAutoField(editable=False, prefix='GAIA', use_year=False, zeros=5)
    Fullname = models.CharField(max_length=100, blank=True, null=False, default=" ")
    Phone_number = PhoneNumberField()
    Country = CountryField(blank_label="(select country)")
    Email = models.EmailField(blank=True, default=" ")
    Joined_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.MID.__str__()

    class Meta:
        db_table = "member"

class Payment(models.Model):
    DMID = models.ForeignKey(Member, on_delete=models.CASCADE, default=" ")
    Fullname = models.CharField(max_length=100, blank=True, null=False, default=" ")
    Year = models.IntegerField(default=datetime.now().year)
    January = models.IntegerField(null=True, blank=True, default=0)
    February = models.IntegerField(null=True, blank=True, default=0)
    March = models.IntegerField(null=True, blank=True, default=0)
    April = models.IntegerField(null=True, blank=True, default=0)
    May = models.IntegerField(null=True, blank=True, default=0)
    June = models.IntegerField(null=True, blank=True, default=0)
    July = models.IntegerField(null=True, blank=True, default=0)
    August = models.IntegerField(null=True, blank=True, default=0)
    September = models.IntegerField(null=True, blank=True, default=0)
    October = models.IntegerField(null=True, blank=True, default=0)
    November = models.IntegerField(null=True, blank=True, default=0)
    December = models.IntegerField(null=True, blank=True, default=0)
    Total = models.IntegerField(null=True, blank=True, default=0)

    def save(self, *args, **kwargs):
        self.Total = self.January + self.February + self.March + self.April + self.May + self.June + self.July + self.August + self.September + self.October + self.November + self.December
        super(Payment, self).save(*args, **kwargs)

    def __str__(self):
        return self.DMID.__str__()

    class Meta:
        db_table = "payment"


def select_storage():
        return storages["mystorage"]
class Donor(models.Model):
    def file_path(self, filename):
        return f'donfile/{self.Donation_attachment}'

    DCHOICE = (
        ("Iftaresaim", "Iftaresaim"),
        ("Ouduhuya", "Ouduhuya"),
        ("Mesjid", "Mesjid"),
        ("Quran", "Quran"),
        ("ZekatelFiter", "ZekatelFiter"),
        ("Mesakin", "Mesakin"),
        ("Education", "Education"),)
    Fullname = models.CharField(max_length=100, blank=True, null=False, default=" ")
    Amount = models.IntegerField()
    Donation_type = models.CharField(max_length=20,
                                     choices=DCHOICE,
                                     default='Quran'
                                     )
    Phone_number = PhoneNumberField()
    Country = CountryField(blank_label="(select country)")
    Donation_attachment = models.FileField(upload_to=upload_to_pattern, default="")
    #Donation_attachment = models.FileField()
    upload_finished_at = models.DateTimeField(default=timezone.now)

    @property
    def is_valid(self):
        """
        We consider a file "valid" if the the datetime flag has value.
        """
        return bool(self.upload_finished_at)

    @property
    def url(self):
        if settings.FILE_UPLOAD_STORAGE == "s3":
            return self.file.url

        return f"{settings.APP_DOMAIN}{self.file.url}"
    class Meta:
        db_table = "donor"

    def __str__(self):
        return self.Fullname.__str__()

class DonorNiya(models.Model):
    DCHOICE = (
        ("Iftaresaim", "Iftaresaim"),
        ("Ouduhuya", "Ouduhuya"),
        ("Mesjid", "Mesjid"),
        ("Quran", "Quran"),
        ("ZekatelFiter", "ZekatelFiter"),
        ("Mesakin", "Mesakin"),
        ("Education", "Education"),)
    Fullname = models.CharField(max_length=100, blank=True, null=False, default=" ")
    Amount = models.IntegerField()
    Donation_type = models.CharField(max_length=20,
                                     choices=DCHOICE,
                                     default='Quran'
                                     )
    Phone_number = PhoneNumberField()
    Country = CountryField(blank_label="(select country)")

    class Meta:
        db_table = "donorniya"

    def __str__(self):
        return self.Fullname.__str__()

class Project(models.Model):
    PID = models.CharField(primary_key='true', max_length=50, unique='true', default=" ")
    Pname = models.CharField(max_length=100, blank=True, null=False, default=" ")
    Location = models.CharField(blank=True, max_length=100, default=" ")
    Allocated_Budget = models.IntegerField(null=True, blank=True, default=0)
    Start_date = models.DateTimeField(default=timezone.now)
    End_date = models.DateTimeField(default=timezone.now)
    PFile = models.FileField(upload_to='projectfile/')

    class Meta:
        db_table = "projects"

    def __str__(self):
        return self.Pname.__str__()


class IslamicEvent(models.Model):
    """
    A model for representing events organized by an Islamic Association.
    """
    Name = models.CharField(max_length=255)
    Description = models.TextField(blank=True)
    Start_date = models.DateTimeField()
    End_date = models.DateTimeField()
    Location = models.CharField(max_length=255)
    Organizer = models.CharField(max_length=255)
    File = models.FileField(upload_to='eventfile/')
    Uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "islamicevents"

    def __str__(self):
        return self.Name.__str__()
