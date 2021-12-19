
function setblogdata(array) {
    html_content = '';
    for (let index = 0; index < 4; index++) {        
        const element = array[index];                             
        const words = element.description.replace(/<[^>]+>/g, '').split(' ');
        let description = '';
        for (let i = 0; i < 30; i++) {
            if (words[i].length > 0) {
                description += words[i] + ' ';
            }
        }    

        html_content += `        
        <div class="col-md-6">
            <div class="card-body">
            <!-- Title -->
            <h4 class="card-title">${element.title}</h4>
            <hr>
            <!-- Text -->
            <p class="card-text">${description}</p>
            <a class="link-text" href="${element.link}">
            <h6>Read more <i class='bx bxs-right-arrow-alt bx-fade-left' style='font-size:24px;' ></i></h6>
            </a>
            </div>            
        </div>
        `;    
    }      
    document.getElementById("blogs").innerHTML = html_content;
}


fetch('https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fblog.saranmahadev.tech%2Frss.xml').then(resp => resp.json()).then(
    data => {
        setblogdata(data.items);
    }
);