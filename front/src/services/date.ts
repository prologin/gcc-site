export const formatDate = function (dateUtc: string) {
  const date: Date = new Date(dateUtc)
  const day: string = [
    'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'
  ][date.getDay()]
  const month: string = [
    'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
    'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'
  ][date.getMonth()]
  return day + ' ' + date.getDate() + ' ' + month
}
