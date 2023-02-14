"""
*insane flappy bird like osu
*Flosy

Todo:
//bottom pipes
//design sprites
//top pipes
//flosy bird charcther
//pipe
flopy gravity
pipe collision
flopy collision
collision detection
sprites
"""

import arcade
import random

"""defining"""

SCREEN_WIDTH = 1920

SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Flosy"

xlist = [40, 100, 120, 160, 320, 480, 640, 800, 960, 1120, 1280, 1440, 1600, 1760, 1920]
hlist = [100, 200, 300, 400, 500]

self.player_list = arcade.SpriteList(use_spatial_hash=True)
self.wall_list = arcade.SpriteList()

"""end of defining"""

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()

#things
for i in range(10):
    #*random x and y coordinates
    x = random.choice(xlist)
    y = 100
    w = 100
    h = random.choice(hlist)
    arcade.draw_rectangle_filled(x, y, w, h, arcade.color.BRITISH_RACING_GREEN)
    print(x, y)
    
while True:
    if key == arcade.key.SPACE or key == arcade.key.W or key == arcade.key.UP:
        if self.pysics_engine.can_jump():
            self.playerSprite.change_y = playerJumpSpeed

arcade.finish_render()
arcade.run()