import django
django.setup()

import sys
import json
from datetime import datetime, date
from users.models import User
from profiles.models import Profile
from events.models import Center, Address, Event
from applications.models import Application, ApplicationStatus
from django.db import transaction


def get_users(users):
    for user in users:
        user_model = User(
            id = user['id'],
            email = user['email'],
            first_name = user['first_name'],
            last_name = user['last_name'],
            date_joined = datetime.fromisoformat(user['date_joined']),
            last_login = datetime.fromisoformat(user['last_login']),
            is_active = False
        )
        

        yield (user_model, Profile(
            id = user_model.id,
            user = user_model,
            first_name = user_model.first_name,
            last_name = user_model.last_name,
            birth_date = user['birthday'],
            email = user_model.email
        ))

def get_centers(centers):
    for center in centers:
        center_model = Center(
            id = center['id'],
            name = center['name'],
            private_notes="# This file is managed by Ansible, all changes will be lost"
        )
        address = Address(
            id = center['id'],
            center = center_model,
            street = center['address'],
            city = center['city'],
            zip_code = int(center['postal_code']) if center['postal_code'] else 0,
            country = center['country']
        )
        yield (center_model, address)

def get_events(events, centers):
    for event in events:
        start_date = datetime.fromisoformat(event['event_start'])
        yield Event(
            id = event['id'],
            name = '{} {}/{}'.format(centers[event['center_id']].name, start_date.month, start_date.year),
            center = centers[event['center_id']],
            year = start_date.year,
            start_date = start_date,
            end_date = datetime.fromisoformat(event['event_end']),
            signup_start_date = datetime.fromisoformat(event['signup_start']),
            signup_end_date = datetime.fromisoformat(event['signup_end']),
        )



def get_applicants(applicants, events, profiles):
    old2new = dict(
        Incomplete = ApplicationStatus.REJECTED.value,
        Pending = ApplicationStatus.PENDING.value,
        Rejected = ApplicationStatus.REJECTED.value,
        Selected = ApplicationStatus.ACCEPTED.value,
        Accepted = ApplicationStatus.ACCEPTED.value,
        Confirmed = ApplicationStatus.CONFIRMED.value,
    )

    for applicant in applicants:
        yield Application(
            id = applicant['id'],
            event = events[applicant['event_id']],
            profile = profiles[applicant['user_id']],
            status = old2new[applicant['status']]
        )


def main(file_path):
    with open(file_path) as f:
        data = json.load(f)
    
    users = data['users']

    with transaction.atomic():
        profiles_by_user_id = dict()
        for user, profile in get_users(users):
            user.save()
            profiles_by_user_id[profile.pk] = profile
            profile.save()
        centers_by_id = dict()
        for center, addr in get_centers(data['centers']):
            center.save()
            centers_by_id[center.pk] = center
            addr.save()
        events_by_id = dict()
        for event in get_events(data['events'], centers_by_id):
            events_by_id[event.pk] = event
            event.save()
        for application in get_applicants(data['applicants'], events_by_id, profiles_by_user_id):
            application.save()

main(sys.argv[1])
