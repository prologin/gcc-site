export default {
  dlInfo (applications, users) {
    let csv =
      "Nom de famille,Prénom, Nom représentant légal, Prénom représentant légal, Email représentant légal\n";
    for (let index = 0; index < this.applications.length; index++) {
      // Arreter d'harcode ca et mettre l'enum
      if (this.applications[index].status === 4) {
        csv +=
          this.applications[index].last_name +
          "," +
          this.applications[index].first_name;
        csv += '\n';
      }
    }
    const hiddenElement = document.createElement('a');
    hiddenElement.href = "data:text/csv;charset=utf-8," + encodeURI(csv);
    hiddenElement.target = "_blank";
    // provide the name for the CSV file to be downloaded
    hiddenElement.download = 'Infos_GCC!.csv';
    hiddenElement.click()
  },
};
