/*
 * ===========================================
 *   Home Page Enhancements JavaScript
 *   Counter animations, interactive effects
 * ===========================================
 */

// ===== HOME PAGE ENHANCEMENTS MODULE =====
const HomePageEnhancements = {
    init() {
        this.initCounterAnimations();
        this.initTypingEffect();
        this.initDynamicBackground();
        this.initCardTilt();
        this.initScrollIndicator();
        this.initParallaxEffect();
    },

    // Counter Animation for Stats
    initCounterAnimations() {
        const counters = document.querySelectorAll('.counter');
        
        if (counters.length === 0) return;

        const animateCounter = (counter) => {
            const target = parseInt(counter.getAttribute('data-target'));
            const duration = 2000; // 2 seconds
            const increment = target / (duration / 16); // 60fps
            let current = 0;

            const updateCounter = () => {
                current += increment;
                if (current < target) {
                    counter.textContent = Math.floor(current).toLocaleString();
                    requestAnimationFrame(updateCounter);
                } else {
                    counter.textContent = target.toLocaleString();
                }
            };

            updateCounter();
        };

        // Intersection Observer for counter animation
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(counter => {
            counter.textContent = '0';
            counterObserver.observe(counter);
        });
    },

    // Typing Effect for Headers
    initTypingEffect() {
        const typingElements = document.querySelectorAll('.typing-effect');
        
        typingElements.forEach((element, index) => {
            const originalText = element.textContent;
            element.textContent = '';
            
            setTimeout(() => {
                this.typeText(element, originalText, 100);
            }, 500 + (index * 200));
        });
    },

    typeText(element, text, speed) {
        let i = 0;
        const timer = setInterval(() => {
            element.textContent += text.charAt(i);
            i++;
            if (i >= text.length) {
                clearInterval(timer);
                // Remove typing cursor after completion
                setTimeout(() => {
                    element.style.borderRight = 'none';
                }, 1000);
            }
        }, speed);
    },

    // Dynamic Background Effects
    initDynamicBackground() {
        const heroSection = document.querySelector('.hero-section');
        if (!heroSection) return;

        // Mouse move parallax effect
        heroSection.addEventListener('mousemove', (e) => {
            const particles = heroSection.querySelectorAll('.particle');
            const shapes = heroSection.querySelectorAll('.geo-shape');
            
            const mouseX = e.clientX / window.innerWidth;
            const mouseY = e.clientY / window.innerHeight;

            particles.forEach((particle, index) => {
                const speed = (index + 1) * 0.5;
                const x = (mouseX - 0.5) * speed * 20;
                const y = (mouseY - 0.5) * speed * 20;
                particle.style.transform += ` translate(${x}px, ${y}px)`;
            });

            shapes.forEach((shape, index) => {
                const speed = (index + 1) * 0.3;
                const x = (mouseX - 0.5) * speed * 15;
                const y = (mouseY - 0.5) * speed * 15;
                shape.style.transform += ` translate(${x}px, ${y}px)`;
            });
        });
    },

    // Card Tilt Effect
    initCardTilt() {
        const cards = document.querySelectorAll('[data-tilt]');
        
        cards.forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.transformStyle = 'preserve-3d';
            });

            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const centerX = rect.left + rect.width / 2;
                const centerY = rect.top + rect.height / 2;
                
                const mouseX = e.clientX - centerX;
                const mouseY = e.clientY - centerY;
                
                const rotateX = (mouseY / rect.height) * -10;
                const rotateY = (mouseX / rect.width) * 10;
                
                card.style.transform = `
                    rotateX(${rotateX}deg) 
                    rotateY(${rotateY}deg) 
                    translateZ(0)
                `;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = 'rotateX(0) rotateY(0) translateZ(0)';
            });
        });
    },

    // Enhanced Scroll Indicator
    initScrollIndicator() {
        const scrollIndicator = document.querySelector('.scroll-indicator');
        if (!scrollIndicator) return;

        scrollIndicator.addEventListener('click', () => {
            const featuresSection = document.querySelector('.features-section');
            if (featuresSection) {
                featuresSection.scrollIntoView({ 
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });

        // Hide scroll indicator when user scrolls
        let scrollTimeout;
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 100) {
                scrollIndicator.style.opacity = '0';
                scrollIndicator.style.visibility = 'hidden';
            } else {
                clearTimeout(scrollTimeout);
                scrollTimeout = setTimeout(() => {
                    scrollIndicator.style.opacity = '1';
                    scrollIndicator.style.visibility = 'visible';
                }, 500);
            }
        });
    },

    // Parallax Scrolling Effect
    initParallaxEffect() {
        const parallaxElements = document.querySelectorAll('.geo-shape, .floating-bg-icon');
        
        if (parallaxElements.length === 0) return;

        const handleScroll = () => {
            const scrolled = window.pageYOffset;
            
            parallaxElements.forEach((element, index) => {
                const speed = (index + 1) * 0.1;
                const yPos = -(scrolled * speed);
                element.style.transform += ` translateY(${yPos}px)`;
            });
        };

        // Throttled scroll handler for performance
        let ticking = false;
        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    handleScroll();
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
    }
};

