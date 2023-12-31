import time
# import os
import sys

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def dungeon_start(cla, dungeon):
    try:
        print("dungeon_start")
    except Exception as e:
        print(e)
        return  0

def season_dungeon_in_mobius_ing(cla, dungeon):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_add
    try:
        print("season_dungeon_in_mobius_ing")
        ing_ = True
        ing_count = 0
        while ing_ is True:
            ing_count += 1
            if ing_count > 10:
                ing_ = False
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\mobius_ing.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(780, 70, 835, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                ing_count = 0
                print("모비우스 던전 중...")
                time.sleep(2)
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\sungwoon_fail.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(430, 270, 540, 360, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("season_dungeon_in_mobius_ing : failed", imgs_)
                    myQuest_play_add(cla, dungeon)
                    ing_ = False
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\dark_exit.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 1000, 800, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("뫼비우스 나가기")
                            click_pos_2(555, 1015, cla)
                            break
                        time.sleep(0.2)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\mobius_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("season_dungeon_in_mobius_ing : mobius_title", imgs_)
                        myQuest_play_add(cla, dungeon)
                        ing_ = False
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\season\\clear.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(430, 270, 540, 360, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("season_dungeon_in_mobius_ing : clear", imgs_)
                            ing_count = 0
                            click_pos_2(555, 1015, cla)



                print("모비우스 체크 카운터 10... => ", ing_count)
                time.sleep(1)

            print("모비우스 중...??? 카운터 10", ing_count)
            time.sleep(1)


    except Exception as e:
        print(e)
        return 0

def season_dungeon_in_mobius(cla, dungeon):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg, mouse_move_cpp
    from action_ares import menu_open, loading_ares
    from schedule import myQuest_play_add
    try:
        print("season_dungeon_in_mobius")

        where_dungeon = dungeon.split("_")

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\mobius_ing.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(780, 70, 835, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            season_dungeon_in_mobius_ing(cla, dungeon)
        else:

            sd_in_ = False
            sd_in_count = 0
            while sd_in_ is False:
                sd_in_count += 1
                if sd_in_count > 4:
                    sd_in_ = True
                    myQuest_play_add(cla, dungeon)
                    time.sleep(0.2)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\mobius_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(820, 1015, cla)
                    # 로딩
                    for i in range(20):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\alrim.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 450, 500, 500, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(535, 585, cla)

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            sd_in_ = True
                            loading_ares(cla)
                            # ing
                            season_dungeon_in_mobius_ing(cla, dungeon)
                            break
                        time.sleep(0.7)




                else:
                    menu_open(cla)
                    click_pos_2(80, 160, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\hondon_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(310, 190, cla)
                            for z in range(10):
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\mobius_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.5)
                            break
                        time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0

# 어비스
def season_dungeon_in_ubis_ing(cla, dungeon):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_add
    try:
        print("season_dungeon_in_ubis_ing")
        ing_ = True
        ing_count = 0
        while ing_ is True:
            ing_count += 1
            if ing_count > 10:
                ing_ = False
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\ubis_ing.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(780, 70, 835, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                ing_count = 0
                print("어비스 던전 중...")
                time.sleep(2)
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\ubis_ing2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(780, 90, 835, 120, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    ing_count = 0
                    print("어비스 던전 중...2")
                    time.sleep(2)
                else:

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\sungwoon_fail.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(430, 270, 540, 360, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("season_dungeon_in_ubis_ing : failed", imgs_)
                        myQuest_play_add(cla, dungeon)
                        ing_ = False

                        for i in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\dark_exit.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 1000, 800, 1040, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("어비스 나가기")
                                click_pos_2(555, 1015, cla)
                                break
                            time.sleep(0.2)

                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\ubis_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("season_dungeon_in_ubis_ing : ubis_title", imgs_)
                            myQuest_play_add(cla, dungeon)
                            ing_ = False
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\sungwoon_clear.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 270, 540, 360, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("season_dungeon_in_ubis_ing : clear", imgs_)
                                click_pos_2(555, 1015, cla)
                                ing_count = 0



                    print("어비스 체크 카운터 10... => ", ing_count)
                time.sleep(1)

            print("어비스 중...??? 카운터 10", ing_count)
            time.sleep(1)



    except Exception as e:
        print(e)
        return 0

def season_dungeon_in_ubis(cla, dungeon):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg, mouse_move_cpp
    from action_ares import menu_open, loading_ares
    from schedule import myQuest_play_add
    try:
        print("season_dungeon_in_ubis")

        where_dungeon = dungeon.split("_")

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\ubis_ing.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(780, 70, 835, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            season_dungeon_in_ubis_ing(cla, dungeon)
        else:

            sd_in_ = False
            sd_in_count = 0
            while sd_in_ is False:
                sd_in_count += 1
                if sd_in_count > 4:
                    sd_in_ = True
                    myQuest_play_add(cla, dungeon)
                    time.sleep(0.2)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\ubis_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(820, 1015, cla)
                    # 로딩
                    for i in range(20):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\alrim.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 450, 500, 500, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(535, 585, cla)

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            loading_ares(cla)
                            # ing
                            season_dungeon_in_ubis_ing(cla, dungeon)
                            sd_in_ = True
                            break
                        time.sleep(0.7)




                else:
                    menu_open(cla)
                    click_pos_2(80, 160, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\hondon_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(620, 190, cla)
                            for z in range(10):
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\ubis_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.5)
                            break
                        time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0


# 배틀 시뮬레이션
def season_dungeon_in_battle_ing(cla, dungeon):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_add
    try:
        print("season_dungeon_in_battle_ing")
        ing_ = True
        while ing_ is True:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\sungwoon_fail.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(430, 270, 540, 360, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("season_dungeon_in_battle_ing : failed", imgs_)
                myQuest_play_add(cla, dungeon)
                ing_ = False

                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\dark_exit.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 1000, 800, 1040, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("battle 나가기")
                        click_pos_2(555, 1015, cla)
                        break
                    time.sleep(0.2)

            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\battle_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("season_dungeon_in_battle_ing : battle_title", imgs_)
                    myQuest_play_add(cla, dungeon)
                    ing_ = False
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\sungwoon_clear.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(430, 270, 540, 360, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("season_dungeon_in_battle_ing : clear", imgs_)
                        click_pos_2(555, 1015, cla)

            print("battle 체크 카운터 10... => ")
            time.sleep(1)



    except Exception as e:
        print(e)
        return 0


def season_dungeon_in_battle(cla, dungeon):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg, mouse_move_cpp
    from action_ares import menu_open, loading_ares
    from schedule import myQuest_play_add
    try:
        print("season_dungeon_in_battle")

        where_dungeon = dungeon.split("_")

        sd_in_ = False
        sd_in_count = 0
        while sd_in_ is False:
            sd_in_count += 1
            if sd_in_count > 4:
                sd_in_ = True
                myQuest_play_add(cla, dungeon)
                time.sleep(0.2)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\battle_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(820, 1015, cla)
                # 로딩
                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\alrim.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(450, 450, 500, 500, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(535, 585, cla)

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        loading_ares(cla)
                        # ing
                        season_dungeon_in_battle_ing(cla, dungeon)
                        sd_in_ = True
                        break
                    time.sleep(0.7)




            else:
                menu_open(cla)
                click_pos_2(80, 160, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\hondon_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(620, 190, cla)
                        for z in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\season_dungeon\\battle_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.5)
                        break
                    time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0