import pygame
import os
import math
import sys
import neat
import random

WINDOW_WIDTH = 1230
WINDOW_HEIGHT = 1000
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
ROAD = pygame.image.load("assets/track.png")


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("assets/car.png")
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(150, 100))

        self.vel_vector = pygame.math.Vector2(0.8, 0)
        self.angle = 0
        self.rotation_vel = 4
        self.direction = 0
        self.alive = True
        self.radars = []

    def update(self):
        self.radars.clear()
        self.drive()
        self.rotate()
        for radar_angle in (-60, -30, 0, 30, 60):
            self.radar(radar_angle)
        self.collision()
        self.data()

    def drive(self):
        self.rect.center += self.vel_vector * random.randint(1, 3)


    def collision(self):
        length = 25
        # 18 - 15
        x_right = int(self.rect.center[0] + math.cos(math.radians(self.angle + 15)) * length)
        y_right = int(self.rect.center[1] - math.sin(math.radians(self.angle + 15)) * length)
        x_left = int(self.rect.center[0] + math.cos(math.radians(self.angle - 15)) * length)
        y_left = int(self.rect.center[1] - math.sin(math.radians(self.angle - 15)) * length)
        if(x_left < 10):
            x_left = 10
        if (x_left >= WINDOW_WIDTH - 10):
            x_left = WINDOW_WIDTH - 20
        if (x_right < 10):
            x_right = 10
        if (x_right >= WINDOW_WIDTH - 10):
            x_right = WINDOW_WIDTH - 20
        if(y_left < 10):
            y_left = 10
        if (y_left >= WINDOW_HEIGHT - 10):
            y_left = WINDOW_HEIGHT - 10
        if (y_right < 10):
            y_right = 10
        if (y_right >= WINDOW_HEIGHT - 10):
            y_right = WINDOW_HEIGHT - 10


        collision_point_right = [x_right,y_right]
        collision_point_left = [x_left,y_left]
        # Die on Collision
        if WINDOW.get_at(collision_point_right) == pygame.Color(0, 0, 255, 255)\
                or WINDOW.get_at(collision_point_left) == pygame.Color(0, 0, 255, 255)\
                or WINDOW.get_at(collision_point_right) == pygame.Color(255, 253, 112, 255)\
                or WINDOW.get_at(collision_point_left) == pygame.Color(255, 253, 112, 255):
            self.alive = False

        # Draw Collision Points
        pygame.draw.circle(WINDOW, (0, 255, 255, 0), collision_point_right, 5)
        pygame.draw.circle(WINDOW, (0, 255, 255, 0), collision_point_left, 5)

    def rotate(self):
        if self.direction == 1:
            self.angle -=self.rotation_vel
            self.vel_vector.rotate_ip(self.rotation_vel)
        if self.direction == -1:
            self.angle +=self.rotation_vel
            self.vel_vector.rotate_ip(-self.rotation_vel)

        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def radar(self, radar_angle):
        length = 0
        x = int (self.rect.center[0])
        y = int (self.rect.center[1])

        #custom code start
        if (x < 5):
            x = 5
        if (y < 5):
            y = 5
        if (x >= WINDOW_WIDTH - 10):
            x = WINDOW_WIDTH - 20
        if (y >= WINDOW_HEIGHT - 10):
            y = WINDOW_HEIGHT - 20
        #custom code end
        while not (WINDOW.get_at((x, y)) == pygame.Color(0, 0, 255, 255) or WINDOW.get_at((x, y)) == pygame.Color(255, 253, 112, 255) or WINDOW.get_at((x, y)) == pygame.Color(255, 255, 255, 255)) and length < 100:
            length += 1
            x = int(self.rect.center[0] + math.cos(math.radians(self.angle + radar_angle)) * length)
            y = int(self.rect.center[1] - math.sin(math.radians(self.angle + radar_angle)) * length)
            if (x < 10):
                x = 10
            if (y < 10):
                y = 10
            if (x >= WINDOW_WIDTH - 10):
                x = WINDOW_WIDTH - 10
            if (y >= WINDOW_HEIGHT - 10):
                y = WINDOW_HEIGHT - 10
        #print (x, y)
        pygame.draw.line(WINDOW, (255, 0, 255, 255), self.rect.center, (x, y), 1)
        pygame.draw.circle(WINDOW, (255, 0, 255, 255), (x, y), 3)



        dist = int(math.sqrt(math.pow(self.rect.center[0] - x, 2) + math.pow(self.rect.center[1] - y, 2)))
        self.radars.append([radar_angle, dist])

    def data(self):
            input = [0, 0, 0, 0, 0]
            for i , radar in enumerate(self.radars):
                input[i] = int(radar[1])
            return input

def remove (index):
    cars.pop(index)
    ge.pop(index)
    nets.pop(index)

def eval_genomes(genomes, config):
    global cars, ge, nets
    cars = []
    ge = []
    nets = []

    for genome_id , genome in genomes:
        cars.append(pygame.sprite.GroupSingle(Car()))
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        WINDOW.blit(ROAD, (0, 0))

        if len(cars) == 0:
            break

        for i, car in enumerate(cars):
            ge[i].fitness += 1
            if not car.sprite.alive:
                remove(i)

        for i, car in enumerate(cars):
            output = nets[i].activate(car.sprite.data())
            if output[0] > 0.7:
                car.sprite.direction = 1
            if output[1] > 0.7:
                car.sprite.direction = -1
            if output[0] <= 0.7 and output[1] <= 0.7:
                car.sprite.direction = 0

        for car in cars:
            car.draw(WINDOW)
            car.update()
        pygame.display.update()

def run(config_path):
    global pop
    numGeneration  = 50
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    pop.run(eval_genomes, numGeneration)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
