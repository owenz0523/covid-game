##
# CPT: Final Project
#
# @author Owen Zhang
# @course ICS3UC-03
# @date 2021/06/21 - LastModified
#

## Pygame setup - entire template from Mr. Reid
import pygame
import random

# Player class - taken from Lab 13 program
class Player(pygame.sprite.Sprite):
  def __init__(self, filename):
    super().__init__()
 
    # Create image (needs work)
    self.image = pygame.image.load(filename).convert()
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.image.set_colorkey(BLACK)
    self.rect = self.image.get_rect()
    self.rect.x = 30
    self.rect.y = 150

    # Set speed vector
    self.change_x = 0
    self.change_y = 0

    # Scene of Player
    self.scene = 1

  # Change the speed of the player
  def changeSpeed(self, x, y):
    self.change_x += x
    self.change_y += y

  # Find a new position for the player
  def update(self):
    self.rect.x += self.change_x
    self.rect.y += self.change_y
    if self.rect.x < 20:
      self.rect.x = 20
    if self.rect.x > 330:
      self.rect.x = 330
    if self.rect.y < 20:
      self.rect.y = 20
    if self.rect.y > 230:
      self.rect.y = 230

# Objectives Class - taken from Lab 13
class Objective(pygame.sprite.Sprite):
  def __init__(self, filename):
    super().__init__()

    # Scene of objective
    self.scene = random.randrange(3, 8)
 
    # Create an image of the block
    self.image = pygame.image.load(filename).convert()
    self.image.set_colorkey(BLACK)
      
    # Fetch the rectangle object
    self.rect = self.image.get_rect()

# Draw scenes and effects for the game - used template from Mr. Reid's Alien, graphics used are referenced in final report
pos = [15, 15]
# Draw Scene 1
def drawIntroScreen1():
  introImage = pygame.image.load("graphics/intro.png").convert()
  screen.blit(introImage, pos)

# Draw Scene 2
def drawHallway2():
  hallwayImage = pygame.image.load("graphics/hallway.png").convert()
  screen.blit(hallwayImage, pos)
  pygame.draw.line(screen, WHITE, [80, 20], [160, 20], 8)
  pygame.draw.line(screen, WHITE, [240, 20], [320, 20], 8)
  pygame.draw.line(screen, WHITE, [80, 280], [160, 280], 8)
  pygame.draw.line(screen, WHITE, [240, 280], [320, 280], 8)
  pygame.draw.line(screen, WHITE, [380, 110], [380, 190], 8)

# Draw Scene 3
def drawBedroom3():
  bedroomImage = pygame.image.load("graphics/bedroom.png").convert()
  screen.blit(bedroomImage, pos)
  pygame.draw.line(screen, WHITE, [80, 280], [160, 280], 8)

# Draw Scene 4
def drawKitchen4():
  kitchenImage = pygame.image.load("graphics/kitchen.png").convert()
  screen.blit(kitchenImage, pos)
  pygame.draw.line(screen, WHITE, [155, 280], [235, 280], 8)

# Draw Scene 5
def drawStorage5():
  storageImage = pygame.image.load("graphics/storage.png").convert()
  screen.blit(storageImage, pos)
  pygame.draw.line(screen, WHITE, [15, 50], [15, 200], 8)

# Draw Scene 6
def drawLivingRoom6():
  livingImage = pygame.image.load("graphics/living.png").convert()
  screen.blit(livingImage, pos)
  pygame.draw.line(screen, WHITE, [285, 280], [355, 280], 8)

# Draw Scene 7
def drawBathroom7():
  bathroomImage = pygame.image.load("graphics/bathroom.png").convert()
  screen.blit(bathroomImage, pos)
  pygame.draw.line(screen, WHITE, [30, 280], [110, 280], 8)

# Draw Scene 8
def drawEndWinScreen8():
  winscreenImage = pygame.image.load("graphics/winscreen.png").convert()
  screen.blit(winscreenImage, pos)

# Draw Scene 9
def drawEndLossScreen9():
  losescreenImage = pygame.image.load("graphics/losescreen.png").convert()
  screen.blit(losescreenImage, pos)

