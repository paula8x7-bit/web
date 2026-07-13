// Menú móvil
const burgerBtn = document.getElementById('burger-btn');
const mobileMenu = document.getElementById('mobile-menu');

burgerBtn.addEventListener('click', () => {
  mobileMenu.classList.toggle('open');
});

document.querySelectorAll('.close-menu').forEach((el) => {
  el.addEventListener('click', () => {
    mobileMenu.classList.remove('open');
  });
});

// Efectos hover genéricos a partir de data-hover
document.querySelectorAll('[data-hover]').forEach((el) => {
  const baseStyle = el.getAttribute('style') || '';
  const hoverStyle = el.getAttribute('data-hover');

  el.addEventListener('mouseenter', () => {
    el.setAttribute('style', baseStyle + ';' + hoverStyle);
  });
  el.addEventListener('mouseleave', () => {
    el.setAttribute('style', baseStyle);
  });
});
