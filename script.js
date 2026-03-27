// ==========================================
// URCA RP - JavaScript Simplificado
// ==========================================

const DISCORD_SELL_URL = 'https://discord.gg/ZgWVdm4H';

function isBuyActionElement(el) {
  if (!el) return false;

  const text = (el.textContent || '').toLowerCase().trim();
  const buyKeywords = [
    'comprar',
    'adquirir',
    'customizar',
    'aplicar',
    'ativar',
    'evoluir',
    'criar',
    'competir',
    'conferir'
  ];

  return buyKeywords.some((k) => text.includes(k));
}

function redirectToDiscord() {
  window.open(DISCORD_SELL_URL, '_blank', 'noopener,noreferrer');
}

// Menu mobile
function toggleMenu() {
  document.getElementById("menu").classList.toggle("ativo");
  document.querySelector(".hamburguer").classList.toggle("ativo");
}

// FAQ Accordion
function toggleFAQ(element) {
  const item = element.parentElement;
  const isActive = item.classList.contains("active");
  
  // Fecha todos os itens
  document.querySelectorAll(".faq-item").forEach(i => i.classList.remove("active"));
  
  // Abre o clicado se não estava ativo
  if (!isActive) item.classList.add("active");
}

// Comprar VIP
function comprar(plano) {
  const vip = (plano || 'vip').toUpperCase();
  alert(`Você escolheu o VIP ${vip}!\n\nRedirecionando para o Discord...`);
  redirectToDiscord();
}

// FiveM Integration (se necessário)
function comprarCarro(modelo) {
  if (typeof GetParentResourceName === 'function') {
    fetch(`https://${GetParentResourceName()}/comprarCarro`, {
      method: 'POST',
      body: JSON.stringify({ carro: modelo })
    });
    return;
  }

  redirectToDiscord();
}

document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('a, button').forEach((el) => {
    if (isBuyActionElement(el) && el.tagName.toLowerCase() === 'a') {
      el.setAttribute('href', DISCORD_SELL_URL);
      el.setAttribute('target', '_blank');
      el.setAttribute('rel', 'noopener noreferrer');
    }
  });

  document.addEventListener('click', function(e) {
    const target = e.target.closest('a, button');
    if (!target || !isBuyActionElement(target)) return;

    e.preventDefault();
    redirectToDiscord();
  });
});
