from io import BytesIO

import requests
from celery import shared_task
from django.apps import apps
from django.conf import settings
from django.core.files.base import ContentFile
from django.db import transaction
from pypdf import PdfWriter

from gccsite import tools


@shared_task(
    acks_late=True,
    autoretry_for=(Exception,),
    max_retries=5,
    retry_backoff=True,
)
def expense_report_generate_document(event_id):
    e = apps.get_model("events.event").objects.get(pk=event_id)

    data = {
        "place": e.center.name,
        "address": e.center.address,
        "city": e.center.address.city,
        "zip_code": e.center.address.zip_code,
        "event_start": e.start_date,
        "event_end": e.end_date,
        "event_start_time": "09:00",
        "event_end_time": "18:00",
    }

    print("here")

    response = requests.post(
        settings.DOCUMENTS_GENERATOR_DOCUMENTS_GCC_ENDPOINT,
        json=data,
        headers=tools.get_auth_headers_for_app("documents-generator"),
        timeout=60,
    )
    response.raise_for_status()


    merger = PdfWriter()
    merger.append(BytesIO(response.content))

    b = BytesIO()
    merger.write(b)
    b.seek(0)

    with transaction.atomic():
        e = apps.get_model("events.Events").objects.get(pk=event_id)
        e.document = ContentFile(b.read(), "docs_stage.pdf")
        e.save()
