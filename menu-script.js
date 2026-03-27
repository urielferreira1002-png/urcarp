/* ============================================
   ⚙️ MENU URCA RP - SCRIPT SEM HAMBURGUER
============================================ */

// Navegação entre seções
function navigate(section) {
  const sections = document.querySelectorAll('.content-section');
  sections.forEach(s => s.style.display = 'none');

  const selected = document.getElementById(section);
  if (selected) {
    selected.style.display = 'block';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // Fecha menus
  const menuLateral = document.querySelector('.menu-lateral');

  if (window.innerWidth <= 768 && menuLateral) {
    menuLateral.classList.remove('active');
  }
}

// Menu lateral
function toggleMenu() {
  const menu = document.querySelector('.menu-lateral');
  if (menu) menu.classList.toggle('active');
}

function toggleHeaderMenu(e) {
  if (e && typeof e.preventDefault === 'function') e.preventDefault();
  if (e && typeof e.stopPropagation === 'function') e.stopPropagation();

  const menu = document.getElementById('headerMenu');
  const btn = document.querySelector('.hamburger-btn');
  if (!menu || !btn) return;

  const open = !menu.classList.contains('active');
  menu.classList.toggle('active', open);
  btn.classList.toggle('active', open);
  btn.setAttribute('aria-expanded', open ? 'true' : 'false');
}

document.addEventListener('DOMContentLoaded', function() {
  const menu = document.getElementById('headerMenu');
  const btn = document.querySelector('.hamburger-btn');

  if (!menu || !btn) return;

  btn.setAttribute('aria-expanded', 'false');

  btn.addEventListener('click', function(e) {
    toggleHeaderMenu(e);
  });

  menu.addEventListener('click', function(e) {
    e.stopPropagation();
  });

  document.addEventListener('click', function(e) {
    if (!menu.contains(e.target) && !btn.contains(e.target)) {
      menu.classList.remove('active');
      btn.classList.remove('active');
      btn.setAttribute('aria-expanded', 'false');
    }
  });

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      menu.classList.remove('active');
      btn.classList.remove('active');
      btn.setAttribute('aria-expanded', 'false');
    }
  });
});