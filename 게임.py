import pygame
import random

pygame.init()

screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥피하기")

# FPS 클럭
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load('background.png')
# 캐릭터 이미지 불러오기 
character = pygame.image.load('character.png')
# 캐릭터 위치 정보 저장
c_size = character.get_rect().size # 사진 이미지의 가로세로 크기
c_width = c_size[0]
c_height = c_size[1]
c_x_pos = screen_width/2 - c_width/2
c_y_pos = screen_height - c_height/2

# 적 이미지 불러오기 
enemy = pygame.image.load('enemy.png')
# 적 위치 정보 저장
e_size = enemy.get_rect().size # 사진 이미지의 가로세로 크기
e_width = e_size[0]
e_height = e_size[1]
e_x_pos = random.randrange(0, screen_width - e_width)
e_y_pos = - e_height

# 위치의 변화량
to_x = 0
to_y = 0

# 속도
c_speed = 0.5
e_init_speed = 0.5
e_speed = e_init_speed

run = True
while run:
    dt = clock.tick(60) # 창의 초당 프레임 수
    #print("fps: %f" % clock.get_fps())
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        # 키가 눌러졌을 때
        if e.type == pygame.KEYDOWN:
            # character
            if e.key == pygame.K_LEFT:
                to_x -= c_speed # x 위치의 변화량
            elif e.key == pygame.K_RIGHT:
                to_x += c_speed # x 위치의 변화량
            elif e.key == pygame.K_UP:
                to_y -= c_speed # y 위치의 변화량
            elif e.key == pygame.K_DOWN:
                to_y += c_speed # y 위치의 변화량

            '''
            # enemy
            if e.key == pygame.K_a:
                e_to_x -= e_speed # x 위치의 변화량
            elif e.key == pygame.K_d:
                e_to_x += e_speed #
            elif e.key == pygame.K_w:
                e_to_y -= e_speed # y 위치의 변화량
            elif e.key == pygame.K_s:
                e_to_y += e_speed
            '''
                
        # 키를 뗐을 때
        if e.type == pygame.KEYUP:
            # character
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                to_x = 0
            elif e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                to_y = 0
            '''
            # enemy
            elif e.key == pygame.K_a or e.key == pygame.K_d:
                e_to_x = 0
            elif e.key == pygame.K_w or e.key == pygame.K_s:
                e_to_y = 0
            '''

    # character
    c_x_pos += to_x * dt
    c_y_pos += to_y * dt

    # falling enemy
    e_y_pos += e_speed * dt
    # 가속도
    e_speed += 0.01

    # character
    # (가로)화면 영역 밖으로 나가는 지 검사
    if c_x_pos < 0:
        c_x_pos = 0
    elif c_x_pos > screen_width - c_width:
        c_x_pos = screen_width - c_width
        
    # (세로)화면 영역 밖으로 나가는 지 검사
    if c_y_pos < 0:
        c_y_pos = 0
    elif c_y_pos > screen_height - c_height:
        c_y_pos = screen_height - c_height

    # enemy
    if e_y_pos >= screen_height:
        e_y_pos = - e_height
        e_x_pos = random.randrange(0, screen_width - e_width)
        # 속도 초기화
        e_speed = e_init_speed
    
    # 캐릭터의 사각형 정보
    c_rect = character.get_rect()
    c_rect.left = c_x_pos
    c_rect.top = c_y_pos
    # 적의 사각형 정보
    e_rect = enemy.get_rect()
    e_rect.left = e_x_pos
    e_rect.top = e_y_pos
    # 충돌 체크
    if c_rect.colliderect(e_rect):
        print("충돌함!")
        run = False
        
    # 배경을 띄우기
    screen.blit(background, (0,0))
    # 캐릭터를 창에 띄우기
    screen.blit(character, (c_x_pos, c_y_pos))
    # 적을 창 가운데 띄우기
    screen.blit(enemy, (e_x_pos, e_y_pos))
    
    # 변경된 창을 실제 화면에 띄우기
    pygame.display.update()

pygame.quit()
