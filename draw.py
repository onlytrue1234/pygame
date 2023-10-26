import pygame

#GAME SCRREN SIZE
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

#DEFINE COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 파이게임 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("drawing")

# 스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 게임 종료 전까지 반복
done = False #게임이 진행 중인지 확인하는 변수
#done이 True라면 게임이 계속 진행 중이라는 의미

#게임 반복 구간
while not done: #게임이 진행되는 동안 계속 반복 작업을 하는 while 루프
    #이벤트 반복 구간
    for event in pygame.event.get():
        #어떤 이벤트가 발생했는지 확인
        if event.type == pygame.QUIT:
            # QUIT는 윈도우 창을 닫을 때 발생하는 이벤트
            #창이 닫히는 이벤트가 발생했다면
            done = True # 반복을 중단시켜 게임 종료

    #게임 로직 구간

    #화면 삭제구간

    #스크린 채우기
    screen.fill(WHITE)

    # 화면 그리기 구간
    pygame.draw.line(screen, RED, [50, 50],[500, 50],4)
    pygame.draw.line(screen, GREEN, [50, 100], [500, 100], 4)
    pygame.draw.line(screen, BLUE, [50, 150], [500, 150], 4)
    #사각형 그리기
    pygame.draw.rect(screen,RED, [50, 200, 150, 150], 4)
    # 다각형 그리기
    pygame.draw.polygon(screen, GREEN, [[350,200], [250,350], [450,350]], 4)
    # 원형 그리기
    pygame.draw.circle(screen,BLUE,[150,450], 60, 4)
    #타원 그리기
    pygame.draw.ellipse(screen, BLUE,[250, 400, 200, 100], 0)
    # 폰트 선택(폰트, 크기,두껍게,이탤릭)
    font = pygame.font.SysFont('FixedSYs',40, True, False)
    #안티 얼리언스를 적용하고 검은색 문자열 렌더링
    text = font.render("Hello pygame",True,BLACK)

    screen.blit(text, [200, 600])
    # 화면 업데이트
    pygame.display.flip()
    #초당 60 프레임으로 업데이트
    clock.tick(60)

# Pygame 종료
pygame.quit()


