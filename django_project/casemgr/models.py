from django.db import models
from django.urls import reverse
from auditlog.registry import auditlog
from handyhelpers.models import HandyHelperBaseModel


class ContactObject(models.Model):
    address = models.CharField(max_length=32, blank=True, null=True, help_text="")
    city = models.CharField(max_length=32, blank=True, null=True, help_text="")
    state = models.CharField(max_length=32, blank=True, null=True, help_text="")
    zip_code = models.CharField(max_length=10, blank=True, null=True, help_text="")
    email_address = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        abstract = True


class Human(HandyHelperBaseModel, ContactObject):
    title = models.CharField(max_length=16, blank=True, null=True, help_text="")
    first_name = models.CharField(max_length=32, blank=True, null=True, help_text="")
    middle_name = models.CharField(max_length=32, blank=True, null=True, help_text="")
    last_name = models.CharField(max_length=32, blank=True, null=True, help_text="")

    class Meta:
        abstract = True


class Arrestee(Human):
    SEX_CHOICES = [
        ("M", 'Male'),
        ("F", 'Female'),
    ]
    
    dob = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    class Meta:
        abstract = True


class Lawyer(Human, ContactObject):
    lawfirm = models.CharField(max_length=64, help_text="")
    license = models.CharField(max_length=32, unique=True, help_text="")
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        abstract = True


class Booking(Arrestee):
    booking_id = models.CharField(max_length=64, unique=True, help_text="")
    booking_officer = models.CharField(max_length=64, blank=True, null=True, help_text="")
    arresting_officer = models.CharField(max_length=64, blank=True, null=True, help_text="")
    details = models.TextField(blank=True, null=True, help_text="")

    def __str__(self) -> str:
        return self.booking_id    


class Court(HandyHelperBaseModel):
    COURT_TYPE_CHOICES = [
        ("civil", 'civil'),
        ("criminal", 'criminal'),
        ("family", 'family'),
        ("probate", 'probate'),
    ]
    name = models.CharField(max_length=32, help_text="")
    address = models.CharField(max_length=32, help_text="")
    city = models.CharField(max_length=32, help_text="")
    state = models.CharField(max_length=32, help_text="")
    zip_code = models.CharField(max_length=10, help_text="")
    court_type = models.CharField(max_length=16, choices=COURT_TYPE_CHOICES)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("casemgr:court", kwargs={"pk": self.pk})


class Case(HandyHelperBaseModel):
    case_number = models.CharField(max_length=64, blank=True, null=True, help_text="")
    title = models.CharField(max_length=64, blank=True, null=True, help_text="")
    booking = models.ForeignKey("Booking", on_delete=models.CASCADE)
    defendant = models.ForeignKey("Defendant", on_delete=models.CASCADE)
    defenders = models.ManyToManyField("Defender")
    prosecutors = models.ManyToManyField("Prosecutor") 
    files = models.ManyToManyField("CaseFile")

    def __str__(self) -> str:
        return self.case_number

    def get_absolute_url(self) -> str:
        return reverse("casemgr:case", kwargs={"pk": self.pk})
    

class CaseFile(HandyHelperBaseModel):
    title = models.CharField(max_length=32, blank=True, null=True, help_text="")
    url = models.URLField()

    def __str__(self) -> str:
        return self.title


class Defendant(Arrestee):

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Defender(Lawyer):

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Hearing(HandyHelperBaseModel):
    HEARING_TYPE_CHOICES = [
        ("civil", 'civil'),
        ("criminal", 'criminal'),
        ("family", 'family'),
        ("probate", 'probate'),
    ]
    
    case = models.ForeignKey("Case", on_delete=models.CASCADE)
    hearing_date = models.DateField()
    judge = models.ForeignKey("Judge", on_delete=models.CASCADE)
    hearing_type = models.CharField(max_length=32, choices=HEARING_TYPE_CHOICES)

    def __str__(self) -> str:
        return self.case_number

    def get_absolute_url(self) -> str:
        return reverse("casemgr:hearing", kwargs={"pk": self.pk})


class Judge(Human):
    """ """
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Prosecutor(Lawyer):

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


# register models with auditlog
auditlog.register(Booking)
auditlog.register(Case)
auditlog.register(Court)
auditlog.register(Hearing)
auditlog.register(Defendant)
auditlog.register(Defender)
auditlog.register(Judge)
auditlog.register(Prosecutor)
