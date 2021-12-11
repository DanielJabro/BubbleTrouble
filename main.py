import math
import random as rand
import pygame
import time
import leaderboard as lb

pygame.init()

win = pygame.display.set_mode((900,620))
pygame.display.set_caption("Bubble Trouble")
clock = pygame.time.Clock()
bg = pygame.image.load("player1.gif")
background = pygame.image.load("Water.gif")
bg2 = pygame.image.load("player2.gif")
tri = pygame.image.load("triangle.png")
tri = pygame.transform.scale(tri, (50,30))
tri2 = pygame.image.load("triangle2.png")
tri2 = pygame.transform.scale(tri2, (50,30))
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (180,150))
jump = False #True
startb = False #True
jumpcount = 13
score = 0
adder = 100
pt = 0
font = pygame.font.Font(None, 50)
frame_count = 0
frame_rate = 26
frame_countdown = 0
frame_ratedown = 26
player1 = False #True
player2 = False #True
countdown = False
white = (255,255,255)
menu = True
orange = (255, 95, 31)
smallfont = pygame.font.SysFont('Corbel',50)
bigfont = pygame.font.SysFont('Verdana' , 100)
text2 = smallfont.render('2 Players' , True , white)
text = smallfont.render('1 Player' , True , white)
title = bigfont.render('Bubble Trouble' , True , orange)
color_dark = (100,100,100)
color_light = (170,170,170)
width = win.get_width()
height = win.get_height()
leaderboard_file_name = "score.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your team name:")

while menu:
  mouse = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      menu = False

    if event.type == pygame.MOUSEBUTTONDOWN:
      if 310 <= mouse[0] <= 590 and 220 <= mouse[1] <= 300: 
        jump = True #True
        startb = True #True
        player1 = True #True
        menu = False
      
      if 310 <= mouse[0] <= 590 and 410 <= mouse[1] <= 490: 
        jump = True #True
        startb = True #True
        player1 = True #True
        player2 = True #True
        menu = False

  win.fill((60,25,60))
  mouse = pygame.mouse.get_pos()
  
  if 310 <= mouse[0] <= 590 and 220 <= mouse[1] <= 300:
    pygame.draw.rect(win,color_light,[width/2 - 140,height/2 - 90,280,80])

  else:
    pygame.draw.rect(win,color_dark,[width/2 - 140,height/2 - 90,280,80])

  if 310 <= mouse[0] <= 590 and 410 <= mouse[1] <= 490:
    pygame.draw.rect(win,color_light,[width/2 - 140,height/2 + 100,280,80])
  
  else:
    pygame.draw.rect(win,color_dark,[width/2 - 140,height/2 + 100,280,80])

  win.blit(title , (130,50))
  win.blit(text , (width/2 - 70,height/2 - 65))
  win.blit(text2 , (width/2 - 70,height/2 + 125))

  pygame.display.update()

class p1():
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.vel = 10
    self.jumpcount = 10
    self.left = False
    self.right = False
    self.walkcount = 0
        
  def draw(self,win):
    if octo.walkcount + 1 >= 27:
      octo.walkcount = 0
      if left:
        win.blit(bg, (octo.x,octo.y))
        octo.walkcount -= 1
    elif right:
      win.blit(bg, (octo.x,octo.y))
      octo.walkcount += 1
    else:
      win.blit(bg, (octo.x,octo.y))

class Bubble():
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.grav = 1
    self.vel = 1
    self.velx = 4
    self.difference = 0
    self.jumpcount = 12
    self.left = False
    self.right = False
    self.walkcount = 0
    self.max = 399
    self.facing = 5

  def drawb(self, win):
    win.blit(ball, (self.x,self.y))

class p2():
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.vel = 10
    self.jumpcount = 10
    self.left = False
    self.right = False
    self.walkcount = 10

  def draw2(self,win):
    if self.walkcount + 1 >= 27:
      self.walkcount = 0
    if left:
      win.blit(bg2, (octo2.x,octo2.y))
      self.walkcount -= 1
    elif right:
      win.blit(bg2, (octo2.x,octo2.y))
      self.walkcount += 1
    else:
      win.blit(bg2, (octo2.x,octo2.y))

class projectile():
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.vel = 7

  def draw3(self,win):
    win.blit(tri, (self.x,self.y))

class projectile2():
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.vel = 7

  def draw4(self,win):
    win.blit(tri2, (self.x,self.y))

def double_points():
  global adder
  print("double score")
  adder = 200

def manage_leaderboard():
  global leader_scores_list
  global leader_names_list
  global score
  global spot
 
 # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)
 
 # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
   lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
   lb.draw_leaderboard(leader_names_list, leader_scores_list, True, octo, score)
 
  else:
   lb.draw_leaderboard(leader_names_list, leader_scores_list, False, octo, score)

def pop():
  global score
  dp = rand.randint(0,5)
  if dp == 2:
    countdown = True
    double_points()
  jump = False
  jumpcount = 12
  chance = rand.randint(1,10)
  if chance == 3:
    bubbles.append(Bubble(0, 0, 100, 100))
  rangrav = rand.randint(-1,1)
  if rangrav >= 0:
    bubble.grav = 1
  else:
    bubble.grav = -1
  global pt
  pt += 1
  score += adder
  ranx = rand.randint(0,800)
  rany = rand.randint(0,100)
  bubbles.append(Bubble(ranx, rany, 100, 100))

