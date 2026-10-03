const progress = document.getElementById('prog');
const navLinks = document.querySelectorAll('.nav-links a');

function updateScrollProgress() {
  const total = document.body.scrollHeight - window.innerHeight;
  const pct = total > 0 ? (window.scrollY / total) * 100 : 0;
  if (progress) progress.style.width = pct + '%';

  let current = '';
  const sections = document.querySelectorAll('section[id], .cta-section[id]');
  sections.forEach(section => {
    if (window.scrollY >= section.offsetTop - 120) current = section.id;
  });

  navLinks.forEach(link => {
    const target = link.getAttribute('href');
    link.classList.toggle('active', target === '#' + current);
  });
}

window.addEventListener('scroll', updateScrollProgress);

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add('vis');

    entry.target.querySelectorAll('.skill-bar-fill').forEach((bar, index) => {
      setTimeout(() => {
        bar.style.width = bar.dataset.w + '%';
      }, index * 100);
    });

    entry.target.querySelectorAll('.ring-fg').forEach((ring, index) => {
      const circle = 2 * Math.PI * 45;
      setTimeout(() => {
        ring.style.strokeDashoffset = circle * (1 - parseFloat(ring.dataset.pct) / 100);
      }, index * 150 + 80);
    });

    observer.unobserve(entry.target);
  });
}, { threshold: 0.12 });

['.reveal', '.tl-item', '.edu-card', '.cert-card', '.vol-card', '.lang-card', '.skill-section', '.edi-card', '.edi-why-card'].forEach(selector => {
  document.querySelectorAll(selector).forEach(el => observer.observe(el));
});

document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', (event) => {
    const target = document.querySelector(a.getAttribute('href'));
    if (target) {
      event.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    const nav = document.getElementById('nav-links');
    if (nav) nav.classList.remove('open');
  });
});

window.addEventListener('load', updateScrollProgress);
