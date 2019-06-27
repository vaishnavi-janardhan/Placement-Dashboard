function createSelfPlacedTable() {
    var table = document.createElement('table');
    table.setAttribute('class', 'table');
    var tableHeaders = new Array();
    tableHeaders = ['First Name', 'Last Name', 'Batch ID']
    var arrValue = new Array();
    var tr = table.insertRow(-1);

    for (var h = 0; h < arrHead.length; h++) {
        var th = document.createElement('th');
        th.innerHTML = tableHeaders[h];
        tr.appendChild(th);
    }

    arrValue.push(['1', 'Green Field', 'Accountant']);
    for (var c = 0; c <= arrValue.length - 1; c++) {
        tr = table.insertRow(-1);
        for (var j = 0; j < arrHead.length; j++) {
            var td = document.createElement('td');
            td = tr.insertCell(-1);
            td.innerHTML = arrValue[c][j];
        }
    }
}   
