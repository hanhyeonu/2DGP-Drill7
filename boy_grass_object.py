from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(0, 400)
        self.frame = random.randint(0,7)

    def draw(self):
        self.image.clip_draw(100 * self.frame, 0, 100, 100, self.x, 90)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

class Ball:
    def __init__(self,size):        # size 를 인자로 하나 더 던져줄 수 있네.
        self.SIZE = size

        if size == 'small':
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

        self.x = random.randint(0, 800) # 0~ 800 랜덤하게 설정
        self.y = 599 # 599 고정.

    def draw(self):
        self.image.draw(self.x,self.y) # frame 없이 이동만 할거니까.

    def update(self):
        if self.SIZE == 'small':
            if self.y > 71:
                self.y -= random.randint(1,10)
        else:
            if self.y > 81:
                self.y -= random.randint(1,10)




def reset_world():
    global running
    running = True

    global world
    world = []
    grass = Grass()
    world.append(grass)

    global team
    team = [Boy() for i in range(11)]
    world += team

    global balls
    balls = [Ball('small') for i in range(10)] + [Ball('big') for i in range(10)] # 작은공, 큰공 객체를 하나의 class로 못만들까?


def update_world():
    for game_object in world:
        game_object.update()


def render_world():
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)


close_canvas()
