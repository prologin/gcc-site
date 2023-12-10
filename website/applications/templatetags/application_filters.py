from django import template

from applications.models import Application, ApplicationStatus

register = template.Library()


@register.filter
def get_available_transitions(application: Application, user):
    return application.get_available_transitions_names(user)


@register.filter
def status_label(application: Application):
    return ApplicationStatus(application.status).label
