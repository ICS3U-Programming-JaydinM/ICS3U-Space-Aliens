#!/usr/bin/env python3
# Made by Jaydin Madore
# Made on 2022-12-16


import ugame
import stage
import constants


# This function is the main game game_scene
def game_scene():
    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    #
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y -(2 * constants.SPRITE_SIZE))

    # set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # Set the Layers of all sprites, items show up in order
    game.layers = [ship] + [background]

    game.render_block()

    while True:
        # This code is for user input
        # It give you the ability to move the Sprite
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_RIGHT:
             if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                 ship.move(ship.x + 1, ship.y)
             else:
                 ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                 ship.move(ship.x - 1, ship.y)
            else:
                 ship.move(0, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 2)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 2)
        # The purpose of game.render_sprites([ship]) is to render it over and over again
        game.render_sprites([ship])
        # The purpose of game.tick() is to stop the PyBadge from refreshing the entire screen 60 times in a second.
        game.tick()


if __name__ == "__main__":
    game_scene()
