// Three.js Background Animation
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({
    canvas: document.querySelector('#bg-canvas'),
    alpha: true,
    antialias: true
});

renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);
camera.position.setZ(30);

// Add stars
function addStar() {
    const geometry = new THREE.SphereGeometry(0.15, 24, 24);
    const material = new THREE.MeshStandardMaterial({ color: 0xffffff });
    const star = new THREE.Mesh(geometry, material);

    const [x, y, z] = Array(3).fill().map(() => THREE.MathUtils.randFloatSpread(100));
    star.position.set(x, y, z);
    scene.add(star);
}
Array(200).fill().map(addStar);

// Lighting
const pointLight = new THREE.PointLight(0xffffff);
pointLight.position.set(5, 5, 5);
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(pointLight, ambientLight);

// Animation Loop
function animate() {
    requestAnimationFrame(animate);
    scene.rotation.x += 0.0005;
    scene.rotation.y += 0.001;
    renderer.render(scene, camera);
}
animate();

// Resize handling
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

// GSAP Animations
gsap.registerPlugin(ScrollTrigger);

// Hero Animations
const tl = gsap.timeline();

tl.from(".animate-hi", {
    y: 50,
    opacity: 0,
    duration: 0.8,
    ease: "power3.out"
})
    .from(".animate-name", {
        y: 50,
        opacity: 0,
        duration: 1,
        ease: "power4.out"
    })
    .from(".animate-role", {
        y: 30,
        opacity: 0,
        duration: 0.8,
        ease: "power2.out"
    })
    .from(".animate-bio", {
        opacity: 0,
        x: -20,
        duration: 0.8,
        ease: "power2.out"
    })
    .from(".hero-content .flex", {
        opacity: 0,
        y: 20,
        duration: 0.8,
        stagger: 0.2
    })
    .from(".hero-content .relative", {
        opacity: 0,
        scale: 0.5,
        duration: 1,
        ease: "back.out(1.7)"
    });

// Reveal sections on scroll (if they exist)
const sections = ['#about', '#experience', '#projects', '#contact'];
sections.forEach(selector => {
    const el = document.querySelector(selector);
    if (el) {
        gsap.from(el, {
            scrollTrigger: {
                trigger: el,
                start: "top 80%",
            },
            opacity: 0,
            y: 50,
            duration: 1,
            ease: "power2.out"
        });
    }
});
