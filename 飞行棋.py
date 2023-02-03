import pygame
import random
import time

pygame.init()
screen_width = 1050
screen_height = 566
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill((255, 255, 255))
pygame.display.set_caption("Flight chess")
bgimg = pygame.image.load("image/bgimg.png")

# 对应点的坐标，1-52为从左上方开始绕一圈（坐标x,坐标y,格子颜色，跳跃的个数）
dic1 = {1: [255, 50, 3, 4],
        2: [290, 45, 4, 4],
        3: [325, 45, 1, 4],
        4: [355, 45, 2, 4],
        5: [385, 40, 3, 4],
        6: [420, 40, 4, 4],
        7: [450, 50, 1, 16],
        8: [465, 85, 2, 4],
        9: [465, 115, 3, 4],
        10: [450, 145, 4, 4],
        11: [480, 170, 1, 12],
        12: [510, 160, 2, 4],
        13: [545, 160, 3, 4],
        14: [580, 170, 4, 4],
        15: [585, 200, 1, 4],
        16: [585, 230, 2, 4],
        17: [585, 260, 3, 4],
        18: [585, 290, 4, 4],
        19: [585, 320, 1, 4],
        20: [580, 355, 2, 16],
        21: [545, 365, 3, 4],
        22: [510, 365, 4, 4],
        23: [480, 350, 1, 4],
        24: [455, 375, 2, 12],
        25: [465, 405, 3, 4],
        26: [465, 435, 4, 4],
        27: [455, 470, 1, 4],
        28: [420, 480, 2, 4],
        29: [390, 480, 3, 4],
        30: [355, 480, 4, 4],
        31: [325, 480, 1, 4],
        32: [295, 480, 2, 4],
        33: [260, 470, 3, 16],
        34: [250, 435, 4, 4],
        35: [250, 405, 1, 4],
        36: [260, 375, 2, 4],
        37: [235, 355, 3, 12],
        38: [200, 365, 4, 4],
        39: [170, 365, 1, 4],
        40: [135, 350, 2, 4],
        41: [125, 320, 3, 4],
        42: [125, 290, 4, 4],
        43: [125, 260, 1, 4],
        44: [125, 230, 2, 4],
        45: [125, 200, 3, 4],
        46: [135, 170, 4, 16],
        47: [170, 160, 1, 4],
        48: [200, 160, 2, 4],
        49: [230, 165, 3, 4],
        50: [260, 145, 4, 12],
        51: [245, 115, 1, 4],
        52: [245, 85, 2, 4],
        # 黄色基地
        53: [125, 45],
        54: [185, 45],
        55: [125, 100],
        56: [185, 100],
        57: [110, 150],
        # 绿色基地
        58: [525, 45],
        59: [585, 45],
        60: [525, 100],
        61: [585, 100],
        62: [475, 35],
        # 蓝色基地
        63: [525, 420],
        64: [585, 420],
        65: [525, 480],
        66: [585, 480],
        67: [600, 375],
        # 红色基地
        68: [125, 420],
        69: [185, 420],
        70: [125, 475],
        71: [185, 475],
        72: [235, 490],
        # 绿色终点圈
        73: [355, 45],
        74: [355, 85],
        75: [355, 115],
        76: [355, 150],
        77: [355, 175],
        78: [355, 205],
        79: [355, 235],
        # 蓝色终点圈
        80: [585, 260],
        81: [545, 260],
        82: [510, 260],
        83: [475, 260],
        84: [445, 260],
        85: [415, 260],
        86: [385, 260],
        # 红色终点圈
        87: [355, 480],
        88: [355, 440],
        89: [355, 410],
        90: [355, 375],
        91: [355, 350],
        92: [355, 320],
        93: [355, 290],
        # 黄色终点圈
        94: [125, 260],
        95: [165, 260],
        96: [200, 260],
        97: [235, 260],
        98: [265, 260],
        99: [295, 260],
        100: [325, 260],
        # 黄色获胜区域
        101: [850, 250],
        102: [890, 250],
        103: [930, 250],
        104: [970, 250],
        # 绿色获胜区域
        105: [850, 300],
        106: [890, 300],
        107: [930, 300],
        108: [970, 300],
        # 蓝色获胜区域
        109: [850, 350],
        110: [890, 350],
        111: [930, 350],
        112: [970, 350],
        # 红色获胜区域
        113: [850, 400],
        114: [890, 400],
        115: [930, 400],
        116: [970, 400],
        }


class qizi:
    def __init__(self, _type, _pos, _img):
        self.type = _type  # 飞机类型 1:黄色 2：绿色 3：蓝色 4：红色
        self.position = _pos  # 飞机位置
        self.img = pygame.image.load(_img)  # 图片位置
        self.fly = False  # 是否已经起飞
        self.fina = False  # 是否处于终点圈
        self.fina_flag = [43, 4, 17, 30]
        self.direction = True
        self.list1 = [94, 73, 80, 87]  # 终点圈起点位置
        self.list2 = [100, 79, 86, 93]  # 终点位置
        self.win = False

    def move(self):
        if not self.fina:  # 不在终点圈
            if self.position == 52:
                self.position = 0
            self.position += 1
            if self.position == self.fina_flag[self.type - 1]:
                self.fina = True
        else:  # 在终点圈
            if self.position < 60:
                self.position = self.list1[self.type - 1]
            if self.direction:
                self.position += 1
            else:
                self.position -= 1
            if self.position == self.list2[self.type - 1]:
                self.direction = False


