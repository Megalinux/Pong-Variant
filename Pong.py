import pygame
import random
from pygame.locals import *

# Initialize PyGame
pygame.init()

#Sound management
#Sound of the left paddle when touching the ball
hit_sound_paddle_left = pygame.mixer.Sound('Pong.mp3')
#sound of the left paddle when touching the ball
hit_sound_paddle_right = pygame.mixer.Sound('Ping.mp3')
#sound of victory
hit_victory = pygame.mixer.Sound('vict1.mp3')
#paddle lengthening sound
hit_paddle_allungamento = pygame.mixer.Sound('bonus2.wav')
#Sound of the ball comes out of the screen to the right or left
out_ball = pygame.mixer.Sound('outbordo.wav')
#Wall collision sound
hit_wall = pygame.mixer.Sound('hit_wall.wav')
#Sound of wall appearing
see_wall = pygame.mixer.Sound('comparsa_wall1.wav')
#Start music
hit_start = pygame.mixer.Sound('start_music2.wav')


last_hit_paddle = None  # Initially, no paddle hit the ball
is_vs_computer = False  # Set the default to two human players

# Set the size of the game window
width, height = 640, 480
screen_size = (640,480)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pong Variant by Grando Ruggero")

#Creation of the list used for the center wall
wall_rects = []

# START button settings
button_color = (50, 205, 50)  # Green Color
button_width, button_height = 200, 80
button_rect = pygame.Rect((width - button_width) / 2, (height - button_height) / 2, button_width, button_height)
button_font = pygame.font.SysFont(None, 40)
button_text = button_font.render('START', True, (255, 255, 255))  # White text
button_text_rect = button_text.get_rect(center=button_rect.center)
# VS COMPUTER settings
button_vs_computer_rect = pygame.Rect((width - button_width) / 2, (height - button_height) / 2 + 100, button_width, button_height)
button_vs_computer_text = button_font.render('VS COMPUTER', True, (255, 255, 255))  # White text
button_vs_computer_text_rect = button_vs_computer_text.get_rect(center=button_vs_computer_rect.center)

