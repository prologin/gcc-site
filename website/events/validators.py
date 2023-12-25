import magic
from django.core.exceptions import ValidationError


def validate_is_pdf(file):
    valid_mime_types = ["application/pdf"]

    file_mime_type = magic.from_buffer(file.read(1024), mime=True)

    if file_mime_type not in valid_mime_types:
        raise ValidationError("Unsupported file type.")
