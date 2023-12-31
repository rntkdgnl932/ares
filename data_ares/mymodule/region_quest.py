import time
# import os
import sys

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def region_quest_start(cla, region_n):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import confirm_all, dead_die, clean_screen, out_check
    from main_grow import grow_skip, grow_complete
    from dungeon import dark_play
    from potion_ares import juljun_potion_check
    try:
        print("quest_start!!!!!!!!!!!!!!!")



        for i in range(10):

            print("순환", i + 1)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\region_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                region_quest_get(cla, region_n)
                v_.region_click = 0
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\region_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    region_quest_get(cla, region_n)
                    v_.region_click = 0

                step = "지역퀘스트_" + region_n
                dead_die(cla, str(step))

                region_quest_camera(cla)

                grow_skip(cla)
                region_skip(cla)
                grow_complete(cla)
                confirm_all(cla)


                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\move\\move_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(880, 80, 960, 170, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:

                    for m in range(20):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\move\\move_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(880, 80, 960, 170, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("이동 중")
                        else:
                            break
                        time.sleep(0.5)
                else:
                    # 지역퀘스트 필드보스
                    region_quest_penetra(cla)
                    region_quest_gorgon(cla)
                    result_ing = region_quest_ing(cla)

                    if result_ing == False:

                        # result_click = region_quest_click_before(cla)
                        #
                        # if result_click == False:

                        result_dark = dark_play(cla)

                        if result_dark == False:

                            # click_pos_2(840, 125, cla)
                            region_quest_get(cla, region_n)
                            #
                            # time.sleep(1)
                            #
                            # confirm_all(cla)
                    else:
                        v_.region_click += 1
                        print("v_.region_click", v_.region_click)
                        if v_.region_click > 10:
                            v_.region_click = 0
                            region_quest_get(cla, region_n)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\dark_clear.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(430, 290, 540, 340, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("region : dark_clear", imgs_)
                    v_.dark_demen = False
                    time.sleep(1)
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\dark_exit.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 1000, 800, 1040, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
    except Exception as e:
        print(e)
        return 0

def region_skip(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import out_check, clean_screen, confirm_all
    from gardiun_mission import gardiun_mission_get

    try:
        print("region_skip")
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\region_gold_click_ready.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(340, 380, 440, 450, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y - 100, cla)
            time.sleep(2)
            confirm_all(cla)



    except Exception as e:
        print(e)
        return 0

def region_quest_camera(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import out_check, clean_screen
    from gardiun_mission import gardiun_mission_get

    try:
        print("region_quest_camera")

        ing_ = False
        ing_count = 0

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\region_camera.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(890, 490, 960, 565, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:

            while ing_ is False:
                ing_count += 1
                if ing_count > 20:
                    clean_screen(cla)
                    result_out = out_check(cla)
                    if result_out == True:
                        ing_ = True

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\region_camera.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(890, 490, 960, 565, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(3)

                    success = True

                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\camera_trash.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(440, 940, 480, 990, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:

                            success = False

                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                            click_pos_2(940, 50, cla)
                            time.sleep(1)
                            click_pos_2(840, 125, cla)
                            break
                        else:
                            result_out = out_check(cla)
                            if result_out == True:
                                ing_ = True
                                break


                            # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\region_camera_no_shot.PNG"
                            # img_array = np.fromfile(full_path, np.uint8)
                            # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            # imgs_ = imgs_set_(460, 510, 505, 555, cla, img, 0.7)
                            # if imgs_ is not None and imgs_ != False:
                            #     print("사진찍는 퀘스트 중")
                            # else:
                            #     print("사진 찍자~!")
                            #     click_pos_reg(x_reg, y_reg, cla)
                    if success == True:
                        ing_ = True
                time.sleep(1)
        else:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\region_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("퀘스트 받기 대기중")
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\gardiun_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    gardiun_mission_get(cla, "가디언임무")
                else:
                    clean_screen(cla)

    except Exception as e:
        print(e)
        return 0

def region_quest_penetra(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import confirm_all

    try:
        print("region_quest_penetra")

        ing_ = False
        ing_count = 0

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\penetra_legend2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 135, 55, 185, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:

            while ing_ is False:
                ing_count += 1
                if ing_count > 20:
                    ing_ = True

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\penetra_legend2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 135, 55, 185, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    ing_ = True
                    time.sleep(1)


    except Exception as e:
        print(e)
        return 0

def region_quest_gorgon(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import confirm_all

    try:
        print("region_quest_gorgon")

        ing_ = False
        ing_count = 0

        # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\region_gorgon.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(780, 100, 900, 135, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:




        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\region_gorgon2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 135, 65, 185, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:

            while ing_ is False:
                ing_count += 1
                if ing_count > 20:
                    ing_ = True

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\region_gorgon2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 135, 65, 185, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    ing_ = True
                time.sleep(1)
                    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
                    # img_array = np.fromfile(full_path, np.uint8)
                    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    # imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
                    # if imgs_ is not None and imgs_ != False:
                    #     click_pos_reg(imgs_.x, imgs_.y, cla)
                    #     v_.gorgon = True
                    #     ing_ = True
                #
                #
                # else:
                #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\region_gorgon.PNG"
                #     img_array = np.fromfile(full_path, np.uint8)
                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #     imgs_ = imgs_set_(780, 100, 860, 135, cla, img, 0.7)
                #     if imgs_ is not None and imgs_ != False:
                #         click_pos_reg(imgs_.x, imgs_.y, cla)
                #
                #         for i in range(100):
                #             full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\region_gorgon2.PNG"
                #             img_array = np.fromfile(full_path, np.uint8)
                #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #             imgs_ = imgs_set_(0, 135, 65, 185, cla, img, 0.7)
                #             if imgs_ is not None and imgs_ != False:
                #                 break
                #             else:
                #                 confirm_all(cla)
                #             time.sleep(1)


    except Exception as e:
        print(e)
        return 0

def region_quest_ing(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg

    try:
        print("region_quest_ing")
        # 잘 안 보이니 일정시간 줘야함.

        ing_ = False
        ing_now = False
        ing_count = 0

        while ing_ is False:
            ing_count += 1
            if ing_count > 15:
                ing_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\quest_ing\\quest_ing_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 100, 800, 180, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("quest_ing_1")
                ing_ = True
                ing_now = True
            time.sleep(0.1)
        return ing_now
    except Exception as e:
        print(e)
        return 0

def region_quest_click_before(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg

    try:
        print("region_quest_click_before")

        ing_now = False

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\click_check_region.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 110, 935, 180, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("click_check")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            ing_now = True
        return ing_now
    except Exception as e:
        print(e)
        return 0


def region_quest_get(cla, region_n):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import menu_open, confirm_all, maul_go, clean_screen
    from schedule import myQuest_play_add

    try:
        print("region_quest_get")

        y_reg = 78 + (34 * int(region_n))

        region_ = False
        region_count = 0
        while region_ is False:
            region_count += 1
            if region_count > 7:
                region_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\region_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("퀘스트 받자")

                region_ = True

                click_pos_2(40, y_reg, cla)
                time.sleep(0.5)

                is_region = False

                for i in range(5):

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\repeat.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(150, 100, 960, 330, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(940, 50, cla)
                        is_region = False
                        break

                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\region_quest_ing.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 100, 960, 330, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            is_region = True
                            time.sleep(0.1)
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\region_quest_list.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(150, 100, 960, 330, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                is_region = True
                                time.sleep(0.1)
                                break
                    time.sleep(0.2)


                if is_region == True:
                    for i in range(10):

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\region_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\anymore_quest.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 90, 500, 130, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("지역 퀘스트 끝")
                                is_region = False
                                break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\not_moving.png"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(390, 90, 480, 140, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("이동경로 실패...마을로 갔다가 오자")
                                maul_go(cla)
                                break
                        time.sleep(0.4)

                    # for i in range(30):
                    #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\not_moving.png"
                    #     img_array = np.fromfile(full_path, np.uint8)
                    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    #     imgs_ = imgs_set_(390, 90, 480, 140, cla, img, 0.7)
                    #     if imgs_ is not None and imgs_ != False:
                    #         print("이동경로 실패...마을로 갔다가 오자")
                    #         maul_go(cla)
                    #         break
                    #     time.sleep(0.2)

                if is_region == False:
                    data = "지역퀘스트_" + str(region_n)
                    myQuest_play_add(cla, data)
                    clean_screen(cla)
                else:
                    confirm_all(cla)

            else:
                menu_open(cla)

                time.sleep(0.1)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\menu_region_quest.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(780, 200, 960, 400, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\region_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)

            time.sleep(0.3)

    except Exception as e:
        print(e)
        return 0

