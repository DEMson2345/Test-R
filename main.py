from pygame import*
from random import randint

init()
#img_win = "maxresdefauit.jpg"
#img_los = "e_1g3qa_2IL1U_UDEeWzHODCaoR2.png"
#img_back = "с16303d599d6cfbc0655c7ba7f97asf1.jpg"
#img_bullet = "1ml-3ml-5ml-10ml-50ml-luer-lock.jpg"
#img_hero = "depositphotos_220218926-stock-photo-handgun-isolated-while-background.jpg"
#img_enemy = "2e5cd15d39b9e95560980c11499cdd48.jpg"

score = 0 
goal = 10
lost = 0 
max_lost = 3

win_width = 700
win_height = 500
display.set_caption("My shuter")
window = display.set_mode((win_width, win_height))
background = transform.scale (image.load("1.jpg"), (win_width,win_height))



class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale (image.load(player_image),(size_x,size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

   

class Enemy(GameSprite):
    def update(self):
        self.rect.y = self.rect.y + self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(80, win_width - 80)
            lost = lost+1


class Bullet(GameSprite):
    def update(self):
        self.rect.y = self.rect.y - self.speed
        if self.rect.y < 0:
            self.kill()


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()    
        if keys[K_LEFT] :
            self.rect.x -= self.speed
        if keys[K_RIGHT] :
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("2.jpg", self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
        



me = Player("3.jpg", 5, win_height - 100, 80, 100, 10)

sprites  = sprite.Group() # s = [ ]
for i in range(1,6):
    monster = Enemy("4.jpg", randint(80, 420), -40, 80, 50, randint(1,5))
    sprites.add(monster)


bullets = sprite.Group()

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type ==  KEYDOWN:
            if e.key == K_SPACE:
                me.fire()


    if not finish:
        window.blit(background, (0,0))
        me.update()
        sprites.update()
        bullets.update()
        
        me.reset()
        sprites.draw(window)
        bullets .draw(window)
        display.update()



        collide = sprite.groupcollide(sprites, bullets, True, True)
        for i in collide:
            monster = Enemy("5.jpg", randit(80, 420), -40, 80, 50, randit(1,5))
            sprites.add(monster)
        if sprite.spritecollide(me,collide,False): #или False????
            finish = True
        if score >= goal:
            finish = True 
        
    display.update ()  
    time.delay(50)    




    window.fill ((255, 255, 255))
    window.blit(transform.scale(image.load("7.jpg"), (win_height, win_height)), (90, 0))