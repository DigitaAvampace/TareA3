document.addEventListener('DOMContentLoaded', () => {
  // Modo oscuro
  const themeToggle = document.querySelector('.theme-toggle');
  themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    themeToggle.querySelector('i').classList.toggle('fa-sun');
  });

  // Fecha y hora
  const datetimeEl = document.getElementById('datetime');
  function updateDateTime() {
    const now = new Date();
    datetimeEl.textContent = now.toLocaleString('es-ES', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    });
  }
  setInterval(updateDateTime, 1000);
  updateDateTime();

  // Animación de entrada para paneles
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = 1;
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.panel').forEach(panel => {
    panel.style.opacity = 0;
    panel.style.transform = 'translateY(20px)';
    panel.style.transition = 'all 0.6s ease-out';
    observer.observe(panel);
  });

  // Expandir/colapsar paneles
  document.querySelectorAll('.panel-header').forEach(header => {
    header.addEventListener('click', () => {
      const panel = header.closest('.panel');
      panel.classList.toggle('open');
    });
  });
});
