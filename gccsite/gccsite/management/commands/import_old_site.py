# Copyright (C) <2019> Association Prologin <association@prologin.org>
# SPDX-License-Identifier: GPL-3.0+

import argparse
import datetime
import json
import sys
import pytz
from django.core.management import BaseCommand

import gcc.models as models
from users.models import GCCUser


class Command(BaseCommand):
    help = "Import datas from the old website"

    def __init__(self, *args, **kwargs):
        self.logs = dict()
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument('import_file', type=argparse.FileType('r'))
        parser.add_argument('imported_users_file', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        try:
            data = json.loads(options['import_file'].read())
            imported_users = json.loads(options['imported_users_file'].read())
        except Exception as exception:
            print('Please specify valid json files ({})'.format(exception))
            sys.exit(1)

        try:
            self.update_database(data, imported_users)
        finally:
            with open('changes.log', 'w') as file:
                file.write(json.dumps(self.logs))

    def update_database(self, data, imported_users):
        #                          _      _   _
        #  _ __   _____      _____| | ___| |_| |_ ___ _ __
        # | '_ \ / _ \ \ /\ / / __| |/ _ \ __| __/ _ \ '__|
        # | | | |  __/\ V  V /\__ \ |  __/ |_| ||  __/ |
        # |_| |_|\___| \_/\_/ |___/_|\___|\__|\__\___|_|
        #
        print('Import Mailing List...')

        for subscriber_data in data['subscribers']:
            fields = subscriber_data['fields']

            if not models.SubscriberEmail.objects.filter(email=fields['mail']):
                models.SubscriberEmail(
                    email=fields['mail'], date=fields['created']
                ).save()
        #
        #   _   _ ___  ___ _ __ ___
        #  | | | / __|/ _ \ '__/ __|
        #  | |_| \__ \  __/ |  \__ \
        #   \__,_|___/\___|_|  |___/
        #
        print('Import Users...')

        users = {}

        for user_data in data['users']:
            fields = user_data['fields']

            if str(user_data['pk']) not in imported_users['users']['new_pk']:
                continue

            new_pk = imported_users['users']['new_pk'][str(user_data['pk'])]
            user, created = GCCUser.objects.get_or_create(
                pk=new_pk, defaults={'username': fields['username']}
            )

            shared_field = (
                'last_login',
                'first_name',
                'last_name',
                'is_active',
                'date_joined',
            )

            for field in shared_field:
                setattr(user, field, fields[field])

            for profile in data['applications']['profile']:
                if profile['fields']['user'] == user_data['pk']:
                    profile['fields']['postal_code'] = profile['fields'][
                        'zipcode'
                    ]
                    shared_fields = (
                        'address',
                        'phone',
                        'birthday',
                        'country',
                        'city',
                        'postal_code',
                    )

                    for f in shared_fields:
                        if f == 'phone' and profile['fields'][f] is not None:
                            profile['fields'][f] = profile['fields'][f][:16]

                        if profile['fields'][f] is not None:
                            setattr(user, f, profile['fields'][f])

            user.save()
            users[user_data['pk']] = user

        #       _                            __
        #   ___(_) __ _ _ __  _   _ _ __    / _| ___  _ __ _ __ ___
        #  / __| |/ _` | '_ \| | | | '_ \  | |_ / _ \| '__| '_ ` _ \
        #  \__ \ | (_| | | | | |_| | |_) | |  _| (_) | |  | | | | | |
        #  |___/_|\__, |_| |_|\__,_| .__/  |_|  \___/|_|  |_| |_| |_|
        #         |___/            |_|
        print('Create signup form...')

        questions = [
            models.Question(
                question='Sais-tu ce qu\'est un tableau en informatique ?',
                response_type=models.AnswerTypes.multichoice.value,
                meta={
                    'choices': {
                        '0': 'pas du tout',
                        '1': 'un peu',
                        '2': 'bien',
                        '3': 'tr??s bien',
                    }
                },
            ),
            models.Question(
                question='Sais-tu ce qu\'est une fonction r??cursive ?',
                response_type=models.AnswerTypes.multichoice.value,
                meta={
                    'choices': {
                        '0': 'pas du tout',
                        '1': 'un peu',
                        '2': 'bien',
                        '3': 'tr??s bien',
                    }
                },
            ),
            models.Question(
                question='Depuis quand programmes-tu ?',
                response_type=models.AnswerTypes.multichoice.value,
                meta={
                    'choices': {
                        '0': 'quelques jours',
                        '1': 'quelques semaines',
                        '2': 'quelques mois',
                        '3': 'un an ou plus',
                        '5': 'pas encore commenc??',
                    }
                },
            ),
            models.Question(
                question='Est-ce que tu programmes en moyenne...',
                response_type=models.AnswerTypes.multichoice.value,
                meta={
                    'choices': {
                        '0': 'une fois par an',
                        '1': 'une fois par mois',
                        '2': 'une fois par semaine',
                        '3': 'tous les jours',
                    }
                },
            ),
            models.Question(
                question='Quel(s) outil(s) ou langage(s) de programmation as-tu d??j?? essay??(s) ?',
                response_type=models.AnswerTypes.string.value,
            ),
            models.Question(
                question='Quel est ton parcours scolaire et as-tu une id??e de ce que tu veux faire plus tard ?',
                response_type=models.AnswerTypes.text.value,
            ),
            models.Question(
                question='Qu\'esp??res-tu apprendre pendant ce stage ?',
                response_type=models.AnswerTypes.text.value,
            ),
            models.Question(
                question='Aimerais-tu r??aliser un projet en rapport avec l\'informatique ? Si oui, lequel ?',
                response_type=models.AnswerTypes.text.value,
            ),
            models.Question(
                question='Quel est ton identifiant sur France-ioi ?',
                response_type=models.AnswerTypes.string.value,
            ),
        ]

        questions_extfields = (
            'knows_array',
            'knows_recurs',
            'experience',
            'frequency',
            'languages',
            'studies',
            'expectations',
            'projects',
            'fioi_login',
        )

        form_name = 'OldWebsiteForm'
        form, created = models.Form.objects.get_or_create(name=form_name)
        form.save()

        for i, question in enumerate(questions):
            try:
                questions[i] = models.Question.objects.get(
                    question=question.question
                )
            except models.Question.DoesNotExist:
                questions[i].save()

            form.question_list.add(questions[i])

        #            _ _ _   _
        #    ___  __| (_) |_(_) ___  _ __  ___
        #   / _ \/ _` | | __| |/ _ \| '_ \/ __|
        #  |  __/ (_| | | |_| | (_) | | | \__ \
        #   \___|\__,_|_|\__|_|\___/|_| |_|___/
        #
        print('Import Editions...')

        editions = {}

        for edition_data in data['applications']['editions']:
            fields = edition_data['fields']

            edition, created = models.Edition.objects.get_or_create(
                year=fields['year'], defaults={'signup_form': form}
            )

            editions[edition_data['pk']] = edition

        #
        #    __ _ _ __  _____      _____ _ __ ___
        #   / _` | '_ \/ __\ \ /\ / / _ \ '__/ __|
        #  | (_| | | | \__ \\ V  V /  __/ |  \__ \
        #   \__,_|_| |_|___/ \_/\_/ \___|_|  |___/
        #
        print('Import Answers...')

        for application_data in data['applications']['application']:
            fields = application_data['fields']

            if fields['user'] not in users:
                continue

            user = users[fields['user']]
            edition = editions[fields['edition']]
            applicant = models.Applicant.for_user_and_edition(user, edition)

            for i, extfield in enumerate(questions_extfields):
                response = str(fields[extfield])

                if response not in [None, '']:
                    # for multichoices, check if the value is valid
                    if (
                        questions[i].response_type
                        == models.AnswerTypes.multichoice.value
                        and response not in questions[i].meta['choices']
                    ):
                        continue

                    question_exists = models.Answer.objects.filter(
                        applicant=applicant, question=questions[i]
                    ).exists()

                    if not question_exists:
                        models.Answer(
                            applicant=applicant,
                            question=questions[i],
                            response=response,
                        ).save()

        #                  _
        #    ___ ___ _ __ | |_ ___ _ __ ___
        #   / __/ _ \ '_ \| __/ _ \ '__/ __|
        #  | (_|  __/ | | | ||  __/ |  \__ \
        #   \___\___|_| |_|\__\___|_|  |___/
        #
        print('Import Centers...')

        centers = {}

        for center_data in data['applications']['centers']:
            fields = center_data['fields']

            center, created = models.Center.objects.get_or_create(
                name=fields['name'],
                defaults={'type': models.Center.Type.center.value},
            )

            if created:
                shared_fields = (
                    'is_active',
                    'comments',
                    'address',
                    'postal_code',
                    'city',
                    'country',
                )

                for f in shared_fields:
                    setattr(center, f, fields[f])

            center.save()

            centers[center_data['pk']] = center

        #                        _
        #    _____   _____ _ __ | |_ ___
        #   / _ \ \ / / _ \ '_ \| __/ __|
        #  |  __/\ V /  __/ | | | |_\__ \
        #   \___| \_/ \___|_| |_|\__|___/
        #
        print('Import Events...')

        events = {}

        for event_data in data['applications']['events']:
            fields = event_data['fields']

            event, created = models.Event.objects.get_or_create(
                center=centers[fields['center']],
                edition=editions[fields['edition']],
                event_start=fields['date_begin'],
                event_end=fields['date_end'],
                signup_start=fields['date_begin'],
                signup_end=fields['date_end'],
            )
            event.save()

            events[event_data['pk']] = event

        #            _     _
        #  __      _(_)___| |__   ___  ___
        #  \ \ /\ / / / __| '_ \ / _ \/ __|
        #   \ V  V /| \__ \ | | |  __/\__ \
        #    \_/\_/ |_|___/_| |_|\___||___/
        #
        print('Import Wishes...')

        for application_data in data['applications']['application']:
            fields = application_data['fields']

            if fields['user'] not in users:
                continue

            user = users[fields['user']]
            edition = editions[fields['edition']]
            applicant = models.Applicant.for_user_and_edition(user, edition)

            field_choices = (
                fields['event_choice1'],
                fields['event_choice2'],
                fields['event_choice3'],
            )

            for order, choice in enumerate(field_choices):
                if choice is None:
                    continue

                order += 1
                event = events[choice]

                wish_exists = bool(
                    models.EventWish.objects.filter(
                        applicant=applicant, event=event
                    )
                )

                if not wish_exists:
                    models.EventWish(
                        applicant=applicant, event=event, order=order
                    ).save()

            if fields['accepted']:
                event_wish = models.EventWish.objects.filter(
                    applicant=applicant
                ).first()

                if event_wish is None:
                    center = models.Center.objects.get(name='EPITA Paris')
                    start = datetime.datetime(
                        int(edition.year),
                        1,
                        1,
                        0,
                        0,
                        tzinfo=pytz.timezone('Europe/Paris'),
                    )
                    end = datetime.datetime(
                        int(edition.year),
                        12,
                        31,
                        23,
                        59,
                        tzinfo=pytz.timezone('Europe/Paris'),
                    )

                    event, created = models.Event.objects.get_or_create(
                        center=center,
                        edition=edition,
                        defaults={
                            'event_start': start,
                            'event_end': end,
                            'signup_start': start,
                            'signup_end': end,
                        },
                    )
                    event.save()

                    event_wish = models.EventWish(
                        applicant=applicant, event=event, order=1
                    )
                    event_wish.save()

                applicant.assignation_event.add(event_wish.event)

        #       _        _
        #   ___| |_ __ _| |_ _   _ ___
        #  / __| __/ _` | __| | | / __|
        #  \__ \ || (_| | |_| |_| \__ \
        #  |___/\__\__,_|\__|\__,_|___/
        #
        print('Update Applications Status...')

        for application_data in data['applications']['application']:
            fields = application_data['fields']

            if fields['user'] not in users:
                continue

            user = users[fields['user']]
            edition = editions[fields['edition']]
            applicant = models.Applicant.for_user_and_edition(user, edition)

            if fields['accepted']:
                if fields['confirmed']:
                    applicant.status = (
                        models.ApplicantStatusTypes.confirmed.value
                    )
                else:
                    applicant.status = (
                        models.ApplicantStatusTypes.accepted.value
                    )
            elif fields['accepted'] is False:
                applicant.status = models.ApplicantStatusTypes.rejected.value

            applicant.save()
