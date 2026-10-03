document.getElementById('contact-form')?.addEventListener('submit', function (event) {
  event.preventDefault();
  if (!this.reportValidity()) return;
  const data = new FormData(this);
  const subject = data.get('subject') || 'Contact Form Message';
  const body = `Name: ${data.get('name')}\nEmail: ${data.get('email')}\n\nMessage:\n${data.get('message')}`;
  window.location.href = `mailto:sahilkarawade@outlook.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
});