# Draw out timer
def timerEffect(seconds):
  font = pygame.font.SysFont("Calibri", 15, True, False)
  text = font.render(seconds, True, WHITE)
  screen.blit(text, [370, 0])

# Create shadow effect - learned from stackoverflow.com/questions/29325169/pygame-setting-a-circle-that-erases-from-the-surface
def shadowEffect(x, y):
  shadow = pygame.Surface((400, 300))
  shadow.fill(BLACK)
  pygame.draw.circle(shadow, WHITE, (x+25, y+25), 75)
  shadow.set_colorkey(WHITE)
  screen.blit(shadow, (0,0))

# Create scoreboard
def drawScoreboard(score):
  font = pygame.font.SysFont("Calibri", 15, True, False)
  text = font.render(score, True, WHITE)
  screen.blit(text, [0, 0])

# Control scenes
def sceneControl(scene, x, y):
  if (scene == 2):
    if (y == 20) and (80 < x < 110):
      scene = 3
      x = 110
      y = 210
    elif (y == 20) and (240 < x < 270):
      scene = 4
      x = 185
      y = 210
    elif (x == 330) and (110 < y < 140):
      scene = 5
      x = 40
      y = 125
    elif (y == 230) and (80 < x < 110):
      scene = 6
      x = 305
      y = 210
    elif (y == 230) and (240 < x < 270):
      scene = 7
      x = 60
      y = 210
  elif (scene == 3):
    if (y == 230) and (80 < x < 110):
      scene = 2
      x = 110
      y = 40
  elif (scene == 4):
    if (y == 230) and (155 < x < 185):
      scene = 2
      x = 270
      y = 40
  elif (scene == 5):
    if (x == 20) and (50 < y < 125):
      scene = 2
      x = 300
      y = 140
  elif (scene == 6):
    if (y == 230) and (285 < x < 305):
      scene = 2
      x = 110
      y = 210
  elif (scene == 7):
    if (y == 230) and (30 < x < 60):
      scene = 2
      x = 270
      y = 210
  return scene, x, y

# Check collection - built on code from Lab 13
def collectionCheck(scene, objectives):
  if (scene == 3):
    scene3HitList = pygame.sprite.spritecollide(player, scene3List, True)
    for hit in scene3HitList:
      objectives += 1
  elif (scene == 4):
    scene4HitList = pygame.sprite.spritecollide(player, scene4List, True)
    for hit in scene4HitList:
      objectives += 1
  elif (scene == 5):
    scene5HitList = pygame.sprite.spritecollide(player, scene5List, True)
    for hit in scene5HitList:
      objectives += 1
  elif (scene == 6):
    scene6HitList = pygame.sprite.spritecollide(player, scene6List, True)
    for hit in scene6HitList:
      objectives += 1
  elif (scene == 7):
    scene7HitList = pygame.sprite.spritecollide(player, scene7List, True)
    for hit in scene7HitList:
      objectives += 1
  return objectives

