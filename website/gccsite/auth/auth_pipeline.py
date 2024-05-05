from django.conf import settings
from django.contrib.auth.models import Group


def map_groups(response, user, *_args, **_kwargs):
    groups = response.get("groups")
    if not groups:
        return

    slugs = set(groups)
    django_groups = set(list(Group.objects.filter(name__in=slugs)))
    missing_groups = slugs - {g.name for g in django_groups}

    allowed_to_login = any(group in settings.ALLOWED_GROUPS for group in slugs)

    user.is_active = allowed_to_login
    user.save()
    if not allowed_to_login:
        return

    for slug in missing_groups:
        g = Group(name=slug)
        g.save()
        django_groups.add(g)

    for group in Group.objects.filter(name__in=slugs):
        user.groups.add(group)

    for group in {g for g in user.groups.all()} - django_groups:
        user.groups.remove(group)

    user.is_staff = any(group in settings.STAFF_GROUPS for group in slugs)
    user.is_superuser = bool(
        slugs.intersection(set(settings.SUPERUSER_GROUPS))
    )

    user.save()
