function getCountdown() {
    const now = new Date();
    let bday = new Date(now.getFullYear(), 6, 21);
    if (now > bday) bday.setFullYear(now.getFullYear() + 1);
    const diff = bday - now;
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    document.getElementById("countdown").innerText = `⏳ Days until your next birthday: ${days}`;
}
getCountdown();

function revealMessage() {
    document.getElementById("secret").style.display = "block";
}

// Fireworks animation
let canvas = document.getElementById("fireworks");
let ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

function random(min, max) {
    return Math.random() * (max - min) + min;
}

function Firework() {
    this.x = random(0, canvas.width);
    this.y = canvas.height;
    this.radius = random(1, 3);
    this.color = `hsl(${random(0, 230)}, 100%, 50%)`;
    this.vy = random(-8, -12);
    this.life = 100;
}

Firework.prototype.update = function() {
    this.y += this.vy;
    this.life--;
};

Firework.prototype.draw = function() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = this.color;
    ctx.fill();
};

let fireworks = [];
let animationFrame;

function animate() {
    animationFrame = requestAnimationFrame(animate);
    ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    if (Math.random() < 0.05) fireworks.push(new Firework());
    fireworks.forEach((f, i) => {
        f.update();
        f.draw();
        if (f.life <= 0) fireworks.splice(i, 1);
    });
}

// Start the animation
animate();

// Stop the animation after 5 seconds
setTimeout(() => {
    cancelAnimationFrame(animationFrame); // Stop the animation loop
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
}, 3000); // 3000ms = 3 seconds