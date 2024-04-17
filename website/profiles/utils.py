from datetime import datetime

from django.core.exceptions import ImproperlyConfigured
from django.utils.crypto import constant_time_compare, salted_hmac
from django.utils.http import int_to_base36

from profiles.models import Profile

_SALT = "josef.marchand"


def _make_token_value(
    timestamp_b36: str, email: str, field: str, profile_id: int
) -> str:
    hash_value = f"{email}{profile_id}{timestamp_b36}"
    hash_str = salted_hmac(_SALT, hash_value).hexdigest()[::2]
    return f"{timestamp_b36}-{field}-{hash_str}"


def generate_profile_email_token(profile: Profile, field: str) -> str:
    """
    Arbitrary hash function for generating confirmation tokens.
    Inspired from django.contrib.auth.tokens.ResetPasswordGenerator
    """
    time_int = int((datetime.now() - datetime(2020, 1, 1)).total_seconds())
    ts_b36 = int_to_base36(time_int)

    email = getattr(profile, field)
    if email is None:
        raise ImproperlyConfigured(f"{profile.__class__} has no field {field}")

    return _make_token_value(ts_b36, email, field, profile.id)


def check_profile_email_token(profile: Profile, token: str) -> bool:
    (ts_b36, field, _) = token.split("-")
    email = getattr(profile, field)
    if email is None:
        return (False, None)

    recomputed_hash = _make_token_value(ts_b36, email, field, profile.id)

    return (constant_time_compare(recomputed_hash, token), field)