# Initialize pygame
pygame.init()
size = (400, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CPT")

## MODEL - Data use in system
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Manage user objectives 
collectedObjectives = 0

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set up object lists - built on code from Lab 13
spritesList = pygame.sprite.Group()
playerList = pygame.sprite.Group()
scene3List = pygame.sprite.Group()
scene4List = pygame.sprite.Group()
scene5List = pygame.sprite.Group()
scene6List = pygame.sprite.Group()
scene7List = pygame.sprite.Group()

# Set up player object
player = Player("graphics/stickFigure.png")
playerList.add(player)
spritesList.add(player)

# Create 3 masks
for i in range(3):
  objective = Objective("graphics/mask.png")

  # Set random location for object
  objective.rect.x = random.randrange(20, 351)
  objective.rect.y = random.randrange(20, 262)

  # Add to list of sprites
  spritesList.add(objective)

# Create 2 sanitizer bottles
for i in range(2):
  objective = Objective("graphics/sanitizer.png")

  # Set random location for object
  objective.rect.x = random.randrange(20, 351)
  objective.rect.y = random.randrange(20, 251)

  # Add to total list of sprites
  spritesList.add(objective)

# Create 2 gloves
for i in range(2):
  objective = Objective("graphics/glove.png")

  # Set random location for object
  objective.rect.x = random.randrange(20, 351)
  objective.rect.y = random.randrange(20, 251)

  # Add to total list of sprites
  spritesList.add(objective)

# Create 2 vaccines
for i in range(2):
  objective = Objective("graphics/vaccine.png")

  # Set random location for object
  objective.rect.x = random.randrange(20, 351)
  objective.rect.y = random.randrange(20, 252)

  # Add to total list of sprites
  spritesList.add(objective)

# Tie object to specific scene
for obj in spritesList:
  if (obj.scene == 3):
    scene3List.add(obj)
  elif (obj.scene == 4):
    scene4List.add(obj)
  elif (obj.scene == 5):
    scene5List.add(obj)
  elif (obj.scene == 6):
    scene6List.add(obj)
  elif (obj.scene == 7):
    scene7List.add(obj)

# Set up timer
currentTime = 0
startTime = 0
gameStarted = False

## Main Program Loop
while not done:
    ## CONTROL
    # Check for events
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            done = True
    
        # Set the speed based on the key pressed - taken from Lab 13
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                player.changeSpeed(-2, 0)
            elif (event.key == pygame.K_RIGHT):
                player.changeSpeed(2, 0)
            elif (event.key == pygame.K_UP):
                player.changeSpeed(0, -2)
            elif (event.key == pygame.K_DOWN):
                player.changeSpeed(0, 2)
            
            # Change intro scene
            if (player.scene == 1):
              if (event.key == pygame.K_RETURN):
                player.scene = 2

                # Start timer once game begins
                gameStarted = True
                startTime = pygame.time.get_ticks()

            # Change end scene to stop game
            if (player.scene == 8) or (player.scene == 9):
              if (event.key == pygame.K_RETURN):
                done = True

        # Reset speed when key goes up
        elif (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT):
                player.changeSpeed(2, 0)
            elif (event.key == pygame.K_RIGHT):
                player.changeSpeed(-2, 0)
            elif (event.key == pygame.K_UP):
                player.changeSpeed(0, 2)
            elif (event.key == pygame.K_DOWN):
                player.changeSpeed(0, -2)
        
    ## Game logic
    spritesList.update()

    # Control in-game scenes
    player.scene, player.rect.x, player.rect.y = sceneControl(player.scene, player.rect.x, player.rect.y)

    # Check collection
    collectedObjectives = collectionCheck(player.scene, collectedObjectives)

    # Check if all items have been found
    if (collectedObjectives == 9):
      player.scene = 8
      gameStarted = False

    ## VIEW
    # Clear screen
    screen.fill(BLACK)

    # Draw - inspired by Mr. Reid's Scene Demo
    if (player.scene == 1):
      drawIntroScreen1()
    elif (player.scene == 8):
      drawEndWinScreen8()
    elif (player.scene == 9):
      drawEndLossScreen9()
    else: 
      if (player.scene == 2):
        drawHallway2()
      elif (player.scene == 3):
        drawBedroom3()
        scene3List.draw(screen)
      elif (player.scene == 4):
        drawKitchen4()
        scene4List.draw(screen)
      elif (player.scene == 5):
        drawStorage5()
        scene5List.draw(screen)
      elif (player.scene == 6):
        drawLivingRoom6()
        scene6List.draw(screen)
      elif (player.scene == 7):
        drawBathroom7()
        scene7List.draw(screen)
      playerList.draw(screen)

    # In-game effects
    if gameStarted:

      # Shadow effect
      shadowEffect(player.rect.x, player.rect.y)

      # Timer - learned from www.youtube.com/watch?v=YOCt8nsQqEo
      currentTime = pygame.time.get_ticks()
      actualTime = (currentTime - startTime)//(1000)
      seconds = str(60 - actualTime)
      timerEffect(seconds)

      # Scoreboard
      score = str(collectedObjectives) + "/9 items"
      drawScoreboard(score)
 
      # Check if any time is left
      if seconds == "0":
        player.scene = 9
        gameStarted = False

    # Update Screen
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit
pygame.quit()