import pygame  # 模块pygame 包含开发游戏所需的功能。
import sys  # 使用模块sys 中的工具来退出游戏


class Test:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("TesT")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:  # 键盘按下事件
                    print(event.key)
            pygame.display.flip()


if __name__ == '__main__':
    ts = Test()
    ts.run_game()
