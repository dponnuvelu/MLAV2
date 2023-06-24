import pygame

SCREEN_WIDTH = 1230
SCREEN_HEIGHT = 900
CURB_WIDTH = 20
LANE_WIDTH = 70
LANE_SEPARATOR = 5
SIGNAL_WIDTH = 10
OFFROAD_WIDTH = (SCREEN_WIDTH - 2*CURB_WIDTH - 6*LANE_WIDTH- 3*LANE_SEPARATOR)/2
OFFROAD_HEIGHT = (SCREEN_HEIGHT - 2*CURB_WIDTH - 6*LANE_WIDTH- 3*LANE_SEPARATOR)/2

INTERSECTION = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
INTERSECTION.fill('blue')

def create_intersection():

   #curb border
   pygame.draw.rect(INTERSECTION, 'black',
                    [CURB_WIDTH, CURB_WIDTH, 6*LANE_WIDTH +3*LANE_SEPARATOR+2*OFFROAD_WIDTH, 6*LANE_WIDTH+3*LANE_SEPARATOR+2*OFFROAD_HEIGHT])

   #four off road
   #row 1
   pygame.draw.rect(INTERSECTION, 'blue', [CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR,
                                           CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR, OFFROAD_WIDTH, OFFROAD_HEIGHT])
   pygame.draw.rect(INTERSECTION, 'blue', [CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+OFFROAD_WIDTH,
                                           CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR, OFFROAD_WIDTH, OFFROAD_HEIGHT])
   #row2
   pygame.draw.rect(INTERSECTION, 'blue',
                    [CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR,
                     CURB_WIDTH+4*LANE_WIDTH+OFFROAD_HEIGHT+2*LANE_SEPARATOR , OFFROAD_WIDTH, OFFROAD_HEIGHT])
   pygame.draw.rect(INTERSECTION, 'blue',
                    [CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+OFFROAD_WIDTH,
                     CURB_WIDTH+4*LANE_WIDTH+OFFROAD_HEIGHT+2*LANE_SEPARATOR, OFFROAD_WIDTH,
                     OFFROAD_HEIGHT])

   #horizontal lane seperator
   #row1
   pygame.draw.rect(INTERSECTION, 'white', [CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR, CURB_WIDTH+LANE_WIDTH, OFFROAD_WIDTH, LANE_SEPARATOR])
   pygame.draw.rect(INTERSECTION, 'white',
                    [CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+OFFROAD_WIDTH, CURB_WIDTH+LANE_WIDTH, OFFROAD_WIDTH,
                     LANE_SEPARATOR])

   #ow2
   pygame.draw.rect(INTERSECTION, 'white',
                    [CURB_WIDTH + 2*LANE_WIDTH +LANE_SEPARATOR, CURB_WIDTH+3*LANE_WIDTH+LANE_SEPARATOR+OFFROAD_HEIGHT, OFFROAD_WIDTH, LANE_SEPARATOR])
   pygame.draw.rect(INTERSECTION, 'white',
                    [CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+OFFROAD_WIDTH, CURB_WIDTH+3*LANE_WIDTH+LANE_SEPARATOR+OFFROAD_HEIGHT, OFFROAD_WIDTH,
                     LANE_SEPARATOR])

   #row3
   pygame.draw.rect(INTERSECTION, 'white',
                    [CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR, CURB_WIDTH+5*LANE_WIDTH+2*LANE_SEPARATOR+2*OFFROAD_HEIGHT, OFFROAD_WIDTH, LANE_SEPARATOR])
   pygame.draw.rect(INTERSECTION, 'white',
                    [CURB_WIDTH + 4*LANE_WIDTH +2*LANE_SEPARATOR + OFFROAD_WIDTH, CURB_WIDTH+5*LANE_WIDTH+2*LANE_SEPARATOR+2*OFFROAD_HEIGHT, OFFROAD_WIDTH,
                     LANE_SEPARATOR])

   #vertical lane seperator
   #row1
   pygame.draw.rect(INTERSECTION, 'white',
                    [CURB_WIDTH + LANE_WIDTH, CURB_WIDTH + 2 * LANE_WIDTH + LANE_SEPARATOR, LANE_SEPARATOR,
                     OFFROAD_HEIGHT])
   pygame.draw.rect(INTERSECTION, 'white',
                    [CURB_WIDTH + 3 * LANE_WIDTH + OFFROAD_WIDTH + LANE_SEPARATOR,
                     CURB_WIDTH + 2 * LANE_WIDTH + LANE_SEPARATOR, LANE_SEPARATOR, OFFROAD_HEIGHT])
   pygame.draw.rect(INTERSECTION, 'white',
                    [CURB_WIDTH + 5 * LANE_WIDTH + 2 * OFFROAD_WIDTH + 2 * LANE_SEPARATOR,
                     CURB_WIDTH + 2 * LANE_WIDTH + LANE_SEPARATOR, LANE_SEPARATOR,
                     OFFROAD_HEIGHT])

   #row2
   pygame.draw.rect(INTERSECTION, 'white',
                 [CURB_WIDTH+LANE_WIDTH, CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR++OFFROAD_HEIGHT, LANE_SEPARATOR, OFFROAD_HEIGHT])
   pygame.draw.rect(INTERSECTION, 'white',
                    [CURB_WIDTH+3*LANE_WIDTH+OFFROAD_WIDTH+LANE_SEPARATOR, CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+OFFROAD_HEIGHT, LANE_SEPARATOR,
                     OFFROAD_HEIGHT])
   pygame.draw.rect(INTERSECTION, 'white',
                    [CURB_WIDTH+5*LANE_WIDTH+2*OFFROAD_WIDTH+2*LANE_SEPARATOR, CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+OFFROAD_HEIGHT,
                     LANE_SEPARATOR, OFFROAD_HEIGHT])

