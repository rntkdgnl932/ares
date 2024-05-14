import time
# import os
import sys

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def juljun_potion_check(cla):
    import numpy as np
    import cv2
    from function import imgs_set_
    from action_ares import maul_go, clean_screen
    try:
        print("juljun_potion_check")
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\juljun_potion.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(530, 980, 590, 1030, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("포션 없다")

                clean_screen(cla)
                time.sleep(1)

                result_maul = maul_go(cla)
                if result_maul == True:
                    maul_potion_get(cla)

    except Exception as e:
        print(e)
        return 0

def maul_potion_get(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import clean_screen, out_check, confirm_all, maul_go, dead_die
    from powerup_ares import power_up_start
    from soojib_boonhae import soojib_boonhae_start
    try:
        print("maul_potion_get")

        for i in range(3):
            result_out = out_check(cla)
            if result_out == True:
                break
            else:
                clean_screen(cla)
            time.sleep(0.5)

        result_maul = maul_go(cla)
        if result_maul == True:

            dead_die(cla, "check")

            potion_go = False
            potion_go_count = 0
            while potion_go is False:
                potion_go_count += 1
                if potion_go_count > 7:
                    potion_go = True
                    confirm_all(cla)
                    clean_screen(cla)

                # 새로운 물약 구매
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\jabhwa_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\ilgwal_buy_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 410, 530, 450, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\ilgwal_buy_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 610, 570, 670, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            click_pos_2(520, 640, cla)

                        for i in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\ilgwal_buy_complete.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 80, 600, 140, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("물약 다 삼")
                                potion_go = True
                            time.sleep(0.1)

                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\ilgwal_buy.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(100, 990, 200, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            for i in range(10):
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\anymore_ilgwal_buy.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 80, 600, 140, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("물약 더 못삼")
                                    potion_go = True
                                time.sleep(0.1)

                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\jabhwa.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(880, 880, 960, 960, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        for i in range(20):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\jabhwa_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                print("잡화상점 가는 중", i)
                            time.sleep(1)

                    else:
                        click_pos_2(920, 990, cla)
                time.sleep(1)

            for i in range(3):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\potion_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 600, 570, 660, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\jabhwa_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(940, 50, cla)
                    else:
                        break

            power_up_start(cla)
            soojib_boonhae_start(cla)

    except Exception as e:
        print(e)
        return 0

def maul_potion_get_ex(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import clean_screen, out_check, confirm_all, maul_go, dead_die
    from powerup_ares import power_up_start
    from soojib_boonhae import soojib_boonhae_start
    try:
        print("maul_potion_get")

        for i in range(3):
            result_out = out_check(cla)
            if result_out == True:
                break
            else:
                clean_screen(cla)
            time.sleep(0.5)

        result_maul = maul_go(cla)
        if result_maul == True:

            dead_die(cla, "check")

            potion_go = False
            potion_go_count = 0
            while potion_go is False:
                potion_go_count += 1
                if potion_go_count > 7:
                    potion_go = True
                    confirm_all(cla)
                    clean_screen(cla)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\max.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(500, 540, 580, 580, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\potion_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 600, 570, 660, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        potion_go = True

                    # 버프들 사까?
                    maul_potion_get_zero(cla)

                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\jabhwa_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\jabhwa_potion.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 120, 80, 560, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(865, 1015, cla)

                            time.sleep(1)

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\exceed_potion.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 80, 480, 140, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("물약 더 못삼")
                                potion_go = True

                                # 버프들 사까?
                                maul_potion_get_zero(cla)
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\jabhwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(880, 880, 960, 960, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            for i in range(20):
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\jabhwa_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    print("잡화상점 가는 중", i)
                                time.sleep(1)

                        else:
                            click_pos_2(920, 990, cla)
                time.sleep(1)
            for i in range(3):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\potion_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 600, 570, 660, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\jabhwa_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(940, 50, cla)
                    else:
                        break

            power_up_start(cla)
            soojib_boonhae_start(cla)

    except Exception as e:
        print(e)
        return 0

def maul_potion_get_full(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import clean_screen, out_check, confirm_all, maul_go, dead_die
    from powerup_ares import power_up_start
    from soojib_boonhae import soojib_boonhae_start
    try:
        print("maul_potion_get_full")

        maul_potion_get(cla)

    except Exception as e:
        print(e)
        return 0

def maul_potion_get_full_2(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import clean_screen, confirm_all
    try:
        print("maul_potion_get_full_2")

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\max.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 540, 580, 580, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\potion_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 600, 570, 660, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

        potion_go = False
        potion_go_count = 0
        while potion_go is False:
            if potion_go_count > 3:
                potion_go = True
                confirm_all(cla)
                clean_screen(cla)

            else:
                y_reg = 200 + (potion_go_count * 45)

                click_pos_2(100, y_reg, cla)

                time.sleep(0.5)

                click_pos_2(865, 1015, cla)

                exceed = False

                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\exceed_potion.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 80, 480, 140, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        exceed = True
                        break
                    time.sleep(0.2)

                if exceed == True:
                    potion_go_count += 1

                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\max.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 540, 580, 580, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.2)

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\max.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 540, 580, 580, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\potion_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 600, 570, 660, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            potion_go_count += 1
            time.sleep(0.3)



    except Exception as e:
        print(e)
        return 0

def maul_potion_get_zero(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import clean_screen, confirm_all
    try:
        print("maul_potion_get_zero")

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\max.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 540, 580, 580, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\potion_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 600, 570, 660, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

        potion_go = False
        potion_go_count = 0
        while potion_go is False:
            if potion_go_count > 3:
                potion_go = True
                confirm_all(cla)
                clean_screen(cla)

            else:
                y_reg = 200 + (potion_go_count * 45)

                click_pos_2(100, y_reg, cla)

                time.sleep(0.5)

                click_pos_2(865, 1015, cla)

                exceed = False

                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\exceed_potion.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 80, 480, 140, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        exceed = True
                        break
                    time.sleep(0.2)

                if exceed == True:
                    potion_go_count += 1

                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\max.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 540, 580, 580, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.2)

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\zero.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(890, 200, 960, 300, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\max.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 540, 580, 580, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.1)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\potion_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 600, 570, 660, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                potion_go_count += 1
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\cancle.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(410, 620, 460, 660, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            potion_go_count += 1
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\cancle.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(410, 620, 460, 660, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        potion_go_count += 1
            time.sleep(0.3)



    except Exception as e:
        print(e)
        return 0


def maul_potion_gardiun(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import clean_screen, out_check, confirm_all
    from powerup_ares import power_up_start
    from soojib_boonhae import soojib_boonhae_start
    try:
        print("maul_potion_gardiun")

        maul_potion_get(cla)

    except Exception as e:
        print(e)
        return 0


