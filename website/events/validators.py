from functools import wraps

import magic
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_is_pdf(file):
    valid_mime_types = ["application/pdf"]

    file_mime_type = magic.from_buffer(file.read(1024), mime=True)

    if file_mime_type not in valid_mime_types:
        raise ValidationError("Unsupported file type.")


def validate_file_max_size(max_size_mb: int):
    @wraps(validate_file_max_size)
    def validator(file):
        if file.size > max_size_mb * (1 << 10):
            raise ValidationError(
                _("File size is too big (Max is %sMB)") % max_size_mb
            )

    return validator
