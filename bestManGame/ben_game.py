# 1 - Import library
import random
import pygame
from pygame.locals import *
# 2 - Initialize the game
pygame.init()
WHITE = (255, 255, 255)
GREEN = (1, 50, 32)
width, height = 1000, 780
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos=[300,100]
discs = []
disc_pic = pygame.image.load("disc.png")
rand_disc = 0
basketpos1=[-10,550]
basketpos2=[190,550]
basketpos3=[390,550]
basketpos4=[590,550]
basketpos5=[790,550]
par = [1, 2, 3, 4, 5]
player = pygame.image.load("ben.png")
disc_image = [pygame.image.load("disc.png"), pygame.image.load("disc2.png"), pygame.image.load("disc3.png"), pygame.image.load("disc4.png"), pygame.image.load("disc5.png")]
basket1 = pygame.image.load("basket.png")
basket2 = pygame.image.load("basket.png")
basket3 = pygame.image.load("basket.png")
basket4 = pygame.image.load("basket.png")
basket5 = pygame.image.load("basket.png")
images = [[300, 100]]

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 60)
rule_font = pygame.font.SysFont('Arial', 25)
game_font = pygame.font.SysFont('Arial', 30)
scores = []
nailed_it = []
pygame.mixer.init()
clink = pygame.mixer.Sound('clink.wav')
pygame.mixer.music.load('jack_j.mp3')
pygame.mixer.music.play(-1)

# 4 - keep looping through
while 1:
    text = "[W]:Up \n[S]:Down \n[A]:Left \n[D]:Right \n[Space]:Throw Disc"
    game_rules = game_font.render("Try and get a disc in all five baskets to win!", 0, (255, 255, 255))
    for x in range(100):
        rand_disc = random.randint(0,4)
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0) 
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
            elif event.key==K_SPACE:
                throw=True
                discpos1=playerpos[:]
                discs.append([disc_pic, playerpos[:]])
                disc_pic = disc_image[rand_disc]
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False

    # # 9 - Move player
    if keys[0]:
        playerpos[1]-=8
    elif keys[2]:
        playerpos[1]+=8
    if keys[1]:
        playerpos[0]-=8
    elif keys[3]:
        playerpos[0]+=8
   
    for d in range(len(discs)):
        if ((discs[d][1][0] >= 40 and discs[d][1][0] <= 85) and (discs[d][1][1] >= 600 and discs[d][1][1] <= 610)):
            nailed_it.append(d)
            if 1 in par:
                par.remove(1)
        elif ((discs[d][1][0] >= 240 and discs[d][1][0] <= 285) and (discs[d][1][1] >= 600 and discs[d][1][1] <= 610)):
            nailed_it.append(d)
            if 2 in par:
                par.remove(2)
        elif ((discs[d][1][0] >= 440 and discs[d][1][0] <= 485) and (discs[d][1][1] >= 600 and discs[d][1][1] <= 610)):
            nailed_it.append(d)
            if 3 in par:
                par.remove(3)
        elif ((discs[d][1][0] >= 640 and discs[d][1][0] <= 685) and (discs[d][1][1] >= 600 and discs[d][1][1] <= 610)):
            nailed_it.append(d)
            if 4 in par:
                par.remove(4)
        elif ((discs[d][1][0] >= 840 and discs[d][1][0] <= 885) and (discs[d][1][1] >= 600 and discs[d][1][1] <= 610)):
            nailed_it.append(d)
            if 5 in par:
                par.remove(5)
        else:
            discs[d][1][1] += 10
   
    for i in nailed_it:
        if i not in scores:
           # pygame.mixer.Sounds.load('clink.mp3')
            pygame.mixer.Sound.play(clink)
            scores.append(i)

    screen.fill(GREEN)
    if (len(par) == 0):
        textsurface = myfont.render('Ben, will you be my best man?', False, (255, 255, 255))
        screen.blit(textsurface,(70,400))
    for disc in discs:
        screen.blit(disc[0], pygame.Rect(disc[1][0], disc[1][1], 0, 0))
  
    screen.blit(game_rules,(30,30))
    lines = text.splitlines()
    for i, l in enumerate(lines):
        screen.blit(rule_font.render(l, 0, (255, 255, 255)), (700, 30 +25*i))
    screen.blit(player, playerpos)
    screen.blit(basket1, basketpos1)
    screen.blit(basket2, basketpos2)
    screen.blit(basket3, basketpos3)
    screen.blit(basket4, basketpos4)
    screen.blit(basket5, basketpos5)

    pygame.display.flip()














