import ctypes


user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

ScreenWidth, ScreenHeight = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

WIDTH = int(ScreenWidth * 0.60)
HEIGHT = int(ScreenHeight * 0.75)

start_pos_1 = (int(WIDTH * 0.30), int(HEIGHT * 0.5))
start_pos_2 = (int(WIDTH * 0.60), int(HEIGHT * 0.5))

PlayerWidth = int(WIDTH * 0.06)
PlayerHeight = int(HEIGHT * 0.075)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
