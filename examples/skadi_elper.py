from gacha_elper.elper import Elper as Elp
from gacha_elper.elper import Point

buttons = {
    'home1': Point(215, 30),
    'home2': Point(73, 230),
    'back': Point(70, 35),
    'combat_skadi': Point(927, 255),
    'operation_map': Point(766, 385),
    'gt_5': Point(682, 376),
    'gt_6': Point(774, 282),
    'auto_deploy': Point(919, 616),
    'start_battle1': Point(913, 666),
    'start_battle2': Point(888, 475)
}

def start():
    if not Elp.find('combat'):
        print('going home')
        Elp.tap(buttons['home1'])
        Elp.tap(buttons['home2'])
    Elp.tap(buttons['combat_skadi'])
    Elp.wait(1.5)
    Elp.tap(buttons['operation_map'])
    gt_5 = True
    gt_5_count = 0
    while True:
        current_map = buttons['gt_5'] if gt_5 else buttons['gt_6']
        Elp.tap(current_map)
        if not Elp.find('auto_enabled'):
            Elp.tap(buttons['auto_deploy'])
        Elp.tap(buttons['start_battle1'], 2.5)
        Elp.tap(buttons['start_battle2'])
        Elp.wait(35)
        while not Elp.find('trust'):
            Elp.wait(5)
        Elp.tap(Point(512, 512))
        Elp.wait(7.5)
        Elp.tap(buttons['back'])
        if gt_5:
            gt_5_count += 1
        if gt_5 and gt_5_count == 2:
            gt_5 = not gt_5
            gt_5_count = 0
        elif not gt_5:
            gt_5 = not gt_5

