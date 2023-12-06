<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Space Shooter Game</title>

    <style>
        body {
            background-color: #f2f2f2; /* Light grey background color */
            color: #333; /* Dark text color */
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        h1 {
            color: #333; /* Dark text color */
        }

        h2 {
            color: #555; /* Slightly darker text color */
        }

        h3 {
            color: #777; /* Lighter text color */
        }

        pre {
            background-color: #ddd; /* Light grey background for code blocks */
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }

        code {
            font-family: 'Courier New', Courier, monospace;
        }
    </style>
</head>

<body>

    <h1>Welcome to the Space Shooter Game!</h1>
    <p>This simple Pygame-based project is a space-themed shooter where players control a spaceship, shoot enemies, and survive as long as possible. The game features dynamic enemy spawning, particle effects, and a scoring system.</p>

    <h2>Getting Started</h2>

    <h3>Prerequisites</h3>
    <p>To run the game, you need to have Python and Pygame installed on your machine. You can install Pygame using the following command:</p>
    <pre><code>pip install pygame</code></pre>

    <h3>Running the Game</h3>
    <p>After installing the required dependencies, you can run the game by executing the main script:</p>
    <pre><code>python main.py</code></pre>

    <h2>Game Controls</h2>
    <ul>
        <li>Move Left: <kbd>A</kbd></li>
        <li>Move Right: <kbd>D</kbd></li>
        <li>Shoot: <kbd>SPACE</kbd></li>
    </ul>

    <h2>Gameplay Features</h2>
    <ul>
        <li><strong>Player Ship:</strong> Control a spaceship using the left and right arrow keys. Shoot enemies by pressing the spacebar.</li>
        <li><strong>Enemies:</strong> Enemies spawn dynamically and move horizontally. Shoot them to earn points.</li>
        <li><strong>Particle Effects:</strong> Particle effects are triggered when enemies are hit, adding visual flair to the gameplay.</li>
        <li><strong>Scoring:</strong> Earn points by shooting enemies. The player's score and best score are displayed during gameplay.</li>
        <li><strong>Lives:</strong> Players start with a certain number of lives. Colliding with enemies decreases the number of lives.</li>
        <li><strong>Game Over:</strong> The game ends when the player runs out of lives. The final score is displayed, and the player can restart the game.</li>
    </ul>

    <h2>Project Structure</h2>
    <ul>
        <li><strong>main.py:</strong> The main script to run the game.</li>
        <li><strong>ship.py:</strong> Contains the <code>Ship</code> class, representing the player's spaceship.</li>
        <li><strong>bullet.py:</strong> Defines the <code>Bullet</code> class for player bullets.</li>
        <li><strong>enemy.py:</strong> Implements the <code>Enemy</code> class for enemy spaceships.</li>
        <li><strong>particle.py:</strong> Contains the <code>Particle</code> class for particle effects.</li>
        <li><strong>enemy_spawner.py:</strong> Manages the spawning of enemy spaceships.</li>
        <li><strong>particle_spawner.py:</strong> Handles the creation and updating of particle effects.</li>
        <li><strong>hud.py:</strong> Defines the Heads-Up Display (HUD) for displaying scores and lives.</li>
        <li><strong>background.py:</strong> Manages the background visuals.</li>
    </ul>

    <h2>Acknowledgments</h2>
    <p>This project uses the Pygame library for game development.</p>

    <p>Feel free to explore, modify, and enhance the game to suit your preferences. Enjoy the Space Shooter Game! 🚀🎮</p>

</body>

</html>
