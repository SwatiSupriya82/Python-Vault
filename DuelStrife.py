import pygame

pygame.init()
start_screen=True
player1_image=pygame.image.load("Character 2.png")
player2_image=pygame.image.load("Character1.png")
player1_image = pygame.transform.scale(player1_image, (180, 320))
player2_image = pygame.transform.scale(player2_image, (150, 280))

player1_image_right=player1_image
player1_image_left=pygame.transform.flip(player1_image_right, True, False)

player2_image_left=player2_image
player2_image_right=pygame.transform.flip(player2_image_left, True, False)

player1_attacking = False
player2_attacking = False

screen = pygame.display.set_mode((800,700))
pygame.display.set_caption("Duel Strife")

player1_x=50
player1_y=600
player2_x=600
player2_y=600
player1_facing=1
player2_facing=-1

clock=pygame.time.Clock()
 
player1_speed_y=0
player1_on_ground=True
player2_speed_y=0
player2_on_ground=True

player1_health=100
player2_health=100

player1_attackcooldown=0
player2_attackcooldown=0

font = pygame.font.Font(None, 60)
font_small = pygame.font.Font(None, 30)

game_over=False

round_time = 60
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            
            if event.key == pygame.K_RETURN and start_screen:
                start_screen = False
                
            if event.key==pygame.K_f and player1_attackcooldown==0:
                if abs(player1_x-player2_x)<80:
                    player2_health=player2_health-10
                    player1_attackcooldown=20
                    player1_attacking=True

            if event.key==pygame.K_RCTRL and player2_attackcooldown==0:
                if abs(player2_x-player1_x)<80:
                    player1_health=player1_health-10
                    player2_attackcooldown=20
                    player2_attacking=True

            if event.key == pygame.K_r and game_over:
                player1_health = 100
                player2_health = 100

                player1_x = 50
                player1_y = 600
                player2_x = 600
                player2_y = 600

                start_time=pygame.time.get_ticks()

                game_over = False
    
    keys=pygame.key.get_pressed()
    if not game_over:

        time_passed = (pygame.time.get_ticks() - start_time) // 1000
        time_left = round_time - time_passed

        if time_left <= 0:
            time_left = 0
            game_over = True
            
        if keys[pygame.K_d]:
            player1_x=player1_x+5
            player1_facing=1
        if keys[pygame.K_a]:
            player1_x=player1_x-5
            player1_facing=-1
        if player1_x<0:
            player1_x=0
        if player1_x>750:
            player1_x=750

        if keys[pygame.K_RIGHT]:
            player2_x=player2_x+5
            player2_facing=1
        if keys[pygame.K_LEFT]:
            player2_x=player2_x-5
            player2_facing=-1
        if player2_x<0:
            player2_x=0
        if player2_x>750:
            player2_x=750

        if keys[pygame.K_w] and player1_on_ground:
            player1_speed_y=-30
            player1_on_ground=False
        if keys[pygame.K_UP] and player2_on_ground:
            player2_speed_y=-30
            player2_on_ground=False

        player1_y=player1_y+player1_speed_y
        player1_speed_y=player1_speed_y+2
        player2_y=player2_y+player2_speed_y
        player2_speed_y=player2_speed_y+2

    
        if player1_attackcooldown>0:
            player1_attackcooldown=player1_attackcooldown-1
        if player2_attackcooldown>0:
            player2_attackcooldown=player2_attackcooldown-1
        if player1_attackcooldown == 0:
            player1_attacking = False
        if player2_attackcooldown == 0:
            player2_attacking = False

            
        if player1_y>=600:
            player1_y=600
            player1_speed_y=0
            player1_on_ground=True

        if player2_y>=600:
            player2_y=600
            player2_speed_y=0
            player2_on_ground=True


        if player1_facing == 1:
            player1_image = player1_image_right
        else:
            player1_image = player1_image_left

        if player2_facing == 1:
            player2_image = player2_image_right
        else:
            player2_image = player2_image_left

    if player1_health <= 0:
        game_over = True

    if player2_health <= 0:
        game_over = True
           
    screen.fill((135, 206, 235))
    pygame.draw.circle(screen, (255, 255, 255), (150, 100), 25)
    pygame.draw.circle(screen, (255, 255, 255), (180, 85), 35)
    pygame.draw.circle(screen, (255, 255, 255), (215, 100), 25)
    pygame.draw.circle(screen, (255, 255, 255), (250, 105), 20)
    pygame.draw.rect(screen, (255, 255, 255), (150, 100, 100, 25))

    pygame.draw.circle(screen, (255, 255, 255), (550, 150), 20)
    pygame.draw.circle(screen, (255, 255, 255), (580, 135), 30)
    pygame.draw.circle(screen, (255, 255, 255), (615, 150), 22)
    pygame.draw.circle(screen, (255, 255, 255), (645, 155), 17)
    pygame.draw.rect(screen, (255, 255, 255), (550, 150, 95, 20))

    pygame.draw.circle(screen, (255, 255, 255), (300, 230), 20)
    pygame.draw.circle(screen, (255, 255, 255), (330, 215), 30)
    pygame.draw.circle(screen, (255, 255, 255), (365, 230), 22)
    pygame.draw.rect(screen, (255, 255, 255), (300, 230, 65, 20))


    pygame.draw.rect(screen, (50, 120, 175), (0, 500, 800, 100))
    for y in range(520, 600, 20):
        for x in range(20, 800, 80):
            pygame.draw.line(screen, (80, 150, 195), (x, y), (x + 35, y), 2)
    for x in range(0, 800, 15):
        pygame.draw.line(screen, (120, 200, 100), (x, 600), (x + 3, 585), 3)
        pygame.draw.line(screen, (45, 110, 45), (x, 600), (x - 3, 585), 3)
    pygame.draw.rect(screen, (70, 140, 60), (0, 600, 800, 100))

    pygame.draw.polygon(screen, (100, 170, 100), [(0, 500), (150, 380), (300, 500)])
    pygame.draw.polygon(screen, (90, 160, 90), [(250, 500), (450, 350), (650, 500)])
    pygame.draw.polygon(screen, (100, 170, 100), [(550, 500), (700, 390), (800, 500)])

    if player1_attacking:
        pygame.draw.ellipse(screen, (255, 215, 0), (player1_x + 150, player1_y - 130, 50, 25))

    if player2_attacking:
        pygame.draw.ellipse(screen, (255, 215, 0), (player2_x - 50, player2_y - 130, 50, 25))
    
    screen.blit(player1_image,(player1_x, player1_y-180))
    screen.blit(player2_image,(player2_x, player2_y-160))
    
    pygame.draw.rect(screen,(200,50,100),(50,30,300,25))
    pygame.draw.rect(screen,(142,105,195),(50,30,player1_health*3,25))
    pygame.draw.rect(screen,(200,50,100),(450,30,300,25))
    pygame.draw.rect(screen,(80,170,100),(450,30,player2_health*3,25))
    clock.tick(25)
    
    player1_text = font_small.render("Player 1", True, (0, 0, 0))
    screen.blit(player1_text, (50, 5))

    player2_text = font_small.render("Player 2", True, (0, 0, 0))
    screen.blit(player2_text, (450, 5))

    timer_text = font_small.render(str(time_left), True, (0, 0, 0))
    screen.blit(timer_text, (390, 5))
    
    if game_over:
        if player1_health > player2_health:
            winner_text = font.render("Player 1 Wins!", True, (220, 100, 0))
        elif player2_health > player1_health:
            winner_text = font.render("Player 2 Wins!", True, (220, 100, 0))
        else:
            winner_text = font.render("Draw!", True, (220, 100, 0))
        screen.blit(winner_text, (270, 320))
        
    if game_over:
        restart_text = font_small.render("Press R to Restart", True, (0, 0, 0))
        screen.blit(restart_text, (320, 380))

    
    if start_screen:
        screen.fill((55, 35, 80))
        pygame.draw.rect(screen, (40, 25, 60), (180, 180, 440, 280))

        title_text = font.render("Duel Strife", True, (50, 205, 50))
        screen.blit(title_text, (300, 250))

        subtitle_text = font_small.render("2 Player Fighting Game", True, (100, 220, 220))
        screen.blit(subtitle_text, (300, 650))

        start_text = font_small.render("Press Enter to Start", True, (255,255,150))
        screen.blit(start_text, (300, 330))
    
    pygame.display.flip()

pygame.quit()
