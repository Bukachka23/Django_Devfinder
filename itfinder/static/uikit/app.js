// This code initializes syntax highlighting for code blocks once the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

// This block of code sets up an event listener for the close button of an alert. When the close button is clicked, the alert is hidden.
let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
  alertClose.addEventListener('click', () =>
    alertWrapper.style.display = 'none'
  )
}