def redrawGameWindow():
  global frame_count
  win.blit(background, (0, -150))
  while countdown:
    global frame_countdown
    print("counting")
    remaining_time = 2000
    total_secondsdown = frame_countdown // frame_ratedown
    frame_countdown -= 1
    remaining_time = remaining_time - total_secondsdown
    print(remaining_time)
  pygame.draw.rect(win, white, (0,521,900,100))
  total_seconds = frame_count // frame_rate
  minutes = total_seconds // 60
  seconds = total_seconds % 60
  output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
  counted_score = "Score: {0}".format(score)
  text = font.render(output_string, True, (0,0,0))
  score_counter = font.render(counted_score, True, (0,0,0))
  win.blit(text, [15, 530])
  win.blit(score_counter, [15, 570])
  frame_count += 1
  if player1:
    for bullet in bullets:
      bullet.draw3(win)
  if player2:
    for arrow in arrows:
      arrow.draw4(win)
  if player1:
    octo.draw(win)
  for bubble in bubbles:
    bubble.drawb(win)
  if player2:
    octo2.draw2(win)
  pygame.display.flip()
  pygame.display.update()

run = True
if player2:
  octo2 = p2(400, 400, 64, 64)
if player1:
  octo = p1(500, 400, 64, 64)
  bullets = []
if player2:
  arrows = []
bubbles = []
if run:
  bubbles.append(Bubble(0, 0, 100, 100))
while run:
  clock.tick(26)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  if pt > 1:
    numberbubbles = rand.randint(0,0)
    if numberbubbles == 1:
      ranx = rand.randint(0,800)
      rany = rand.randint(0,100)
      bubbles.append(Bubble(ranx, rany, 100, 100))
    else:
      pt = pt

  if player1:
    for bullet in bullets:
      if bullet.y > -100:
        bullet.y -= bullet.vel
        for bubble in bubbles:
          d_x = abs(bullet.x) - abs(bubble.x) - 20
          d_y = abs(bullet.y) - abs(bubble.y)
          d = math.sqrt(d_x**2 + d_y**2)
          if d < 75:
            bubbles.pop(bubbles.index(bubble))
            pop()
            bullets.pop(bullets.index(bullet))
      else:
        bullets.pop(bullets.index(bullet))

  if player2:
    for arrow in arrows:
      if arrow.y > -100:
        arrow.y -= arrow.vel
        for bubble in bubbles:
          d_x = abs(arrow.x) - abs(bubble.x) - 20
          d_y = abs(arrow.y) - abs(bubble.y)
          d = math.sqrt(d_x**2 + d_y**2)
          if d < 75:
            bubbles.pop(bubbles.index(bubble))
            pop()
            arrows.pop(arrows.index(arrow))
      else:
        arrows.pop(arrows.index(arrow))
  
  for bubble in bubbles:

    if bubble.velx >= 12:
      bubble.velx = 12

    if (bubble.facing == 5):
      direction = 1
    else:
      direction = -1
          
    if bubble.x > 775:
      bubble.facing = 0
      bubble.grav += 0.15

    if bubble.x < 0:
      bubble.facing = 5
      bubble.grav += 0.15
      bubble.velx += 1

    if bubble.grav >= 7:
      bubble.grav = 7
      bubble.velx += 1
    print(bubble.y)
    if bubble.jumpcount >= -15 and jump and bubble.y <= 350:
      bubble.x += (bubble.velx * direction) - (bubble.grav * direction)
      bubble.y -= ((bubble.jumpcount * abs(bubble.jumpcount)) * 0.25) / bubble.grav
      bubble.vel -= 1
      bubble.jumpcount -= (.5)
    else:
      bubble.difference = 350 - bubble.y
      bubble.y += bubble.difference
      bubble.jumpcount = jumpcount
    
    if player1:
      d_x = abs(octo.x) - abs(bubble.x) - 20
      d_y = abs(octo.y) - abs(bubble.y)
      d = math.sqrt(d_x**2 + d_y**2)
      if d < 80:
        print("Player 1 Died")
        player1 = False

    if player2:
      d_x = abs(octo2.x) - abs(bubble.x) - 20
      d_y = abs(octo2.y) - abs(bubble.y)
      d = math.sqrt(d_x**2 + d_y**2)
      if d < 80:
        print("Player 2 Died")
        player2 = False

  keys = pygame.key.get_pressed()

  if player1:
    if keys[pygame.K_LEFT] and octo.x > octo.vel - 28:
      octo.x -= octo.vel
      left = True
      right = False

    elif keys[pygame.K_RIGHT] and octo.x < 800:
      octo.x += octo.vel
      right = True
      left = False
    else:
      right = False
      left = False
      octo.walkcount = 0

    if keys[pygame.K_UP]:
      if len(bullets) < 1:
        bullets.append(projectile(round(octo.x + octo.width//2), round(octo.y + octo.height//2 + 30), 6, (0,0,0)))
  if player2:
    if keys[pygame.K_SPACE]:
      if len(arrows) < 1:
        arrows.append(projectile2(round(octo2.x + octo2.width//2), round(octo2.y + octo2.height//2 + 30), 6, (0,0,0)))

    if keys[pygame.K_a] and octo2.x > octo2.vel - 28:
      octo2.x -= octo2.vel
      left = True
      right = False

    elif keys[pygame.K_d] and octo2.x < 800:
      octo2.x += octo2.vel
      right = True
      left = False
    else:
      right = False
      left = False
      octo2.walkcount = 0

  redrawGameWindow()
  if player1 or player2:
    run = True
  else:
    win = pygame.display.set_mode((1,1))
    manage_leaderboard()
    run = False

pygame.quit()