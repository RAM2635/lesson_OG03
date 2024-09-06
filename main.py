import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Меткий Эколог")

# Загрузка иконки и изображений
icon = pygame.image.load("screns/logo3.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("screns/basket.png")
cursor_img = pygame.image.load("screns/cup30.png")  # Изображение курсора стакана
cursor_width, cursor_height = cursor_img.get_size()

target_width = 100
target_height = 100

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

# Отключаем стандартный курсор
pygame.mouse.set_visible(False)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Отображаем цель
    screen.blit(target_img, (target_x, target_y))

    # Получаем текущие координаты мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Отображаем изображение курсора на месте мыши
    screen.blit(cursor_img, (mouse_x - cursor_width // 2, mouse_y - cursor_height // 2))

    # Обновляем экран
    pygame.display.update()

pygame.quit()
