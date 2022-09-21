export default class ScheduleAPIService {
  getWeekEndSchedule () {
    return [
      {
        day: 'Samedi',
        activities: [
          {
            title: 'Accueil et petit déjeuner',
            start: 9,
            duration: 1
          },
          {
            title: 'Introduction du stage',
            start: 10,
            duration: 2
          },
          {
            title: 'Repas',
            start: 12,
            duration: 2
          },
          {
            title: 'Projet Micro:bit',
            start: 14,
            duration: 3
          },
          {
            title: 'Gouter et jeux du soir',
            start: 17,
            duration: 1
          }
        ]
      },
      {
        day: 'Dimanche',
        activities: [
          {
            title: 'Accueil et petit déjeuner',
            start: 9,
            duration: 1
          },
          {
            title: 'Projet Micro:bit',
            start: 10,
            duration: 1
          },
          {
            title: 'Conférence',
            start: 11,
            duration: 1
          },
          {
            title: 'Repas',
            start: 12,
            duration: 2
          },
          {
            title: 'Conférence',
            start: 14,
            duration: 1
          },
          {
            title: 'Projet Micro:bit',
            start: 15,
            duration: 2
          },
          {
            title: 'Gouter et jeux du soir',
            start: 17,
            duration: 1
          }
        ]
      }
    ]
  }

  getWeekSchedule () {
    return [
      {
        day: 'Lundi',
        activities: [
          {
            title: 'Accueil et petit déjeuner',
            start: 9,
            duration: 1
          },
          {
            title: 'Introduction et présentation',
            start: 10,
            duration: 2
          },
          {
            title: 'Prise en main',
            start: 12,
            duration: 1
          },
          {
            title: 'Repas',
            start: 13,
            duration: 1
          },
          {
            title: 'Initiation au Python',
            start: 14,
            duration: 4
          }
        ]
      },
      {
        day: 'Mardi',
        activities: [
          {
            title: 'Accueil et petit déjeuner',
            start: 9,
            duration: 1
          },
          {
            title: 'Python',
            start: 10,
            duration: 2
          },
          {
            title: 'Repas',
            start: 12,
            duration: 2
          },
          {
            title: 'Python',
            start: 14,
            duration: 4
          }
        ]
      },
      {
        day: 'Mercredi',
        activities: [
          {
            title: 'Accueil et petit déjeuner',
            start: 9,
            duration: 1
          },
          {
            title: 'Découverte de la cryptologie',
            start: 10,
            duration: 2
          },
          {
            title: 'Repas',
            start: 12,
            duration: 1
          },
          {
            title: 'Activité surprise',
            start: 13,
            duration: 5
          }
        ]
      },
      {
        day: 'Jeudi',
        activities: [
          {
            title: 'Accueil et petit déjeuner',
            start: 9,
            duration: 1
          },
          {
            title: 'Découverte du web et du réseau',
            start: 10,
            duration: 2
          },
          {
            title: 'Repas',
            start: 12,
            duration: 2
          },
          {
            title: 'Projets',
            start: 14,
            duration: 4
          }
        ]
      },
      {
        day: 'Vendredi',
        activities: [
          {
            title: 'Accueil et petit déjeuner',
            start: 9,
            duration: 1
          },
          {
            title: 'Projets',
            start: 10,
            duration: 1
          },
          {
            title: 'Conférence',
            start: 11,
            duration: 1
          },
          {
            title: 'Repas',
            start: 12,
            duration: 2
          },
          {
            title: 'Projets',
            start: 14,
            duration: 4
          }
        ]
      },
      {
        day: 'Samedi',
        activities: [
          {
            title: 'Accueil et petit déjeuner',
            start: 9,
            duration: 1
          },
          {
            title: 'Conférence',
            start: 10,
            duration: 1
          },
          {
            title: 'Projets',
            start: 11,
            duration: 2
          },
          {
            title: 'Repas',
            start: 13,
            duration: 2
          }
        ]
      }
    ]
  }
}

export const scheduleAPI = new ScheduleAPIService()
