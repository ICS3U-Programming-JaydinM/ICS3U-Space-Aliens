#!/usr/bin/env python3

# Made by Jaydin Madore
# # Made on 2022-12-16


import ugame
import stage


# This function is the main game game_scene
def game_scene():
    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    #
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)
    # set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # Set the Layers of all sprites, items show up in order
    game.layers = [ship] + [background]

    game.render_block()

    while True:
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
