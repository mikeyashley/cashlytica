(function () {
  'use strict';

  function send(name, params) {
    try {
      if (typeof window.gtag === 'function') {
        window.gtag('event', name, Object.assign({ transport_type: 'beacon' }, params || {}));
      }
    } catch (_err) {}
  }

  document.addEventListener('click', function (event) {
    var element = event.target.closest('a, button');
    if (!element) return;
    var href = element.getAttribute('href') || '';
    var text = (element.getAttribute('data-analytics-label') || element.textContent || '').trim().slice(0, 100);
    var params = { link_text: text, link_url: href, page_location: window.location.pathname };
    if (href.indexOf('mailto:') === 0) {
      send('email_contact_click', Object.assign(params, { method: 'email' }));
    } else if (/\/register\b|register|audit/i.test(href + ' ' + text)) {
      send('registration_start', params);
      send('cta_click', Object.assign(params, { cta_type: 'registration' }));
    } else if (/\/samples\//i.test(href) || /sample|report/i.test(text)) {
      send('report_view', params);
      send('cta_click', Object.assign(params, { cta_type: 'report' }));
    } else if (/calculator|calculate/i.test(href + ' ' + text)) {
      send('calculator_start', params);
    } else if (element.matches('.btn, .button, [class*="cta"]')) {
      send('cta_click', params);
    }
  }, { capture: true });

  document.addEventListener('focusin', function (event) {
    var field = event.target;
    if (!field.matches('input, textarea, select')) return;
    var form = field.closest('form');
    if (!form || form.dataset.analyticsStarted) return;
    form.dataset.analyticsStarted = '1';
    send('form_start', { form_name: form.id || form.className || 'form', page_location: window.location.pathname });
  });

  document.addEventListener('submit', function (event) {
    var form = event.target;
    if (!form.matches('form')) return;
    send('form_submit', { form_name: form.id || form.className || 'form', page_location: window.location.pathname });
  }, { capture: true });
})();
