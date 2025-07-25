document.addEventListener('DOMContentLoaded', () => {
    // Create rotating cubes
    const container = document.querySelector('.cubes-container');
    const logo = document.querySelector('.logo');
    const cubeCount = 6;
    const maxSizePercent = 1;
    const rotationSpeed = 90;
    const angleStep = 50;
    
    function createCubes() {
        container.innerHTML = '';
        
        const logoRect = logo.getBoundingClientRect();
         // Сдвигаем центр кубов вправо (добавляем 20% от ширины экрана)
        const logoCenterX = logoRect.left + logoRect.width/2 + window.innerWidth * 0.0;
        const logoCenterY = logoRect.top + logoRect.height/2;
        
        const maxSizePx = Math.min(window.innerWidth, window.innerHeight) * maxSizePercent;
        
        let sizes = [];
        for (let i = 0; i < cubeCount; i++) {
            if (i === 0) {
                sizes[i] = 500 + (i / 2 * (maxSizePx + 200) / (cubeCount - 1));
            } else {
                sizes[i] = sizes[i - 1] / 1.2;
            }
        }

        for (let i = 0; i < cubeCount; i++) {
            const cube = document.createElement('div');
            cube.classList.add('cube');
            
            const size = sizes[i];
            cube.style.width = `${size}px`;
            cube.style.height = `${size}px`;
            
            cube.style.animationDuration = `${rotationSpeed}s`;
            
            const startAngle = i * angleStep;
            cube.style.setProperty('--start-angle', `${startAngle}deg`);
            
            cube.style.left = `${logoCenterX - size * 0.65}px`;
            cube.style.top = `${logoCenterY - size * 0.5}px`;
            
            container.appendChild(cube);
        }
    }

    // Scroll functionality
    const scrollButton = document.getElementById('scrollButton');
    
    
    // Initialize and handle resize
    createCubes();
    window.addEventListener('resize', () => {
        createCubes();
    });
});
function loh(){
        document.location.href = "/login";
    }
    