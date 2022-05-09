export const formatDate = function (dateUtc: string) {
  const date: Date = new Date(dateUtc)
  const daysNames: Array<string> = [
    'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'
  ]
  const monthsNames: Array<string> = [
    'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
    'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'
  ]
  return daysNames[date.getDay()] + ' ' + date.getDate() + ' ' + monthsNames[date.getMonth()]
}
