console.log('hello bitch')
const videosBox = document.getElementById('videos-box')
console.log(videosBox)
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const loadBox = document.getElementById('loading-box')
let visible = 6

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
                    videosBox.innerHTML += `<div class="col-md-6">
                                                <a class="text-decoration-none" href="${video.link}">
                                                <div class="card bg-dark text-center text-white mb-4 shadow-sm c-item">
                                                <div class="card-body" style="padding-bottom: 0;">
                                                  <h2 class="display-9 text-white">${video.title}</h2>
                                                  <p class="lead text-white">${video.short_description}</p>
                                                <div>
                                                <div class="bg-light shadow mx-auto" style="width: 80%;height: auto;border-radius: 21px 21px 0 0;">
                                                <img class="card-img-top w-100 b-img" src="${video.image}"></div>
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