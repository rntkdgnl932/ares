import time
# import os
import sys

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def power_up_start(cla):
    try:
        print("power_up_start")
        soohosuk(cla)
        time.sleep(0.2)
        hoilodo(cla)
        time.sleep(0.2)
        monster_dogam(cla)
    except Exception as e:
        print(e)
        return 0


def soohosuk(cla):
    import numpy as np
    import cv2

    from action_ares import menu_open
    from function import click_pos_2, imgs_set_, click_pos_reg
    from tuto_grow import tuto_grow_skip
    try:
        print("soohosuk")

        sooho_up = False
        sooho_up_count = 0
        while sooho_up is False:
            sooho_up_count += 1
            print("sooho_up_count", sooho_up_count)
            if sooho_up_count > 15:
                sooho_up = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\soohosuk_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("soohosuk_title : 진입완료료")

                for z in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\skip_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(640, 470, 720, 570, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.1)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\skip_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(640, 470, 720, 570, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("soogosuk : skip_2")

                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\skip_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(640, 470, 720, 570, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\skip_2_end.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(640, 410, 720, 570, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                click_pos_2(685, 445, cla)
                            break
                        time.sleep(0.2)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\soohosuk_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 80, 170, 130, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("soohosuk_point", imgs_)
                        click_pos_reg(imgs_.x - 14, imgs_.y + 10, cla)

                        if cla == "one":
                            x1 = imgs_.x - 15
                            x2 = imgs_.x + 15
                        if cla == "two":
                            x1 = imgs_.x - 15 - 960
                            x2 = imgs_.x + 15 - 960
                        if cla == "three":
                            x1 = imgs_.x - 15 - 960 - 960
                            x2 = imgs_.x + 15 - 960 - 960
                        if cla == "four":
                            x1 = imgs_.x - 15 - 960 - 960 - 960
                            x2 = imgs_.x + 15 - 960 - 960 - 960

                        y1 = imgs_.y - 15
                        y2 = imgs_.y + 15

                        time.sleep(0.5)


                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\sooho_skip_off.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(690, 990, 790, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("sooho_skip_off", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\sooho_skip_on.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(690, 990, 790, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("sooho_skip_on", imgs_)
                            for i in range(5):
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\soohosuk_point.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(x1, y1, x2, y2, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(910, 1015, cla)
                                else:
                                    break
                                time.sleep(1)
                        else:
                            for i in range(5):
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\sooho_mystery_open.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(780, 980, 960, 1060, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(910, 1015, cla)
                                else:
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\soohosuk_point.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x1, y1, x2, y2, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(910, 1015, cla)
                                    else:
                                        break
                                time.sleep(1)


                    else:
                        sooho_up = True
                    time.sleep(0.5)




            else:

                menu_open(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\soohosuk_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_jejak\\friend.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 300, 860, 360, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            # 포인트 여부 파악

                            ispoint = False

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\menu_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(830, 150, 865, 180, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                ispoint = True
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\menu_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(830, 150, 865, 180, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    ispoint = True

                            if ispoint == True:
                                click_pos_2(840, 180, cla)
                            else:
                                sooho_up = True
                                break
                    time.sleep(1)

            time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\soohosuk_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 45, cla)
            else:
                break
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


def hoilodo(cla):
    import numpy as np
    import cv2

    from action_ares import menu_open
    from function import click_pos_2, imgs_set_, click_pos_reg
    from tuto_grow import tuto_grow_skip
    try:
        print("hoilodo")

        hoilodo_up = False
        hoilodo_up_count = 0
        while hoilodo_up is False:
            hoilodo_up_count += 1
            print("hoilodo_up_count", hoilodo_up_count)
            if hoilodo_up_count > 15:
                hoilodo_up = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hoilodo_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("hoilodo_title : 진입완료료")

                time.sleep(0.5)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(60, 60, 220, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("hoilodo_point_1", imgs_)
                    click_pos_reg(imgs_.x - 40, imgs_.y + 5, cla)
                    time.sleep(0.5)

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(120, 120, 170, 330, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("hoilodo_point_2", imgs_)
                        click_pos_reg(imgs_.x - 70, imgs_.y + 7, cla)
                        time.sleep(1)

                        for i in range(20):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(120, 120, 170, 330, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:

                                hoilodo_point = False

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_3.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(150, 310, 800, 880, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("hoilodo_point_3", imgs_)
                                    click_pos_reg(imgs_.x - 10, imgs_.y + 7, cla)
                                    hoilodo_point = True
                                    time.sleep(0.5)
                                else:
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_4.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(150, 310, 800, 880, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("hoilodo_point_4", imgs_)
                                        click_pos_reg(imgs_.x - 10, imgs_.y + 7, cla)
                                        hoilodo_point = True
                                        time.sleep(0.5)
                                    else:
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_4.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(150, 310, 800, 880, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("hoilodo_point_4", imgs_)
                                            click_pos_reg(imgs_.x - 10, imgs_.y + 7, cla)
                                            hoilodo_point = True
                                            time.sleep(0.5)

                                if hoilodo_point == True:
                                    click_pos_2(865, 1020, cla)
                                else:
                                    break
                            else:
                                break
                            time.sleep(0.5)
                else:
                    hoilodo_up = True

            else:

                menu_open(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hoilodo_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_jejak\\friend.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 300, 860, 360, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            # 포인트 여부 파악

                            ispoint = False

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\menu_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(930, 150, 960, 180, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                ispoint = True
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\menu_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(930, 150, 960, 180, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    ispoint = True

                            if ispoint == True:
                                click_pos_2(935, 175, cla)
                            else:
                                hoilodo_up = True
                                break
                    time.sleep(1)

            time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hoilodo_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 45, cla)
            else:
                break
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0


def monster_dogam(cla):
    import numpy as np
    import cv2

    from action_ares import menu_open
    from function import click_pos_2, imgs_set_, click_pos_reg
    try:
        print("monster_dogam")

        monster_up = False
        monster_up_count = 0
        while monster_up is False:
            monster_up_count += 1
            print("monster_up_count", monster_up_count)
            if monster_up_count > 15:
                monster_up = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\monster_dogam_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("monster_dogam_title : 진입완료료")
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(80, 980, 120, 1020, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 40, imgs_.y + 7, cla)
                    # click_pos_2(60, 1015, cla)
                    time.sleep(1)
                    for i in range(5):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\monster_dogam_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            time.sleep(0.5)
                            break
                        else:
                            click_pos_2(60, 1015, cla)
                        time.sleep(0.5)

                    # 만약 코어가 쌓인다면 후처리도 함께하기
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_grow_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(170, 70, 215, 105, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 40, imgs_.y + 7, cla)
                        # click_pos_2(155, 95, cla)

                        for z in range(20):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_grow_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(170, 70, 215, 105, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_dogam_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 580, 580, 630, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    print("혹시 몰라 예 클릭하기")

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_corestone_use.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(800, 990, 920, 1060, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)

                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\no_monster_core_.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(380, 60, 550, 130, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_grow_point_3.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(150, 300, 800, 600, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x - 30, imgs_.y + 25, cla)
                                            time.sleep(0.5)
                                        else:
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_grow_point_2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(70, 120, 120, 280, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x - 40, imgs_.y + 2, cla)
                                                # click_pos_2(55, 155, cla)
                                                time.sleep(0.5)

                                    else:
                                        for k in range(10):
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_dogam_confirm.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(480, 580, 580, 630, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                break
                                            time.sleep(0.5)

                                else:
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_grow_point_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(70, 120, 120, 280, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x - 40, imgs_.y + 2, cla)
                                        # click_pos_2(55, 155, cla)
                                        time.sleep(0.5)

                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_grow_point_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(150, 300, 800, 600, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x - 30, imgs_.y + 25, cla)
                                        time.sleep(0.5)
                            else:
                                monster_up = True
                                break
                            time.sleep(0.5)
                    else:
                        monster_up = True
                else:
                    # 후처리 하기
                    # 만약 코어가 쌓인다면 후처리도 함께하기
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_grow_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(170, 70, 215, 105, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 40, imgs_.y + 7, cla)
                        # click_pos_2(155, 95, cla)

                        for z in range(20):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_grow_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(170, 70, 215, 105, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_dogam_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 580, 580, 630, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    print("혹시 몰라 예 클릭하기")

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_corestone_use.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(800, 990, 920, 1060, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:

                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)

                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\no_monster_core_.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(380, 60, 550, 130, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_grow_point_3.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(150, 300, 800, 600, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x - 30, imgs_.y + 25, cla)
                                            time.sleep(0.5)
                                    else:
                                        for k in range(10):
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_dogam_confirm.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(480, 580, 580, 630, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                break
                                            time.sleep(0.5)

                                else:
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_grow_point_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(70, 120, 120, 280, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x - 40, imgs_.y + 2, cla)
                                        # click_pos_2(55, 155, cla)
                                        time.sleep(0.5)

                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_grow_point_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(150, 300, 800, 600, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x - 30, imgs_.y + 25, cla)
                                        time.sleep(0.5)
                            else:
                                monster_up = True
                                break
                            time.sleep(0.5)
                    else:
                        monster_up = True

            else:

                menu_open(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\monster_dogam_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_jejak\\friend.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 300, 860, 360, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            # 포인트 여부 파악

                            ispoint = False
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\menu_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(860, 210, 900, 240, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                ispoint = True
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\menu_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(860, 210, 900, 240, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    ispoint = True

                            if ispoint == True:
                                click_pos_2(870, 240, cla)
                            else:
                                monster_up = True
                                break
                    time.sleep(1)

            time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\monster_dogam_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 45, cla)
            else:
                break
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0


