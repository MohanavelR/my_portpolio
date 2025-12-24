// Page Loader
window.addEventListener('load', () => {
    const loader = document.getElementById('pageLoader');
    setTimeout(() => {
        loader.classList.add('hidden');
    }, 1000);
});

// Scroll Reveal Animation
const revealElements = document.querySelectorAll(
    '.scroll-reveal, .scroll-reveal-left, .scroll-reveal-right, .scroll-reveal-scale, .scroll-reveal-rotate'
);

const revealOnScroll = () => {
    revealElements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        
        if (elementTop < windowHeight - 50) {
            element.classList.add('active');
        }
    });
};

window.addEventListener('scroll', revealOnScroll);
revealOnScroll(); // Initial check

// Header Scroll Effect
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// Mobile Menu Toggle
const menuToggle = document.getElementById('menuToggle');
const navMenu = document.getElementById('navMenu');
const panelOverlay = document.getElementById('panelOverlay');

menuToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    panelOverlay.classList.toggle('active');
    const icon = menuToggle.querySelector('i');
    icon.classList.toggle('fa-bars');
    icon.classList.toggle('fa-times');
});

// Close menu when clicking on links
navMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        panelOverlay.classList.remove('active');
        const icon = menuToggle.querySelector('i');
        icon.classList.add('fa-bars');
        icon.classList.remove('fa-times');
    });
});

// Theme Panel Toggle
const themePanel = document.getElementById('themePanel');
const themePanelToggle = document.getElementById('themePanelToggle');

themePanelToggle.addEventListener('click', (e) => {
    e.stopPropagation();
    themePanel.classList.toggle('active');
    panelOverlay.classList.toggle('active');
});

// Close panels when clicking overlay
panelOverlay.addEventListener('click', () => {
    themePanel.classList.remove('active');
    navMenu.classList.remove('active');
    panelOverlay.classList.remove('active');
    const icon = menuToggle.querySelector('i');
    icon.classList.add('fa-bars');
    icon.classList.remove('fa-times');
});

// Dark/Light Mode Toggle
const modeSwitch = document.getElementById('modeSwitch');
const modeText = document.getElementById('modeText');
const body = document.body;

modeSwitch.addEventListener('click', () => {
    body.classList.toggle('light-mode');
    const icon = modeSwitch.querySelector('i');
    
    if (body.classList.contains('light-mode')) {
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
        modeText.textContent = 'Light Mode';
        localStorage.setItem('theme', 'light');
    } else {
        icon.classList.remove('fa-sun');
        icon.classList.add('fa-moon');
        modeText.textContent = 'Dark Mode';
        localStorage.setItem('theme', 'dark');
    }
});

// Load saved theme preference
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'light') {
    body.classList.add('light-mode');
    const icon = modeSwitch.querySelector('i');
    icon.classList.remove('fa-moon');
    icon.classList.add('fa-sun');
    modeText.textContent = 'Light Mode';
}

// Color Theme Selection
const colorOptions = document.querySelectorAll('.color-option');

colorOptions.forEach(option => {
    option.addEventListener('click', () => {
        colorOptions.forEach(opt => opt.classList.remove('active'));
        option.classList.add('active');
        const theme = option.getAttribute('data-theme');
        
        // Remove all theme classes
        body.className = body.className.replace(/theme-\d/g, '');
        body.classList.add(`theme-${theme}`);
        
        // Preserve light mode if active
        if (savedTheme === 'light' || body.classList.contains('light-mode')) {
            body.classList.add('light-mode');
        }
        
        // Save theme preference
        localStorage.setItem('colorTheme', theme);
    });
});

// Load saved color theme
const savedColorTheme = localStorage.getItem('colorTheme');
if (savedColorTheme) {
    body.className = body.className.replace(/theme-\d/g, '');
    body.classList.add(`theme-${savedColorTheme}`);
    colorOptions.forEach(opt => {
        if (opt.getAttribute('data-theme') === savedColorTheme) {
            opt.classList.add('active');
        } else {
            opt.classList.remove('active');
        }
    });
}

// Smooth Scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Typing Animation
const typedTextSpan = document.querySelector('.typed-text');
const words = ['Web Developer', 'Frontend Developer', 'Backend Developer', 'Full Stack Developer'];
let wordIndex = 0;
let charIndex = 0;
let isDeleting = false;

function type() {
    const currentWord = words[wordIndex];
    
    if (isDeleting) {
        typedTextSpan.textContent = currentWord.substring(0, charIndex - 1);
        charIndex--;
    } else {
        typedTextSpan.textContent = currentWord.substring(0, charIndex + 1);
        charIndex++;
    }

    if (!isDeleting && charIndex === currentWord.length) {
        setTimeout(() => isDeleting = true, 2000);
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        wordIndex = (wordIndex + 1) % words.length;
    }

    const typingSpeed = isDeleting ? 50 : 100;
    setTimeout(type, typingSpeed);
}

// Start typing animation after page loads
setTimeout(type, 1000);

// Animate skill progress bars
const animateSkillBars = () => {
    const skillBars = document.querySelectorAll('.skill-progress');
    skillBars.forEach(bar => {
        const width = bar.getAttribute('data-width');
        bar.style.width = width + '%';
    });
};

// Trigger skill bar animation when scrolling to skills section
const skillsSection = document.querySelector('.info-card.scroll-reveal-right');
if (skillsSection) {
    const skillsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateSkillBars();
                skillsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    skillsObserver.observe(skillsSection);
}