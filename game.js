const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const ui = document.getElementById('ui');

canvas.width = 800;
canvas.height = 400;

const GRAVITY = 0.5;
const FRICTION = 0.98;

let score1 = 0;
let score2 = 0;

function updateUI() {
    ui.textContent = `Score: ${score1} - ${score2}`;
}

class Ball {
    constructor(x, y) {
        this.reset(x, y);
        this.radius = 10;
    }

    reset(x, y) {
        this.x = x;
        this.y = y;
        this.vx = 0;
        this.vy = 0;
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = 'white';
        ctx.fill();
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.closePath();
    }

    update() {
        this.vy += GRAVITY;
        this.x += this.vx;
        this.y += this.vy;

        // Floor collision
        if (this.y + this.radius > canvas.height) {
            this.y = canvas.height - this.radius;
            this.vy *= -0.7;
            this.vx *= FRICTION;
        }

        // Wall collisions
        if (this.x - this.radius < 0) {
            this.x = this.radius;
            this.vx *= -0.7;
        } else if (this.x + this.radius > canvas.width) {
            this.x = canvas.width - this.radius;
            this.vx *= -0.7;
        }
    }
}

class Player {
    constructor(x, y, color, isPlayer1) {
        this.startX = x;
        this.startY = y;
        this.x = x;
        this.y = y;
        this.color = color;
        this.isPlayer1 = isPlayer1;
        this.width = 20;
        this.height = 50;
        this.vx = 0;
        this.vy = 0;
        this.speed = 5;
        this.jumpForce = -10;
        this.grounded = false;
        this.isKicking = false;
    }

    reset() {
        this.x = this.startX;
        this.y = this.startY;
        this.vx = 0;
        this.vy = 0;
    }

    draw() {
        ctx.strokeStyle = this.color;
        ctx.lineWidth = 3;

        // Head
        ctx.beginPath();
        ctx.arc(this.x, this.y - 45, 10, 0, Math.PI * 2);
        ctx.stroke();

        // Body
        ctx.beginPath();
        ctx.moveTo(this.x, this.y - 35);
        ctx.lineTo(this.x, this.y - 15);
        ctx.stroke();

        // Arms
        const armWave = Math.sin(Date.now() / 200) * 5;
        ctx.beginPath();
        ctx.moveTo(this.x - 15, this.y - 30 + armWave);
        ctx.lineTo(this.x + 15, this.y - 30 - armWave);
        ctx.stroke();

        // Legs
        const legWalk = Math.sin(Date.now() / 100) * 10 * (Math.abs(this.vx) / this.speed);
        ctx.beginPath();
        ctx.moveTo(this.x, this.y - 15);
        ctx.lineTo(this.x - 10 + legWalk, this.y);
        ctx.moveTo(this.x, this.y - 15);
        ctx.lineTo(this.x + 10 - legWalk, this.y);
        ctx.stroke();
    }

    update() {
        this.vy += GRAVITY;
        this.x += this.vx;
        this.y += this.vy;

        if (this.y > canvas.height) {
            this.y = canvas.height;
            this.vy = 0;
            this.grounded = true;
        } else {
            this.grounded = false;
        }

        this.vx *= FRICTION;

        // Keep player in bounds
        if (this.x < 0) this.x = 0;
        if (this.x > canvas.width) this.x = canvas.width;
    }
}

const ball = new Ball(canvas.width / 2, canvas.height / 2);
const player1 = new Player(100, canvas.height, 'blue', true);
const player2 = new Player(700, canvas.height, 'red', false);

const keys = {};

window.addEventListener('keydown', (e) => {
    keys[e.code] = true;
});

window.addEventListener('keyup', (e) => {
    keys[e.code] = false;
});

function handleInput() {
    // Player 1 controls (WASD)
    if (keys['KeyA']) player1.vx = -player1.speed;
    if (keys['KeyD']) player1.vx = player1.speed;
    if (keys['KeyW'] && player1.grounded) player1.vy = player1.jumpForce;
    player1.isKicking = keys['KeyQ'];

    // Player 2 controls (Arrows) or AI
    const p2UsingKeys = keys['ArrowLeft'] || keys['ArrowRight'] || keys['ArrowUp'] || keys['KeyP'];

    if (p2UsingKeys) {
        if (keys['ArrowLeft']) player2.vx = -player2.speed;
        if (keys['ArrowRight']) player2.vx = player2.speed;
        if (keys['ArrowUp'] && player2.grounded) player2.vy = player2.jumpForce;
        player2.isKicking = keys['KeyP'];
    } else {
        // Simple AI: Follow the ball
        const dx = ball.x - player2.x;
        if (Math.abs(dx) > 20) {
            player2.vx = Math.sign(dx) * (player2.speed * 0.7); // Slightly slower AI
        }

        // Jump if ball is high and close
        if (ball.y < player2.y - 50 && Math.abs(dx) < 50 && player2.grounded) {
            player2.vy = player2.jumpForce;
        }

        // Kick if close to ball
        const dist = Math.sqrt(dx*dx + (ball.y - (player2.y - 25))**2);
        player2.isKicking = dist < 40;
    }
}

function checkCollision(p, b) {
    const dx = p.x - b.x;
    const dy = (p.y - 25) - b.y;
    const distance = Math.sqrt(dx * dx + dy * dy);

    if (distance < p.height / 2 + b.radius) {
        const angle = Math.atan2(dy, dx);
        let force = 8;

        if (p.isKicking) {
            force = 15;
            // Add some upward force if kicking
            b.vy = -5;
        }

        b.vx = -Math.cos(angle) * force;
        // Only override vy if not kicking or if we want specific kick behavior
        if (!p.isKicking) {
            b.vy = -Math.sin(angle) * force;
        }
    }
}

function drawField() {
    // Pitch outer lines
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 5;
    ctx.strokeRect(0, 0, canvas.width, canvas.height);

    // Midline
    ctx.beginPath();
    ctx.moveTo(canvas.width / 2, 0);
    ctx.lineTo(canvas.width / 2, canvas.height);
    ctx.stroke();

    // Center circle
    ctx.beginPath();
    ctx.arc(canvas.width / 2, canvas.height / 2, 50, 0, Math.PI * 2);
    ctx.stroke();

    // Goals
    ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
    // Left Goal
    ctx.fillRect(0, canvas.height - 100, 30, 100);
    ctx.strokeRect(0, canvas.height - 100, 30, 100);
    // Right Goal
    ctx.fillRect(canvas.width - 30, canvas.height - 100, 30, 100);
    ctx.strokeRect(canvas.width - 30, canvas.height - 100, 30, 100);
}

function checkGoal() {
    // Left goal (Player 2 scores)
    if (ball.x - ball.radius < 30 && ball.y > canvas.height - 100) {
        score2++;
        resetPositions();
    }
    // Right goal (Player 1 scores)
    else if (ball.x + ball.radius > canvas.width - 30 && ball.y > canvas.height - 100) {
        score1++;
        resetPositions();
    }
}

function resetPositions() {
    ball.reset(canvas.width / 2, canvas.height / 2);
    player1.reset();
    player2.reset();
    updateUI();
}

function gameLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawField();
    handleInput();

    player1.update();
    player1.draw();

    player2.update();
    player2.draw();

    ball.update();
    ball.draw();

    checkCollision(player1, ball);
    checkCollision(player2, ball);
    checkGoal();

    requestAnimationFrame(gameLoop);
}

gameLoop();
updateUI();
