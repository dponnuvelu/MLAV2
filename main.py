import pygame
import sys

WINDOW_WIDTH = 1240
WINDOW_HEIGHT = 1016
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
ROAD = pygame.image.load("assets/track.png")


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("assets/car.png")
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(150, 100))
        self.drive_state = False
        self.vel_vector = pygame.math.Vector2(0.8, 0)
        self.angle = 0
        self.rotation_vel = 5
        self.direction = 0

    def update(self):
        self.drive()
        self.rotate()

    def drive(self):
        if self.drive_state:
            self.rect.center += self.vel_vector * 6

    def rotate(self):
        if self.direction == 1:
            self.angle -=self.rotation_vel
            self.vel_vector.rotate_ip(self.rotation_vel)
        if self.direction == -1:
            self.angle +=self.rotation_vel
            self.vel_vector.rotate_ip(-self.rotation_vel)

        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.1)
        self.rect = self.image.get_rect(center = self.rect.center)


car = pygame.sprite.GroupSingle(Car())

def eval_genomes():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        WINDOW.blit(ROAD, (0, 0))

        user_input = pygame.key.get_pressed()

        if sum(pygame.key.get_pressed()) <= 1:
            car.sprite.drive_state = False
            car.sprite.direction = 0

        # steer forward
        if user_input[pygame.K_UP]:
            car.sprite.drive_state = True
        # steer right
        if user_input[pygame.K_RIGHT]:
            car.sprite.direction = 1
        # steer left
        if user_input[pygame.K_LEFT]:
            car.sprite.direction = -1


        car.draw(WINDOW)
        car.update()
        pygame.display.update()

eval_genomes()