document.getElementById('year').textContent = new Date().getFullYear();

// Work cards are rendered statically in index.html for SEO/crawlability.
// This just adds click-to-play behaviour on top of the existing markup.
document.querySelectorAll('.work-card').forEach((card) => {
  card.addEventListener('click', () => loadVideo(card), { once: true });
});

// The Jaguar card carries a link back to the Experience section; don't let
// that click also trigger the card's own click-to-play handler.
document.querySelectorAll('.case-badge').forEach((badge) => {
  badge.addEventListener('click', (e) => e.stopPropagation());
});

function loadVideo(card) {
  const id = card.dataset.id;
  card.innerHTML = `<iframe
      src="https://www.youtube.com/embed/${id}?autoplay=1"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen></iframe>`;
}
