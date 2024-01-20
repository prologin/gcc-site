from functools import wraps

import magic
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


def validate_is_pdf(file):
    valid_mime_types = ["application/pdf"]

    file_mime_type = magic.from_buffer(file.read(1024), mime=True)

    if file_mime_type not in valid_mime_types:
        raise ValidationError("Unsupported file type.")


@deconstructible
class FileSizeValidator:
    """
    Validator that checks the size of the given file
    """

    def __init__(self, max_size_mb=10) -> None:
        self.max_size = max_size_mb * (1 << 10)

    def __call__(self, file):
        if file.size > self.max_size:
            raise ValidationError(
                _("File size is too big (Max is %sMB)") % self.max_size
            )


def validate_file_max_size(max_size_mb: int):
    """
    Do not use, it is here for migration referencing only
    """

    @wraps(validate_file_max_size)
    def validator(file):
        if file.size > max_size_mb * (1 << 10):
            raise ValidationError(
                _("File size is too big (Max is %sMB)") % max_size_mb
            )

    return validator
