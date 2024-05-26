console.log('hello bitch')
const videosBox = document.getElementById('videos-box')
console.log(videosBox)
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const loadBox = document.getElementById('loading-box')
let visible = 6

function cropText(text, maxlenght) {
    if (text.length > maxlenght) {
        return text.substring(0, maxlenght) + '...';
    } else {
        return text;
    }
}

function capitalizeWords(text) {
    return text.replace(/\b\w/g, function(letter) {
        return letter.toUpperCase();
    });
}

const handleGetData = () => {
    $.ajax({
        type: 'GET',
        url: `/videos-json/${visible}/`,
        success: function(response){
            max_size = response.max
            const data = response.data
            spinnerBox.classList.remove('not-visible')
            loadBtn.classList.add('not-visible')
            setTimeout(()=>{
                spinnerBox.classList.add('not-visible')
                loadBtn.classList.remove('not-visible')
                data.map(video=>{
                    console.log(video.id)
                    const dbDate = video.pub_date;
                    const dateObj = new Date(dbDate);
                    const year = dateObj.getFullYear();
                    const month = (dateObj.getMonth() + 1).toString().padStart(2, '0');
                    const day = dateObj.getDate().toString().padStart(2, '0');
                    const formattedDate = `${month}/${day}/${year}`;
                    const hours = dateObj.getHours().toString().padStart(2, '0');
                    const minutes = dateObj.getMinutes().toString().padStart(2, '0');
                    videosBox.innerHTML += `<div class="col-md-4 col-sm-6 mb-5" style="">
                                        <a target="_blank" class="text-decoration-none" href="${video.link}"><div class="card video-card shadow-lg bg-dark text-white" style="">
                                          <img class="card-img-top" src="media/${video.image}" alt="Here is video preview" style="object-fit: cover;aspect-ratio: 16/9;">
                                          <div class="card-body">
                                            <h5 class="card-title">${cropText(video.title, 22).toUpperCase()}</h5><hr style="margin: 0;">
                                            <small class="card-text text-secondary">${formattedDate} ${hours}:${minutes}</small>
                                            
                                          </div>
                                        </div></a>
                                        </div>`
                })
                if(max_size){
                    console.log('done')
                    loadBox.innerHTML = ""
                }
            }, 500)
        },
        error: function(error){
            console.log(error)
        }
    })
}

handleGetData()

loadBtn.addEventListener('click', ()=>{
    visible += 6
    handleGetData()
})