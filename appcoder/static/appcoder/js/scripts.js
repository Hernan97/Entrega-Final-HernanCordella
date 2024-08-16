/*!
* Start Bootstrap - Landing Page v6.0.6 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function toggleEditSection() {
    var section = document.getElementById('editSection');
    if (section.classList.contains('show')) {
        section.classList.remove('show');
    } else {
        section.classList.add('show');
    }
}