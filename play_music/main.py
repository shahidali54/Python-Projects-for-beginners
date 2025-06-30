import pygame
import sys

def main():
    pygame.init()
    
    # Set window size and title
    screen = pygame.display.set_mode((550, 600))
    pygame.display.set_caption("Music Player")

    # Load disc image
    disc_image = pygame.image.load("dvd.png").convert_alpha()
    disc_rect = disc_image.get_rect(center=(300, 300))  # Center of screen

    # Load and play music
    pygame.mixer.pre_init(48000, -16, 2, 512)
    pygame.mixer.init()
    pygame.mixer.music.load("path/to/your/music/file.mp3") # Replace with your music file path
    pygame.mixer.music.play()

    # Clock for controlling frame rate
    clock = pygame.time.Clock()
    angle = 0

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Rotate the disc
        angle += 1
        if angle >= 360:
            angle = 0

        # Clear screen
        screen.fill((30, 30, 30))  # Dark background

        # Rotate image and draw
        rotated_disc = pygame.transform.rotate(disc_image, angle)
        rotated_rect = rotated_disc.get_rect(center=disc_rect.center)
        screen.blit(rotated_disc, rotated_rect)

        pygame.display.flip()
        clock.tick(60)  # 60 frames per second

        if not pygame.mixer.music.get_busy():
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