def create_signals(vSignalColor, hSignalColor):
   #vertical signal
   # row1
   pygame.draw.rect(INTERSECTION, vSignalColor,
                    [CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR, CURB_WIDTH,
                     SIGNAL_WIDTH, LANE_WIDTH])
   pygame.draw.rect(INTERSECTION, vSignalColor,
                    [CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+OFFROAD_WIDTH, CURB_WIDTH,
                     SIGNAL_WIDTH, LANE_WIDTH])
   # row2
   pygame.draw.rect(INTERSECTION, vSignalColor,
                    [CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR,
                     CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR+OFFROAD_HEIGHT,
                     SIGNAL_WIDTH, LANE_WIDTH])

   pygame.draw.rect(INTERSECTION, vSignalColor,
                    [CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+OFFROAD_WIDTH,
                     CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR+OFFROAD_HEIGHT,
                     SIGNAL_WIDTH, LANE_WIDTH])

   #row3
   pygame.draw.rect(INTERSECTION, vSignalColor,
                    [CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR,
                     CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+2*OFFROAD_HEIGHT,
                     SIGNAL_WIDTH, LANE_WIDTH])
   pygame.draw.rect(INTERSECTION, vSignalColor,
                    [CURB_WIDTH+4*LANE_WIDTH+OFFROAD_WIDTH+2*LANE_SEPARATOR,
                     CURB_WIDTH+4*LANE_WIDTH+2*OFFROAD_HEIGHT+2*LANE_SEPARATOR,
                     SIGNAL_WIDTH, LANE_WIDTH])

   #row1
   pygame.draw.rect(INTERSECTION, vSignalColor,
                    [CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR+OFFROAD_WIDTH-SIGNAL_WIDTH, CURB_WIDTH+LANE_WIDTH+LANE_SEPARATOR,
                     SIGNAL_WIDTH, LANE_WIDTH])
   pygame.draw.rect(INTERSECTION, vSignalColor,
                    [CURB_WIDTH +4*LANE_WIDTH+2*LANE_SEPARATOR+2*OFFROAD_WIDTH-SIGNAL_WIDTH, CURB_WIDTH+LANE_WIDTH+LANE_SEPARATOR,
                     SIGNAL_WIDTH, LANE_WIDTH])
   #row2
   pygame.draw.rect(INTERSECTION, vSignalColor,
                    [CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR+OFFROAD_WIDTH-SIGNAL_WIDTH, CURB_WIDTH + 3*LANE_WIDTH+OFFROAD_HEIGHT+2*LANE_SEPARATOR,
                     SIGNAL_WIDTH, LANE_WIDTH])
   pygame.draw.rect(INTERSECTION, vSignalColor,
                    [CURB_WIDTH +4*LANE_WIDTH+2*LANE_SEPARATOR+2*OFFROAD_WIDTH-SIGNAL_WIDTH, CURB_WIDTH + 3*LANE_WIDTH+OFFROAD_HEIGHT+2*LANE_SEPARATOR,
                     SIGNAL_WIDTH, LANE_WIDTH])
   #row3
   pygame.draw.rect(INTERSECTION, vSignalColor,
                    [CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR+OFFROAD_WIDTH-SIGNAL_WIDTH,
                     CURB_WIDTH + LANE_WIDTH * 5 + 2*OFFROAD_HEIGHT+3*LANE_SEPARATOR,
                     SIGNAL_WIDTH, LANE_WIDTH])
   pygame.draw.rect(INTERSECTION, vSignalColor,
                    [CURB_WIDTH +4*LANE_WIDTH+2*LANE_SEPARATOR+2*OFFROAD_WIDTH-SIGNAL_WIDTH,
                     CURB_WIDTH + LANE_WIDTH * 5 + 2*OFFROAD_HEIGHT+3*LANE_SEPARATOR,
                     SIGNAL_WIDTH, LANE_WIDTH])

   #horizontal signal
   #col1
   pygame.draw.rect(INTERSECTION, hSignalColor,
                    [CURB_WIDTH, CURB_WIDTH+2*LANE_WIDTH++LANE_SEPARATOR+OFFROAD_HEIGHT-SIGNAL_WIDTH,
                     LANE_WIDTH, SIGNAL_WIDTH])

   pygame.draw.rect(INTERSECTION, hSignalColor,
                    [CURB_WIDTH, CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+2*OFFROAD_HEIGHT-SIGNAL_WIDTH,
                     LANE_WIDTH, SIGNAL_WIDTH])

   #col3
   pygame.draw.rect(INTERSECTION, hSignalColor,
                    [CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR+OFFROAD_WIDTH ,
                     CURB_WIDTH+2*LANE_WIDTH++LANE_SEPARATOR+OFFROAD_HEIGHT-SIGNAL_WIDTH, LANE_WIDTH, SIGNAL_WIDTH])
   pygame.draw.rect(INTERSECTION, hSignalColor,
                    [CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR+OFFROAD_WIDTH ,
                     CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+2*OFFROAD_HEIGHT-SIGNAL_WIDTH,
                     LANE_WIDTH, SIGNAL_WIDTH])

   #col5
   pygame.draw.rect(INTERSECTION, hSignalColor,
                    [CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+2*OFFROAD_WIDTH ,
                     CURB_WIDTH+2*LANE_WIDTH++LANE_SEPARATOR+OFFROAD_HEIGHT-SIGNAL_WIDTH, LANE_WIDTH, SIGNAL_WIDTH])
   pygame.draw.rect(INTERSECTION, hSignalColor,
                    [CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+2*OFFROAD_WIDTH ,
                     CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+2*OFFROAD_HEIGHT-SIGNAL_WIDTH,
                     LANE_WIDTH, SIGNAL_WIDTH])
   # col2
   pygame.draw.rect(INTERSECTION, hSignalColor,
                    [CURB_WIDTH+LANE_WIDTH+LANE_SEPARATOR, CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR,
                     LANE_WIDTH, SIGNAL_WIDTH])

   pygame.draw.rect(INTERSECTION, hSignalColor,
                    [CURB_WIDTH+LANE_WIDTH+LANE_SEPARATOR, CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+OFFROAD_HEIGHT,
                     LANE_WIDTH, SIGNAL_WIDTH])
   #col4
   pygame.draw.rect(INTERSECTION, hSignalColor,
                    [CURB_WIDTH+3*LANE_WIDTH+2*LANE_SEPARATOR+OFFROAD_WIDTH, CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR,
                     LANE_WIDTH, SIGNAL_WIDTH])

   pygame.draw.rect(INTERSECTION, hSignalColor,
                    [CURB_WIDTH+3*LANE_WIDTH+2*LANE_SEPARATOR+OFFROAD_WIDTH,
                     CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+OFFROAD_HEIGHT,
                     LANE_WIDTH, SIGNAL_WIDTH])
   # col6
   pygame.draw.rect(INTERSECTION, hSignalColor,
                    [CURB_WIDTH+5*LANE_WIDTH+3*LANE_SEPARATOR+2*OFFROAD_WIDTH,
                     CURB_WIDTH+2*LANE_WIDTH+LANE_SEPARATOR,
                     LANE_WIDTH, SIGNAL_WIDTH])

   pygame.draw.rect(INTERSECTION, hSignalColor,
                    [CURB_WIDTH+5*LANE_WIDTH+3*LANE_SEPARATOR+2*OFFROAD_WIDTH,
                     CURB_WIDTH+4*LANE_WIDTH+2*LANE_SEPARATOR+OFFROAD_HEIGHT,
                     LANE_WIDTH, SIGNAL_WIDTH])



def createAssets():
    create_intersection()
    create_signals('red', 'green')
    image = pygame.image.save(INTERSECTION, "assets/intersect_RG.png")

    create_intersection()
    create_signals('red', 'yellow')
    image = pygame.image.save(INTERSECTION, "assets/intersect_RY.png")

    create_intersection()
    create_signals('green', 'red')
    image = pygame.image.save(INTERSECTION, "assets/intersect_GR.png")

    create_intersection()
    create_signals('yellow', 'red')
    image = pygame.image.save(INTERSECTION, "assets/intersect_YR.png")
    pygame.quit()



createAssets()



