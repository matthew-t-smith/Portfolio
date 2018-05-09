const storage = window.localStorage;

document.addEventListener('DOMContentLoaded', function() {
  // Load daily background photo from Unsplash API
  const target = document.getElementById('header_background');
  const photo = new UnsplashPhoto();
  const x = photo.randomize("daily")
    .fromCategory("building")
    .of(['architecture', 'bridge'])
    .fetch();
  target.style.backgroundImage = `url(${x})`;
});
