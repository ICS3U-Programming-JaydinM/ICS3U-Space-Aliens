#!/usr/bin/env python3

# Made by Jaydin Madore
# Made on 2022-12-16

import ugame
import stage

import constants


def menu_scene():
    # this function is the main menu scene

     # image banks for CircuitPython
    image_bank_ms_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

        # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20,10)
    text1.text("MT Game Studio")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

   # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_ms_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    
    # set the layers of all sprites, items show up in order
    game.layers = text + [background]
    
    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # call game scene
        if keys & ugame.K_START != 0:
            game_scene()
    
        # redraw Sprites
        game.tick()

def game_scene():

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # button that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

     # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

     # image at index 5 on (75, 66) on the screen
    ship = stage.Sprite(image_bank_sprites, 4, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

 # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    
    # set the layers of all sprites, items show up in order
    game.layers = [ship] + [background]
    
    # render all sprites
    # most likely you will only render the background once per game scene
    game.render_block()


    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button to fire
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
                
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        # button functions
        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
            # move the ship to the right 
            # if it hits the border it will wrap to the other side of the screen
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 2, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_LEFT != 0:
            # move ship to the left
            # if it hits the border it will wrap to the other side of the screen
            if ship.x >= 0:
                ship.move(ship.x - 2, ship.y)
            else:  
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
        # redraw Sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    menu_scene()