// ===== ENHANCED BUTTON EFFECTS =====
const ButtonEnhancements = {
    init() {
        this.initMagneticEffect();
        this.initRippleEffect();
    },

    // Magnetic button effect
    initMagneticEffect() {
        const magneticButtons = document.querySelectorAll('.btn-hero-primary, .btn-hero-secondary');
        
        magneticButtons.forEach(button => {
            button.addEventListener('mousemove', (e) => {
                const rect = button.getBoundingClientRect();
                const centerX = rect.left + rect.width / 2;
                const centerY = rect.top + rect.height / 2;
                
                const mouseX = e.clientX - centerX;
                const mouseY = e.clientY - centerY;
                
                const distance = Math.sqrt(mouseX * mouseX + mouseY * mouseY);
                const maxDistance = 100;
                
                if (distance < maxDistance) {
                    const strength = (maxDistance - distance) / maxDistance;
                    const pullX = mouseX * strength * 0.3;
                    const pullY = mouseY * strength * 0.3;
                    
                    button.style.transform = `translate(${pullX}px, ${pullY}px) translateY(-3px)`;
                }
            });

            button.addEventListener('mouseleave', () => {
                button.style.transform = 'translate(0, 0) translateY(0)';
            });
        });
    },

    // Ripple effect for buttons
    initRippleEffect() {
        const rippleButtons = document.querySelectorAll('.btn-feature, .btn-hero-primary');
        
        rippleButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                const rect = button.getBoundingClientRect();
                const ripple = document.createElement('span');
                const size = Math.max(rect.width, rect.height);
                const x = e.clientX - rect.left - size / 2;
                const y = e.clientY - rect.top - size / 2;
                
                ripple.style.cssText = `
                    position: absolute;
                    width: ${size}px;
                    height: ${size}px;
                    left: ${x}px;
                    top: ${y}px;
                    background: rgba(255, 255, 255, 0.3);
                    border-radius: 50%;
                    transform: scale(0);
                    animation: ripple 0.6s linear;
                    pointer-events: none;
                `;
                
                button.style.position = 'relative';
                button.style.overflow = 'hidden';
                button.appendChild(ripple);
                
                setTimeout(() => {
                    ripple.remove();
                }, 600);
            });
        });

        // Add ripple animation CSS
        if (!document.querySelector('#ripple-animation')) {
            const style = document.createElement('style');
            style.id = 'ripple-animation';
            style.textContent = `
                @keyframes ripple {
                    to { transform: scale(4); opacity: 0; }
                }
            `;
            document.head.appendChild(style);
        }
    }
};

// ===== PERFORMANCE OPTIMIZATIONS =====
const PerformanceOptimizer = {
    init() {
        this.optimizeAnimations();
        this.preloadImages();
        this.deferNonCriticalAnimations();
    },

    optimizeAnimations() {
        // Pause animations when page is not visible
        document.addEventListener('visibilitychange', () => {
            const animations = document.querySelectorAll('*');
            animations.forEach(el => {
                if (document.hidden) {
                    el.style.animationPlayState = 'paused';
                } else {
                    el.style.animationPlayState = 'running';
                }
            });
        });
    },

    preloadImages() {
        // Preload critical images
        const criticalImages = [
            '/static/images/logo001.jpg',
            '/static/images/logo02.jpg'
        ];

        criticalImages.forEach(src => {
            const img = new Image();
            img.src = src;
        });
    },

    deferNonCriticalAnimations() {
        // Defer heavy animations until user interaction
        const heavyAnimations = document.querySelectorAll('.particle, .geo-shape');
        let userInteracted = false;

        const enableAnimations = () => {
            if (!userInteracted) {
                heavyAnimations.forEach(el => {
                    el.style.animationPlayState = 'running';
                });
                userInteracted = true;
            }
        };

        // Initially pause heavy animations
        heavyAnimations.forEach(el => {
            el.style.animationPlayState = 'paused';
        });

        // Enable animations on first user interaction
        ['click', 'scroll', 'mousemove', 'keydown'].forEach(event => {
            document.addEventListener(event, enableAnimations, { once: true });
        });
    }
};

// ===== AUTO-INITIALIZATION =====
document.addEventListener('DOMContentLoaded', () => {
    // Only initialize on home page
    if (window.location.pathname === '/') {
        HomePageEnhancements.init();
        ButtonEnhancements.init();
        PerformanceOptimizer.init();
        
        // Add some logging for development
        if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
            console.log('🏠 Home page enhancements loaded successfully!');
        }
    }
});

// Export for global access
window.HomePageEnhancements = HomePageEnhancements;
window.ButtonEnhancements = ButtonEnhancements;