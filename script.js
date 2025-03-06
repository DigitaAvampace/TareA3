// script.js
document.addEventListener('DOMContentLoaded', () => {
  const collapsibleElements = document.querySelectorAll('.collapsible h2');
  
  collapsibleElements.forEach(header => {
    header.addEventListener('click', () => {
      const content = header.nextElementSibling;
      // Alternar la visibilidad
      if (content.style.display === "none") {
        content.style.display = "block";
      } else {
        content.style.display = "none";
      }
    });
  });
});
