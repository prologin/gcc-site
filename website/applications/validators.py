from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from profiles.models import Profile


@deconstructible
class ProfileConfirmedValidator:
    def __call__(self, profile_id):
        profile = Profile.objects.get(id=profile_id)
        if not profile.profile_confirmed:
            raise ValidationError(f"Profile {profile} is not confirmed")
