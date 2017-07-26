# coding=UTF-8
# Commentaire : Cyrille Barrera -Responsable Projet LaserWave - 22 Juillet 2017 -

screen_size = [850,600]  # Tailler de l'écran de projection
space = 200
strings = 9
COLOR_ON =  0xFFFFFF
COLOR_OFF =  0x000000
STRING_SIZE = 40
# Liste du spectre coloré en hexadécimale : http://cloford.com/resources/colours/500col.htm
# 0xFF0000= R , 0x0000FF= B, 0x00FF00=R
colorshex = [0xFF0000,  0xFFAA00, 0xCCCC00, 0xAAFF00, 0x00FF00, 0x00FFAA, 0x00AAFF, 0x0044FF, 0x0000FF]

xy_center = [screen_size[0]/2,screen_size[1]/2]

harp_pos = [0,200]
DEFAULT_SPOKES = range(0,359,60)
DEFAULT_PLAYER_EXPLODE_COLOR = 0xFF0000
DEFAULT_SIDE_COUNT = 6
DREARRANGE_SIDES = .02

CRASH_SHAKE_MAX = 6
TDN_CRASH = 200
etherIP="192.168.1.5"

GAME_FS_QUIT = -1
GAME_FS_MENU = 0
GAME_FS_PLAY_PONG = 1
GAME_FS_GAMEOVER = 2
GAME_FS_CAL = 3
GAME_FS_HARP = 4
GAME_FS_ABSRAND = 5 

LASER_CENTER_X = 0
LASER_CENTER_Y = 1
LASER_ZOOM_X = -16
LASER_ZOOM_Y = -13
LASER_SIZE_X = 25000
LASER_SIZE_Y = 25000
LASER_ANGLE = 0

NO_BGM = False
#NO_BGM = True

ball_origin = [400,300,200]
text_pos = [300,500,200]
BALL_acc = 0.02
PADDLE_height = 100
PADDLE_width = 10
PADDLE3D_height = 100
PADDLE3D_width = 100
FACT3D = 2
FLIPS_lorigin = [10,300,0]
FLIPS_rorigin = [780,300,400]
flips_attraction = 0.007
