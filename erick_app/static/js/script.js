let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

function showSlide(index) {
    slides[currentSlide].classList.remove('active');
    currentSlide = (index + slides.length) % slides.length; // Loop back
    slides[currentSlide].classList.add('active');
    const videoContainer = document.querySelector('.video-container');
    videoContainer.style.display = currentSlide === slides.length - 1 ? 'block' : 'none';
}

function nextSlide() {
    showSlide(currentSlide + 1);
}

// Show the first slide and hide the video initially
showSlide(currentSlide);
