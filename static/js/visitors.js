// Add a Visitor Count

document.addEventListener('DOMContentLoaded', function() {
    fetch('https://api.db-ip.com/v2/free/self').then(function(response) {
        return response.json();
    }).then(function(json) {       
        var visitor = {
            ip: json.ipAddress,
            country: json.countryName,
            city: json.city,
        };
        fetch('/visitors/add', {
            method: 'POST',
            headers: {
                'X-CSRFToken': "{{ csrf_token() }}",
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(visitor)            
        }).then(function(response) {
            console.log(response);
        });       
    });
});

document.getElementById('countFetchLink').onclick = function() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/visitors/fetch', true);
    xhr.onload = function() {
        jsonData = JSON.parse(this.responseText);
        document.getElementById('visitCount').innerHTML = jsonData.count;
    };
    xhr.send();
};
