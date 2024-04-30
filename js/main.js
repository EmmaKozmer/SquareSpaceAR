document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.large-box').addEventListener('click', () => {
        location.href = 'creative_mode_ar.html';
    });
    document.querySelector('.yellow-box').addEventListener('click', () => {
        location.href = 'inspirations.html';
    });
    document.querySelector('.green-box').addEventListener('click', () => {
        location.href = 'favourites.html';
    });
    document.querySelector('.blue-box').addEventListener('click', () => {
        location.href = 'about_us.html';
    });
});


function saveImageToLocalStorage(data, name) {
    var images = JSON.parse(localStorage.getItem('galleryImages')) || {};
    images[name] = data;
    localStorage.setItem('galleryImages', JSON.stringify(images));
}

function loadImagesFromLocalStorage() {
    var images = JSON.parse(localStorage.getItem('galleryImages')) || {};
    var dynamicGalleryContainer = document.querySelector('.gallery-container');

    Object.keys(images).forEach(function(name) {
        var imgElement = document.createElement('img');
        imgElement.src = images[name];
        imgElement.alt = name;
        imgElement.className = 'image'; 

        var divElement = document.createElement('div');
        divElement.className = 'gallery-item';
        divElement.appendChild(imgElement);

        var starIcon = document.createElement('div');
        starIcon.className = 'star-icon';
        starIcon.innerHTML = '&#9733;';
        starIcon.onclick = function(event) {
            toggleFavorite(event, name);
        };
        divElement.appendChild(starIcon);

        dynamicGalleryContainer.appendChild(divElement);

        imgElement.onclick = function() {
            modal.style.display = 'block';
            modalImg.src = this.src;
            captionText.innerHTML = this.alt;
        };
    });
}