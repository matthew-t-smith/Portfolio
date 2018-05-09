document.addEventListener('DOMContentLoaded', function() {
  // Load daily background photo from Unsplash API
  const photo = new UnsplashPhoto();
  const x = photo.randomize("daily")
    .fromCategory("building")
    .of(['architecture', 'bridge'])
    .fetch();

  const target1 = document.getElementById('card1');
  target1.style.backgroundImage = `url(${x})`;

  const target2 = document.getElementById('card2');
  target2.style.backgroundImage = `url(${x})`;

  const target3 = document.getElementById('card3');
  target3.style.backgroundImage = `url(${x})`;

  const target4 = document.getElementById('card4');
  target4.style.backgroundImage = `url(${x})`;
});
