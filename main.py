from classes import Game

import config

if __name__ == '__main__':
    game = Game(
        thing_settings=config.THING_SETTINGS,
        person_settings=config.PERSON_SETTINGS,
        general_settings=config.GENERAL_SETTINGS,
        things_pre_list=config.presets.THINGS_PRE_LIST,
        persons_pre_list=config.presets.PERSONS_PRE_LIST,
        persons_skills=config.presets.PERSONS_SKILLS)
