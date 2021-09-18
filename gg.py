from hach import Game

from characters import presets

if __name__ == '__main__':
    game = Game(
        thing_settings=presets.THING_SETTINGS,
        person_settings=presets.PERSON_SETTINGS,
        things_pre_list=presets.THINGS_PRE_LIST)