function getPharmacies(){
    // specify the path of the CSV file
    const selectedCity = document.getElementById("VilleSelect1").value;
    const QuartierList = document.getElementById("Quartier1");
    const path = "F:/Projet_Se7ati/se7ati_project/se7ati_app/static/Quartier_ville.csv";
    alert("Hello");
    
    
       fetch('/se7ati/pharmacy/file')
          .then(response => response.text())
          .then(text => {
            const lines = text.split('\n');
            const secondColumn = [];
            lines.forEach(line => {
              const columns = line.split(',');
              if( (columns.length > 1) && (columns[0] == selectedCity)) {
                  secondColumn.push(columns[1]);
                  const option = document.createElement('option');
                         option.value = columns[1];
                         option.textContent = columns[1];
                         QuartierList.appendChild(option);
              }
            });
            console.log(secondColumn);
          })
          .catch(error => {
             console.error('Error:', error);
             document.write('Error reading file.');
          });
    
    
    }