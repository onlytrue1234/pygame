import pygame

#GAME SCRREN SIZE
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#DEFINE COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 파이게임 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("pygame")

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

    #화면 업데이트
    pygame.display.flip()

    #초당 60 프레임으로 업데이트
    clock.tick(60)

# Pygame 종료
pygame.quit()

