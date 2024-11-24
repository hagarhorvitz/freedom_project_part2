
function confirmDeleteVacation(id){
    const ok = confirm(`Are you sure you want to delete this vacation (ID: ${id})?`);
    if (!ok){
        event.preventDefault();
    };
};

const newUpdateDeletePopupMessage = document.querySelector(".admin_action");
if (newUpdateDeletePopupMessage){
    setTimeout(() => {
        newUpdateDeletePopupMessage.parentNode.removeChild(newUpdateDeletePopupMessage);
    }, 4000);
};

const errorPopupMessage = document.querySelector(".error");
if (errorPopupMessage){
    setTimeout(() => {
        errorPopupMessage.parentNode.removeChild(errorPopupMessage);
    }, 5000);
};


const helloUserPopupMessage = document.querySelector(".clicked");
if (helloUserPopupMessage){
    setTimeout(() => {
        helloUserPopupMessage.parentNode.removeChild(helloUserPopupMessage);
    }, 4000);
};


const vacationForm = document.querySelector(".new_update_vacation_form");
if (vacationForm)
document.getElementById('select_image').addEventListener('change', function() {
    const fileName = this.files.length > 0 ? this.files[0].name : 'No file selected';
    document.getElementById('show_file_name').textContent = "File name: " + fileName;
});


async function handleLikeOrUnlike(button, userId, vacationId) {
    // console.log("userId: " + userId)
    // console.log("vacationId: " + vacationId)
    const heartImage = document.getElementById(`image_${vacationId}`);
    const likesCountParagraph = document.getElementById(`likes_${vacationId}`);
    let LikesCount = parseInt(likesCountParagraph.textContent);
    try {
        const response = await fetch(`/likes/${userId}/${vacationId}`, {method: "POST"});
        // console.log(response);
        const data = await response.json();
        // console.log(data);
        if (response.ok) {
            //console.log(data.result);
            if (data.result == "unlike"){
                heartImage.src = "/static/logos/white_hearts.png";
                button.innerText = "Like";
                LikesCount-- ;
            }
            else if (data.result == "like"){
                heartImage.src = "/static/logos/red_hearts.png";
                button.innerText = "Unlike";
                LikesCount++ ;
            }
        }
        else if (!response.ok) {
            throw new Error("failed to update like/unlike status.");
        }
        heartImage.classList.add("likes_heart");
        likesCountParagraph.textContent = LikesCount;
        console.log("button clicked - all good (:");
    } catch (error) {
        console.error('Error in handleLikeOrUnlike function:', error);
    }
};
  
const gallery = document.getElementById("gallery_container");
if (gallery){
    document.addEventListener('DOMContentLoaded', async function(){
    try {
        const response = await fetch('/home/images', {method: "GET"});
        console.log(response);
        const data = await response.json();
        if (response.ok) {
            const allImages = data.images;
            console.log(allImages);
            for (let i = 0; i <allImages.length; i++){
                let image_name = allImages[i]
                console.log(i + " " + image_name);

                let img = document.createElement("img");
                img.alt = image_name;
                img.src = `/static/home_gallery_images/${image_name}`;
                img.classList.add("home_image");

                let a = document.createElement("a");
                a.appendChild(img);
                gallery.appendChild(a);
            };
        }
        else if (!response.ok) {
            throw new Error("failed to upload images");
        }
    } catch (error) {
        console.error('Error in uploading images', error);
    };
    });
};

