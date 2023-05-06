import pygame
w = 750
h = 550
window = pygame.display.set_mode((w,h))
pygame.display.set_caption("Pin-Pong")
background = pygame.transform.scale(pygame.image.load("background.jpg"),(w,h))
class GameSprite(pygame.sprite.Sprite):
    def __init__ (self, width, height, player_image,player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect() # Створити рамку навколо картинки спрайта
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self): # Функція для того щоб намалювати спрайт на екрані
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y <= 600:
            self.rect.y += self.speed
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.x >= 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.x <= 600:
            self.rect.y += self.speed
game = True
finish = False
clock = pygame.time.Clock()
FPS = 60

racket1 = Player(50, 50,('mishka_player.jpg'), 5, 50, 10)
racket2 = Player(50, 50,('monster_player.jpg'), 600, 50, 10)
ball = GameSprite(50, 50,('photo.jpg'), 250, 50, 10)

pygame.font.init()
font = pygame.font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x +=  speed_x 
        ball.rect.y += speed_y

        if pygame.sprite.collide_rect(racket1, ball) or pygame.sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y = 1

        
        if ball.rect.x < 0:
            finish = True
            window.blit (lose1, (200, 200))
            game_over = True

        racket1.reset()
        racket1.reset()
        racket1.reset()

        if finish != True:
            racket1.update_l()
            racket2.update_r()
            ball.rect.x += speed_x
            ball.rect.x += speed_x
            
            if pygame.sprite.collide_rect(racket1, ball) or pygame.sprite.collide_rect(racket2, ball):
                speed_x *= -1
                speed_x *= 1

            if ball.rect.y > 550 or ball.rect.y < 0:
                speed_y *= -1


            if ball.rect.x < 0:
                finish = True
                window.blit(lose1, (200, 200))
                game_over = True

            racket1.reset()
            racket2.reset()
            ball.reset()
            clock.tick(40)
            pygame.display.update()















            


