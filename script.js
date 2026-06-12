const menuTrigger = document.querySelector('.menu-trigger');
    
menuTrigger.addEventListener('click', () => {
    console.log("Button was clicked!");
    const isExpanded = menuTrigger.getAttribute('aria-expanded') === 'true';
    
    menuTrigger.setAttribute('aria-expanded', !isExpanded);
});