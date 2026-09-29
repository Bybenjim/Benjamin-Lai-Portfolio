document.getElementById('year').textContent = new Date().getFullYear();

// Work cards are rendered statically in index.html for SEO/crawlability, and
// the YouTube player only loads on interaction so the initial page load stays
// light. Cards are keyboard-operable (role="button", tabindex="0").
document.querySelectorAll('.work-card').forEach((card) => {
  card.addEventListener('click', () => loadVideo(card), { once: true });
  card.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      loadVideo(card);
    }
  });
});

function loadVideo(card) {
  if (card.querySelector('iframe')) return; // already loaded (click + keyboard both fired)
  const id = card.dataset.id;
  const title = card.getAttribute('aria-label') || 'YouTube video player';
  card.innerHTML = `<iframe
      src="https://www.youtube.com/embed/${id}?autoplay=1"
      title="${title}"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen></iframe>`;
}
