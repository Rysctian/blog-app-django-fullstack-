
const navContainer = document.querySelector('.nav-container');
const horizontalNav = document.querySelector('.horizontal-nav');
const leftArrow = document.getElementById('left-arrow');
const rightArrow = document.getElementById('right-arrow');

navContainer.addEventListener('scroll', function () {
    leftArrow.style.display = horizontalNav.scrollLeft > 0 ? 'block' : 'none';
    

    rightArrow.style.display = horizontalNav.scrollLeft < (horizontalNav.scrollWidth - horizontalNav.clientWidth) ? 'block' : 'none';
});

leftArrow.addEventListener('click', function () {
    horizontalNav.scrollBy({
        left: -100,
        behavior: 'smooth'
    });
});

rightArrow.addEventListener('click', function () {
    horizontalNav.scrollBy({
        left: 100,
        behavior: 'smooth'
    });
});