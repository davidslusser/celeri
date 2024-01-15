import os
import random
import string

from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from model_bakery import baker

__version__ = "0.0.1"


class Command(BaseCommand):
    """ """

    help = "Create some test data for the Celeri CaseMgr app"

    def __init__(self):
        self.opts = None
        self.app = None
        super(Command, self).__init__()

    def handle(self, *args, **kwargs):
        """command entry point"""
        print("Generating test data for the Celeri CaseMgr app")
        self.generate_courts()
        self.generate_defenders()
        self.generate_prosecutors()
        self.generate_judges()
        self.generate_bookings()
        self.generate_cases()
        self.generate_hearings()

    def generate_courts(self, qty=5):
        """generate some Court entries"""
        f = Faker()
        for _ in range(qty):
            baker.make(
                "casemgr.court",
                name=f.company(),
                address=f.address(),
                city=f.city(),
                state=f.state(),
                zip_code=f.zipcode(),
            )

    def generate_defenders(self, qty=5):
        """generate some Defendor entries"""
        f = Faker()
        for _ in range(qty):
            baker.make(
                "casemgr.defender",
                license="".join(random.choices(string.digits, k=8)),
                first_name=f.first_name(),
                last_name=f.last_name(),
                lawfirm=f.company(),
            )

    def generate_judges(self, qty=5):
        """generate some Judge entries"""
        f = Faker()
        for _ in range(qty):
            baker.make(
                "casemgr.judge",
                first_name=f.first_name(),
                last_name=f.last_name(),
            )

    def generate_prosecutors(self, qty=5):
        """generate some Defendor entries"""
        f = Faker()
        for _ in range(qty):
            baker.make(
                "casemgr.prosecutor",
                license="".join(random.choices(string.digits, k=8)),
                first_name=f.first_name(),
                last_name=f.last_name(),
                lawfirm=f.company(),
            )

    def generate_bookings(self, qty=10):
        """generate some Booking entries"""
        f = Faker()
        for _ in range(qty):
            obj = baker.make(
                "casemgr.booking",
                booking_id="".join(random.choices(string.digits, k=8)),
                first_name=f.first_name(),
                last_name=f.last_name(),
                dob=f.date_of_birth(),
                arresting_officer=f"{f.first_name()} {f.last_name()}",
                booking_officer=f"{f.first_name()} {f.last_name()}",
            )
            baker.make(
                "casemgr.defendant",
                first_name=obj.first_name,
                last_name=obj.last_name,
                dob=obj.dob,
                sex=obj.sex,
            )

    def generate_cases(self, qty=8):
        """generate some Case entries"""
        for _ in range(qty):
            booking_model = apps.get_model("casemgr.booking")
            defendant_model = apps.get_model("casemgr.defendant")
            defender_model = apps.get_model("casemgr.defender")
            prosecutor_model = apps.get_model("casemgr.prosecutor")

            case = baker.make(
                "casemgr.courtcase",
                case_number="".join(random.choices(string.digits, k=8)),
                title="a very interesting case title",
                booking=booking_model.objects.get_random_row(),
                defendant=defendant_model.objects.get_random_row(),
            )
            case.defenders.add(defender_model.objects.get_random_row())
            case.prosecutors.add(prosecutor_model.objects.get_random_row())

    def generate_hearings(self, qty=16):
        """generate some Hearing entries"""
        case_model = apps.get_model("casemgr.courtcase")
        judge_model = apps.get_model("casemgr.judge")
        f = Faker()
        for _ in range(qty):
            baker.make(
                "casemgr.hearing",
                court_case=case_model.objects.get_random_row(),
                judge=judge_model.objects.get_random_row(),
                hearing_date=f.date(),
            )