#Main screen title
title_font_size = 80  # Choose the font size for the title
title_font = pygame.font.SysFont('centurygothic', title_font_size)
title_text = title_font.render('PONG VARIANT', True, (255, 255, 255))  # White text
title_text_rect = title_text.get_rect(center=(width // 2, 50))  # Place the text in the center, 50 pixels from the top


# Player scores
left_score = 0
right_score = 0


# Font to display the score
font_size = 56  # Change the font size here
font = pygame.font.SysFont(None, font_size)

# Font for victory message
victory_font_size = 70  # Change the font size for the victory message
victory_font = pygame.font.SysFont(None, victory_font_size)

# Define the colors
bg_color = (0, 0, 0)
paddle_color = (0, 200, 113)
paddle_color_left = (0, 200, 113)
paddle_color_right = (0, 200, 113)
wall_color = (255,0,0)
last_hit = None

# Set the size and position of the paddles
paddle_width, paddle_height = 10, 60
left_paddle = pygame.Rect(30, height/2 - 30, paddle_width, paddle_height)  # Left Paddle 
right_paddle = pygame.Rect(width - 40, height/2 - 30, paddle_width, paddle_height)  # Right Paddle 

paddle_speed = 5
left_paddle_pos = pygame.Rect(50, height/2 - paddle_height/2, paddle_width, paddle_height)
right_paddle_pos = pygame.Rect(width - 50 - paddle_width, height/2 - paddle_height/2, paddle_width, paddle_height)

# Set the speed and direction of the ball
ball_x_speed = 3
ball_y_speed = 3
ball_pos = pygame.Rect(width/2, height/2, 10, 10)

# Bonus configuration
bonus_font = pygame.font.SysFont(None, 40)  # Change the font size as you like
bonus_text = bonus_font.render('BONUS', True, (255, 255, 255))  # Change the color as you like
bonus_text_width, bonus_text_height = bonus_text.get_size()
bonus_pos = pygame.Rect(random.randint(100, width - 100), random.randint(100, height - 100), bonus_text_width, bonus_text_height)
angle = 0  # Initial rotation angle
bonus_active = True

def create_center_wall():
    global wall_rects
    wall_rects = []
    wall_width = 5
    rect_height = 30
    gap_height = 20
    y = 0
    see_wall.play()
    
    while y < height:
        if random.random() < 0.5:  # 50% chance of creating a gap
            y += gap_height
        else:
            rect = pygame.Rect(width // 2 - wall_width // 2, y, wall_width, rect_height)
            wall_rects.append(rect)
            y += rect_height + gap_height


# Function to update the position of the paddles
def update_paddle(paddle_pos, up_key, down_key, is_computer=False):
    if is_computer:
        if ball_pos.centery > paddle_pos.centery and paddle_pos.bottom < height:
            paddle_pos.y += paddle_speed
        elif ball_pos.centery < paddle_pos.centery and paddle_pos.top > 0:
            paddle_pos.y -= paddle_speed
    else:
        keys = pygame.key.get_pressed()
        if keys[up_key] and paddle_pos.top > 0:
            paddle_pos.y -= paddle_speed
        if keys[down_key] and paddle_pos.bottom < height:
            paddle_pos.y += paddle_speed

        
# Upload the background image
background = pygame.image.load("background1.png")
background = pygame.transform.scale(background,screen_size)


# Function to draw the background image
def draw_background():
    screen.blit(background, (0, 0))
    
# Function to reset game variables
def reset_game():
    global left_score, right_score, ball_pos, ball_x_speed,bonus_active, left_paddle, right_paddle, height, last_hit_paddle, left_paddle_pos,right_paddle_pos,paddle_color,paddle_color_right,paddle_color_left  # o qualunque sia l'altezza originale
    right_paddle.height = 60  # o qualunque sia l'altezza originale

    left_score = 0
    right_score = 0
    ball_pos = pygame.Rect(width/2, height/2, 10, 10)
    ball_x_speed = 3
    ball_y_speed = 3
    # Decidi se il bonus è attivo in questo round
    bonus_active = random.choice([True, False])
    
    left_paddle_pos.height = 60
    right_paddle_pos.height = 60 
    
    paddle_color_left = (0, 200, 113)
    paddle_color_right = (0,200,113)
    
    last_hit_paddle = None
    
    if random.randint(1, 2) == 1:
        create_center_wall()

    
# Function to draw the score
def draw_score():
    score_color = (0, 200, 113)  # Green color
    left_text = font.render(str(left_score), True, score_color)
    right_text = font.render(str(right_score), True, score_color)

    screen.blit(left_text, (width/4 - left_text.get_width()/2, 10))
    screen.blit(right_text, (3*width/4 - right_text.get_width()/2, 10))
    
def draw_start_button():
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_text_rect.topleft)
    pygame.draw.rect(screen, button_color, button_vs_computer_rect)
    screen.blit(button_vs_computer_text, button_vs_computer_text_rect.topleft)
    
# Function to draw the central wall    
def draw_center_wall():
    for rect in wall_rects:
        pygame.draw.rect(screen, wall_color, rect)
        
# Function to manage the collision of the ball with the paddle
def ball_paddle_collision(ball, paddle, is_left_paddle):
    if ball.colliderect(paddle):
        # Calculate the distance between the center of the ball and the center of the paddle
        distance_from_center = abs(ball.centery - paddle.centery)
        
        #Calculate the ratio of the distance from the center to half the height of the paddle
        collision_position_ratio = distance_from_center / (paddle.height / 2)
        
        # Calculate the ball's new speed based on where it hit the paddle
        speed_multiplier = 1 + 0.5 * collision_position_ratio  # You can change the 0.5 to make the effect more or less pronounced
        
        global ball_x_speed, ball_y_speed
        ball_x_speed = -ball_x_speed * speed_multiplier  # Reverses the x direction of the ball and changes the speed
        ball_y_speed += collision_position_ratio * ball_y_speed  # Change the y speed of the ball
        
        global last_hit

        if is_left_paddle:
            hit_sound_paddle_left.play()
            last_hit = "left"
        else:
            hit_sound_paddle_right.play()
            last_hit = "right"
        
# Function that manages pressing the "VS COMPUTER" button       
def is_vs_computer_button_clicked():
    mouse_pos = pygame.mouse.get_pos()
    return button_vs_computer_rect.collidepoint(mouse_pos)
        
# Function that manages the pressing of the "START" button
def is_button_clicked():
    mouse_pos = pygame.mouse.get_pos()
    return button_rect.collidepoint(mouse_pos)
    
#Victory message function
def draw_victory_message(winner):
    victory_color = (255, 0, 0)  # Red color for victory message
    if winner == "left":
        message = "Player 1 won!"
        hit_victory.play()
    else:
        message = "Player 2 won!"
        hit_victory.play()
    victory_text = victory_font.render(message, True, victory_color)
    screen.blit(victory_text, (width/2 - victory_text.get_width()/2, height/2 - victory_text.get_height()/2))
    
def start_screen():
    global is_vs_computer
    while True:
        hit_start.play()
        for event in pygame.event.get():
            
            if event.type == QUIT:
                hit_start.stop()
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if is_button_clicked():
                    hit_start.stop()
                    return
                if is_vs_computer_button_clicked():
                    is_vs_computer = True
                    hit_start.stop()
                    
                    return

        screen.fill(bg_color)
        screen.blit(title_text, title_text_rect.topleft)  # Draw the title text
      
        draw_start_button()
        pygame.display.flip()
        
        
# Mostra la schermata iniziale
start_screen()            
    

# Ciclo principale del gioco
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    
     
    # Gestione degli eventi
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    
    # Aggiorna la posizione dei paddle
    update_paddle(left_paddle_pos, K_w, K_s)
    update_paddle(right_paddle_pos, K_UP, K_DOWN, is_vs_computer)


    # Aggiorna la posizione della palla
    ball_pos.x += ball_x_speed
    ball_pos.y += ball_y_speed

    # Rimbalzo della palla sui bordi verticali
    if ball_pos.top <= 0 or ball_pos.bottom >= height:
        ball_y_speed = -ball_y_speed
        

    # Collisione della palla con i paddle
    ball_paddle_collision(ball_pos, left_paddle_pos, is_left_paddle=True)
    ball_paddle_collision(ball_pos, right_paddle_pos, is_left_paddle=False)
    
  
    
    # Aggiorna il punteggio se la palla va oltre i bordi orizzontali
    if ball_pos.left <= 0:
        right_score += 1
        ball_pos.x = width/2  # Reset della posizione della palla
        ball_x_speed = -ball_x_speed  # Reset della direzione della palla
        ball_x_speed = 2  # Reset della velocità della palla
        ball_y_speed = random.choice([-2, 2])  # Reset della velocità della palla con direzione casuale
        if random.randint(1, 2) == 1:
            create_center_wall()
        out_ball.play()


    if ball_pos.right >= width:
        left_score += 1
        ball_pos.x = width/2
        ball_x_speed = -ball_x_speed
        ball_x_speed = 2  # Reset della velocità della palla
        ball_y_speed = random.choice([-2, 2])  # Reset della velocità della palla con direzione casuale
        out_ball.play()
    
    for rect in wall_rects:
        if ball_pos.colliderect(rect):
            ball_x_speed = -ball_x_speed  # la palla rimbalza quando colpisce il muro centrale
            hit_wall.play()
            break 
    

    # Pulisci lo schermo
    screen.fill(bg_color)
    
    if bonus_active:
        # Ruotare il Testo
        angle += 1  # Aumenta l'angolo ad ogni frame
        rotated_bonus_text = pygame.transform.rotate(bonus_text, angle)
        
        rect = rotated_bonus_text.get_rect(center=bonus_pos.center)
        screen.blit(rotated_bonus_text, rect.topleft)  
        
        
    if bonus_active and ball_pos.colliderect(bonus_pos):
        print('la palla ha colpito il bonus')
        if last_hit is not None:
            if last_hit == "left":
                print('raddopia il paddle left')
                left_paddle_pos.height = 120
                paddle_color_left = (255,0,0)
                hit_paddle_allungamento.play()
   
            else:
                print('raddoppia il paddle right')
                
                right_paddle_pos.height = 120
                paddle_color_right = (255,0,0)
                hit_paddle_allungamento.play()
        
    
        bonus_active = False 

    
    #disegna il background - rimosso per ora
    #draw_background()   
    draw_score()

    # Disegna i paddle e la palla
    pygame.draw.rect(screen, paddle_color_left, left_paddle_pos)
    pygame.draw.rect(screen, paddle_color_right, right_paddle_pos)
    pygame.draw.ellipse(screen, paddle_color, ball_pos)
    
     
    # Controlla se uno dei giocatori ha vinto
    if left_score == 3:
        draw_victory_message("left")
        pygame.display.flip()
        pygame.time.wait(3000)  # Mostra il messaggio per 3 secondi
        reset_game()
        start_screen()
    elif right_score == 3:
        draw_victory_message("right")
        pygame.display.flip()
        pygame.time.wait(3000)  # Mostra il messaggio per 3 secondi
        reset_game()
        start_screen()

    # disegna il muro centrale
    draw_center_wall()
    # Aggiorna la schermata
    pygame.display.flip()

# Chiudi Pygame
pygame.quit()
