(() => {
  'use strict';
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#site-nav');
  if (toggle && nav) {
    const setOpen = (open, restoreFocus = false) => {
      toggle.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
      toggle.querySelector('span').textContent = open ? '−' : '＋';
      if (restoreFocus) toggle.focus();
    };
    toggle.hidden = false;
    document.documentElement.classList.add('js');
    toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
    nav.addEventListener('click', (event) => {
      const link = event.target.closest('a');
      if (!link || toggle.getAttribute('aria-expanded') !== 'true') return;
      // Retira o foco do menu antes de ocultá-lo; âncoras locais recebem o foco.
      setOpen(false, true);
      const url = new URL(link.href);
      if (url.pathname === location.pathname && url.hash) {
        const destination = document.getElementById(url.hash.slice(1));
        if (destination) {
          destination.setAttribute('tabindex', '-1');
          destination.focus({ preventScroll:true });
        }
      }
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') setOpen(false, true);
    });
    document.addEventListener('click', (event) => {
      if (!event.target.closest('.site-header') && toggle.getAttribute('aria-expanded') === 'true') setOpen(false);
    });
    window.matchMedia('(min-width:761px)').addEventListener('change', () => setOpen(false));
  }
  document.querySelectorAll('[data-year]').forEach((element) => { element.textContent = new Date().getFullYear(); });
  const number = window.DEUTERA_CONTACT?.whatsappNumber || '';
  if (/^[1-9]\d{9,14}$/.test(number)) {
    document.querySelectorAll('[data-whatsapp]').forEach((button) => {
      const link = document.createElement('a');
      link.className = 'button button-primary';
      link.href = `https://wa.me/${number}`;
      link.textContent = 'Atendimento via WhatsApp ↗';
      button.replaceWith(link);
    });
    const status = document.querySelector('#contact-status');
    if (status) status.textContent = 'Converse com a DEUTERA pelo WhatsApp.';
  }
})();