# 定义类
yellow = [qizi(1, 53, "image/yellow1.png"),
          qizi(1, 54, "image/yellow2.png"),
          qizi(1, 55, "image/yellow3.png"),
          qizi(1, 56, "image/yellow4.png")]
green = [qizi(2, 58, "image/green1.png"),
         qizi(2, 59, "image/green2.png"),
         qizi(2, 60, "image/green3.png"),
         qizi(2, 61, "image/green4.png")]
blue = [qizi(3, 63, "image/blue1.png"),
        qizi(3, 64, "image/blue2.png"),
        qizi(3, 65, "image/blue3.png"),
        qizi(3, 66, "image/blue4.png")]
red = [qizi(4, 68, "image/red1.png"),
       qizi(4, 69, "image/red1.png"),
       qizi(4, 70, "image/red1.png"),
       qizi(4, 71, "image/red1.png")]

players_init_pos = [[53, 54, 55, 56], [58, 59, 60, 61], [63, 64, 65, 66], [68, 69, 70, 71]]
players_score_pos = [[101, 102, 103, 104], [105, 106, 107, 108], [109, 110, 111, 112], [113, 114, 115, 116]]
n = 0
# 文字
font_name = pygame.font.match_font('fangsong')  # 2.获得字体文件
font = pygame.font.Font(font_name, 50)  # 1.获取font对象（需要字体文件）
text1 = font.render("空格摇骰子", True, (0, 0, 0))


text_color = [font.render("黄色", True, (255, 255, 0)),
              font.render("绿色", True, (0, 255, 0)),
              font.render("蓝色", True, (0, 0, 255)),
              font.render("红色", True, (255, 0, 0))]

inital_pos = [57, 62, 67, 72]
begin_pos = [46, 7, 20, 33]
players = [yellow, green, blue, red]
running = True


# 刷新页面图片
def show_img():
    screen.blit(bgimg, (0, 0))
    screen.blit(text1, (750, 50))
    screen.blit(text_color[0], (750, 250))
    screen.blit(text_color[1], (750, 300))
    screen.blit(text_color[2], (750, 350))
    screen.blit(text_color[3], (750, 400))
    for i in range(4):
        screen.blit(yellow[i].img, (dic1[yellow[i].position][0], dic1[yellow[i].position][1]))
        screen.blit(green[i].img, (dic1[green[i].position][0], dic1[green[i].position][1]))
        screen.blit(blue[i].img, (dic1[blue[i].position][0], dic1[blue[i].position][1]))
        screen.blit(red[i].img, (dic1[red[i].position][0], dic1[red[i].position][1]))

    pygame.display.update()
    time.sleep(0.5)


# 等待空格输入
def wait_space(plane_now):
    global n, text1
    text1 = font.render("空格摇骰子", True, (0, 0, 0))
    show_img()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                n = random.randint(1, 6)
                text = font.render(str(n), True, (0, 0, 0))  # 显示摇到的点数
                screen.fill((255, 255, 255))
                screen.blit(text, (850, 150))
                if plane_now == 0:
                    text1 = font.render("黄色选择飞机", True, (255, 255, 0))
                elif plane_now == 1:
                    text1 = font.render("绿色选择飞机", True, (0, 255, 0))
                elif plane_now == 2:
                    text1 = font.render("蓝色选择飞机", True, (0, 0, 255))
                elif plane_now == 3:
                    text1 = font.render("红色选择飞机", True, (255, 0, 0))
                show_img()
                waiting = False


# 等待输入飞机序号
def wait_num():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                text = font.render("1号飞机", True, (0, 0, 0))  
                screen.blit(text, (800, 200))
                return 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                text = font.render("2号飞机", True, (0, 0, 0))  
                screen.blit(text, (800, 200))
                return 2
            if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                text = font.render("3号飞机", True, (0, 0, 0))  
                screen.blit(text, (800, 200))
                return 3
            if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                text = font.render("4号飞机", True, (0, 0, 0))  
                screen.blit(text, (800, 200))
                return 4


# 移动
def yidong(x, y=0):
    if players[x][y].win:
        wait_num()
        num = wait_num()
        yidong(player, num - 1)
        return
    players[x][y].direction = True  # 设置方向（终点圈时使用）
    if not players[x][y].fly:  # 还未起飞
        players[x][y].position = inital_pos[x]
        players[x][y].fly = True
    for i in range(n):  # 设置初始位置
        if players[x][y].position == inital_pos[players[x][y].type - 1]:
            players[x][y].position = begin_pos[players[x][y].type - 1]
            show_img()
        else:
            players[x][y].move()
            show_img()

    if not players[x][y].fina and dic1[players[x][y].position][2] == players[x][y].type:  # 是否跳跃
        for i in range(dic1[players[x][y].position][3]):
            players[x][y].move()
            show_img()

    for i in range(4):  # 是否撞到其他飞机
        for j in range(4):
            if i != x and players[i][j].position == players[x][y].position:
                players[i][j].position = players_init_pos[i][j]
                players[i][j].fly = False
                players[i][j].fina = False
                show_img()

    if players[x][y].position == players[x][y].list2[x]:  # 是否获胜
        players[x][y].position = players_score_pos[x][y]
        players[x][y].win = True
        show_img()


if __name__ == '__main__':
    while running:
        show_img()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        for player in range(4):
            screen.fill((255, 255, 255))
            wait_space(player)
            num = wait_num()
            yidong(player, num - 1)
