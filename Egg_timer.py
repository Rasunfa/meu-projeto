import asyncio
import platform
import time
import msvcrt
import sys
import pygame
FPS = 60

# Inicialização do Pygame
pygame.init()
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timer de Ovos Cozidos")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Carregar imagem estática
image_path = "C:/Users/manel/Desktop/ProjetoFinal/Egg.jpg"  # Substitua pelo caminho da sua imagem
try:
    image = pygame.image.load(image_path).convert_alpha()
    image = pygame.transform.scale(image, (200, 150))
except:
    image = pygame.Surface((200, 150))
    image.fill((255, 0, 0))  # Placeholder vermelho se imagem não encontrada

# Definição das caixas (botões)
buttons = {
    "mole": pygame.Rect(5, 250, 150, 50),
    "médio": pygame.Rect(175, 250, 150, 50),
    "duro": pygame.Rect(345, 250, 150, 50),
    "terminar": pygame.Rect(175, 320, 150, 50)
}
button_texts = {
    "mole": "Ovo Mole (5min)",
    "médio": "Ovo Médio (7min)",
    "duro": "Ovo Duro (10min)",
    "terminar": "Terminar"
}
font = pygame.font.Font(None, 24)

# Tempos em segundos
egg_times = {"mole": 300, "médio": 420, "duro": 600}

def setup():
    screen.fill(WHITE)

def update_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for egg_type, rect in buttons.items():
                if rect.collidepoint(mouse_pos):
                    if egg_type == "terminar":
                        sys.exit(0)
                    else:
                        start_timer(egg_type)

    screen.fill(WHITE)
    screen.blit(image, (150, 50))  # Exibe a imagem estática no topo
    for egg_type, rect in buttons.items():
        color = GREEN if egg_type == "terminar" else BLACK
        pygame.draw.rect(screen, color, rect, 2)
        text_surface = font.render(button_texts[egg_type], True, color)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    if msvcrt.kbhit() and msvcrt.getch() == b' ':
        print("\nTimer interrompido pelo usuário!")
        sys.exit(0)

    pygame.display.flip()

def start_timer(egg_type):
    seconds = egg_times[egg_type]
    while seconds > 0:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if buttons["terminar"].collidepoint(mouse_pos):
                    print("\nAplicação encerrada pelo botão Terminar!")
                    sys.exit(0)
        if msvcrt.kbhit() and msvcrt.getch() == b' ':
            print("\nTimer interrompido pelo usuário!")
            return
        mins, secs = divmod(seconds, 60)
        timer_text = f"Tempo: {mins:02d}:{secs:02d}"
        screen.fill(WHITE)
        screen.blit(image, (150, 50))
        for egg_type, rect in buttons.items():
            color = GREEN if egg_type == "terminar" else BLACK
            pygame.draw.rect(screen, color, rect, 2)
            text_surface = font.render(button_texts[egg_type], True, color)
            text_rect = text_surface.get_rect(center=rect.center)
            screen.blit(text_surface, text_rect)
        timer_surface = font.render(timer_text, True, RED)
        screen.blit(timer_surface, (250, 200))
        pygame.display.flip()
        time.sleep(1)
        seconds -= 1
    print("\nTimer finalizado! Seu ovo está pronto!")

async def main():
    setup()
    while True:
        update_loop()
        await asyncio.sleep(1.0 / FPS)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())