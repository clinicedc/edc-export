import uuid

from django.apps import apps as django_apps
from django.test import TestCase
from edc_appointment.models import Appointment
from edc_utils import get_utcnow

from edc_export.model_exporter import PlanExporter
from edc_export.models import Plan

from ..helper import Helper
from ..models import Crf, ListModel, SubjectVisit

app_config = django_apps.get_app_config("edc_export")


class TestPlan(TestCase):

    path = app_config.export_folder

    def setUp(self):
        self.helper = Helper()
        for appointment in Appointment.objects.all().order_by("visit_code"):
            SubjectVisit.objects.create(
                appointment=appointment,
                subject_identifier=appointment.subject_identifier,
                report_datetime=get_utcnow(),
            )
        self.subject_visit = SubjectVisit.objects.all()[0]
        self.thing_one = ListModel.objects.create(display_name="thing_one", name="thing_one")
        self.thing_two = ListModel.objects.create(display_name="thing_two", name="thing_two")
        self.crf = Crf.objects.create(
            subject_visit=self.subject_visit,
            char1="char",
            date1=get_utcnow(),
            int1=1,
            uuid1=uuid.uuid4(),
        )

    def test_plan(self):
        plan_name = "test_plan"
        Plan.objects.create(name=plan_name, model="edc_export.crf")
        PlanExporter(plan_name=plan_name)
