# 3AM Tetro 🎮

> A remake of Tetris but specially designed to play at 3AM with dark theme and soothing background music 🌙

**3AM Tetro** is a Python/Pygame based Tetris game

## How to Play 📥

Downlaod the **3AM Tetro.exe** from the repository files.

## Controls 🕹️
|---|---|
| `←` / `A` | Move left |
| `→` / `D` | Move right |
| `↓` / `S` | Move down faster |
| `↑` / `W` | Rotate piece |
| `ESC` | Quit game |

## Screenshots 📸


## Tetrominos 
```python
SYSTEMS = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}
```

## Built With 🛠️

- **Python**
- **Pygame**
- **Pygame Freetype**
- **PyInstaller**

## Base Text 📜
```python
def draw(self):
        self.font.render_to(
            self.app.screen,
            (WIN_W * 0.595, WIN_H * 0.02),
            text='3AM',
            fgcolor='red',
            size=TILE_SIZE * 1.4)
```

## Project Structure 📁

```text
Tetris/
├── main.py
├── settings.py
├── system.py
├── tetris.py
│
├── assets/
│   ├── background.png
│   ├── icon.png
│   ├── icon.ico
│   ├── music.mp3
│   ├── fonts/
│   └── sprites/
│
└── main.exe
```

## Future Updates 🎯
- Add More UI Options
- Add Animated Background
- Add Better Sprites
- More Game Logics

## Author 👤
Created with ❤️ by Arman Ahmad