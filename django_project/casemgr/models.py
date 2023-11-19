from django.db import models
from django.urls import reverse
from auditlog.registry import auditlog
from handyhelpers.models import HandyHelperBaseModel


class Human(HandyHelperBaseModel):
    title = models.CharField(max_length=16, blank=True, null=True, help_text="")
    first_name = models.CharField(max_length=32, blank=True, null=True, help_text="")
    last_name = models.CharField(max_length=32, blank=True, null=True, help_text="")

    class Meta:
        abstract = True


class Booking(HandyHelperBaseModel):
    booking_id = models.CharField(max_length=64, unique=True, help_text="")
    # personal information
    # police report

    def __str__(self) -> str:
        return self.booking_id    


class Court(HandyHelperBaseModel):
    name = models.CharField(max_length=32, help_text="")
    address = models.CharField(max_length=32, help_text="")
    city = models.CharField(max_length=32, help_text="")
    state = models.CharField(max_length=32, help_text="")
    zip_code = models.CharField(max_length=10, help_text="")
    court_type = models.ForeignKey("CourtType", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("app1:court", kwargs={"pk": self.pk})


class CourtType(HandyHelperBaseModel):
    name = models.CharField(max_length=32, unique=True, help_text="")
    description = models.CharField(max_length=255, blank=True, null=True, help_text="")
    enabled = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
    

class Case(HandyHelperBaseModel):
    case_number = models.CharField(max_length=64, blank=True, null=True, help_text="")
    title = models.CharField(max_length=64, unique=True, help_text="")
    booking = models.ForeignKey("Booking", on_delete=models.CASCADE)
    defendant = models.ForeignKey("Defendant", on_delete=models.CASCADE)
    defenders = models.ManyToManyField("Defender")
    prosecutors = models.ManyToManyField("Prosecutor") 
    files = models.ManyToManyField("CaseFile")

    def __str__(self) -> str:
        return self.case_number

    def get_absolute_url(self) -> str:
        return reverse("app1:case", kwargs={"pk": self.pk})
    

class CaseFile(HandyHelperBaseModel):
    title = models.CharField(max_length=32, blank=True, null=True, help_text="")
    url = models.URLField()

    def __str__(self) -> str:
        return self.title


class Defendant(Human):
    dob = models.DateField()
    sex = models.CharField(max_length=8, help_text="")
    address = models.CharField(max_length=32, blank=True, null=True, help_text="")
    city = models.CharField(max_length=32, blank=True, null=True, help_text="")
    state = models.CharField(max_length=32, blank=True, null=True, help_text="")
    zip_code = models.CharField(max_length=10, blank=True, null=True, help_text="")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Defender(Human):
    address = models.CharField(max_length=32, blank=True, null=True, help_text="")
    city = models.CharField(max_length=32, blank=True, null=True, help_text="")
    state = models.CharField(max_length=32, blank=True, null=True, help_text="")
    zip_code = models.CharField(max_length=10, blank=True, null=True, help_text="")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Hearing(HandyHelperBaseModel):
    case = models.ForeignKey("Case", on_delete=models.CASCADE)
    hearing_date = models.DateField()
    judge = models.ForeignKey("Judge", on_delete=models.CASCADE)
    hearing_type = models.ForeignKey("HearingType", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.case_number

    def get_absolute_url(self) -> str:
        return reverse("app1:hearing", kwargs={"pk": self.pk})


class HearingType(models.Model):
    name = models.CharField(max_length=32, unique=True, help_text="")
    description = models.CharField(max_length=255, blank=True, null=True, help_text="")
    enabled = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Judge(Human):
    """ """
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Prosecutor(Human):
    address = models.CharField(max_length=32, blank=True, null=True, help_text="")
    city = models.CharField(max_length=32, blank=True, null=True, help_text="")
    state = models.CharField(max_length=32, blank=True, null=True, help_text="")
    zip_code = models.CharField(max_length=10, blank=True, null=True, help_text="")

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
