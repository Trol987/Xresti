import pygame
import pygame_menu
import sys

# Инициализация глобальной переменной (предотвращает ошибки при первом обращении)
difficulty_level = 1


def set_difficulty(value, difficulty):
    global difficulty_level
    difficulty_level = difficulty
    print(f"Выбор игры с: {value} (код: {difficulty_level})")


def start_the_game():
    mode_text = "С ботом" if difficulty_level == 1 else "С другом"
    print(f"Игра запущена! Режим: {mode_text}")

CYBERPUNK_THEME = pygame_menu.Theme(
    background_color=(5, 5, 15),
    title_background_color=(255, 20, 147),
    title_font_color=(0, 255, 255),
    widget_font_color=(0, 255, 180),
    selection_color=(255, 0, 255),
    widget_selection_effect=pygame_menu.widgets.SimpleSelection(),
    widget_background_color=(20, 0, 30),
    title_font_size=55,
    widget_font_size=32,
    cursor_color=(0, 255, 255),
    cursor_switch_ms=400,
    widget_padding=15,
    widget_border_color=(0, 255, 255),
    widget_border_width=2
)

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Крестики-нолики")
    bg_color = (255, 255, 255)
    
    menu = pygame_menu.Menu(
        "Крестики-нолики",
        1200, 800,
        theme=CYBERPUNK_THEME
    )

    menu.add.text_input("Имя: ", default="Игрок")
    menu.add.selector("Играть с: ", [("С ботом", 1), ("С другом", 2)], onchange=set_difficulty)
    menu.add.selector("Режим: ", [("Обычные крестики-нолики", 1), ("Мега крестики-нолики", 2)], onchange=set_difficulty)
    menu.add.button("Играть", start_the_game)
    menu.add.button("Выход", pygame_menu.events.EXIT)

    clock = pygame.time.Clock()  # Таймер для стабильного FPS

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(bg_color)
        
        if menu.is_enabled():
            menu.update(events)
            menu.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)  # Ограничение FPS до 60


run()