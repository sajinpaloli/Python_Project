
function fetchDataAndUpdateTable() {
    fetch('http://127.0.0.1:5000/api/data')  
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#movieTable tbody');
            const tableHeader = document.querySelector('#movieTable thead tr');
            tableBody.innerHTML = '';  

            if (data.length > 0) {
                
                const headers = Object.keys(data[0]);
                tableHeader.innerHTML = ''; 

                headers.forEach(header => {
                    const th = document.createElement('th');
                    th.innerText = header.charAt(0).toUpperCase() + header.slice(1);  
                    tableHeader.appendChild(th);
                });

                
                data.forEach(movie => {
                    const row = document.createElement('tr');

                    headers.forEach(header => {
                        const td = document.createElement('td');
                        td.innerText = movie[header];  
                        row.appendChild(td);
                    });

                    tableBody.appendChild(row);
                });
            } else {
       
                tableBody.innerHTML = '<tr><td colspan="100%">No data available</td></tr>';
            }
        })
        .catch(error => console.error('Error fetching data:', error));
}


fetchDataAndUpdateTable();
