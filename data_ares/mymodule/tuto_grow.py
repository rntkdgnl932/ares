import sys
import time

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def tuto_grow_start(cla, schedule):
    from action_ares import confirm_all, dead_die
    try:
        print("tuto_grow_start")
        dead_die(cla, schedule)
        tuto_grow_intro(cla)
        tuto_grow_main(cla, schedule)
        tuto_grow_skip(cla)
        tuto_grow_complete(cla)
        tuto_grow_explain(cla)
        confirm_all(cla)
    except Exception as e:
        print(e)
        return 0

def tuto_grow_intro(cla):
    import numpy as np
    import cv2
    import pyautogui
    from function import imgs_set_, click_pos_reg, click_pos_2
    from massenger import line_to_me

    try:
        print("tuto_grow_intro")
        # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\intro\\intro_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(415, 150, 550, 230, cla, img, 0.8)
        # if imgs_ is not None:
        #     click_pos_2(480, 505, cla)
        #     time.sleep(0.2)
        #     pyautogui.keyDown('w')
        #     time.sleep(3)
        #     pyautogui.keyUp('w')
        # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\intro\\intro_2.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(400, 650, 550, 700, cla, img, 0.8)
        # if imgs_ is not None:
        #     click_pos_reg(imgs_.x, imgs_.y, cla)
        #     time.sleep(0.2)
        #     click_pos_2(480, 505, cla)
        #
        #     w_ = False
        #     w_count = 0
        #     while w_ is False:
        #         w_count += 1
        #         if w_count > 10:
        #             why = "인트로에 막힌듯 하다."
        #             line_to_me(cla, why)
        #             w_ = True
        #         full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\intro\\intro_3.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(700, 900, 920, 960, cla, img, 0.8)
        #         if imgs_ is not None:
        #             click_pos_2(920, 990, cla)
        #             time.sleep(1)
        #             click_pos_2(920, 990, cla)
        #             w_ = True
        #         else:
        #             time.sleep(0.2)
        #             pyautogui.keyDown('w')
        #             time.sleep(3)
        #             pyautogui.keyUp('w')
        #         time.sleep(2)
        # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\intro\\intro_4.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(700, 900, 920, 960, cla, img, 0.8)
        # if imgs_ is not None:
        #     click_pos_2(920, 990, cla)
        #
        # # 이 부분은 조작이 아주 힘들다...
        # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\intro\\intro_5.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(700, 900, 920, 960, cla, img, 0.8)
        # if imgs_ is not None:
        #     for i in range(10):
        #         full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\intro\\intro_6.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(670, 870, 830, 930, cla, img, 0.8)
        #         if imgs_ is not None:
        #             for i in range(10):
        #                 click_pos_2(480, 505, cla)
        #                 time.sleep(0.2)
        #
        #                 pyautogui.keyDown('s')
        #                 time.sleep(3)
        #                 pyautogui.keyUp('s')
        #                 time.sleep(0.3)
        #                 click_pos_2(845, 955, cla)
        #                 time.sleep(0.2)
        #                 click_pos_2(830, 995, cla)
        #                 time.sleep(0.2)
        #                 click_pos_2(920, 935, cla)
        #                 time.sleep(0.2)
        #                 click_pos_2(920, 990, cla)
        #                 time.sleep(0.2)
        #                 click_pos_2(885, 945, cla)
        #                 time.sleep(0.2)
        #                 click_pos_2(970, 990, cla)
        #                 time.sleep(0.2)
        #         else:
        #             click_pos_2(480, 505, cla)
        #             time.sleep(0.2)
        #
        #             click_pos_2(920, 935, cla)
        #             time.sleep(0.2)
        #             click_pos_2(920, 990, cla)
        #             time.sleep(0.2)
        #             click_pos_2(885, 945, cla)
        #             time.sleep(0.2)
        #             click_pos_2(970, 990, cla)
        #             time.sleep(0.2)
        #         time.sleep(1)
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\intro\\intro_7.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 250, 570, 310, cla, img, 0.8)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0


def tuto_grow_main(cla, schedule):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, drag_pos
    from schedule import myQuest_play_add


    try:
        print("tuto_grow_main")


        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\main\\chaps\\chaps.png"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(785, 75, 835, 100, cla, img, 0.77)
        if imgs_ is not None:
            drag_pos(405, 605, 805, 605, cla)
            time.sleep(1)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\main\\chaps\\chaps.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(785, 75, 835, 100, cla, img, 0.77)
            if imgs_ is not None:
                print("chaps", imgs_)
                myQuest_play_add(cla, schedule)
                time.sleep(1)
        else:
            drag_pos(405, 605, 805, 605, cla)
            file_path = "C:\\my_games\\ares\\data_ares\\imgs\\tuto\\main\\chap_1\\chap_1.txt"
            with open(file_path, "r", encoding='utf-8-sig') as file:
                read_chap = file.read().splitlines()

            # 제1막 프롤로그 위기, chap_1_0
            # 제1막 1, 가디언의 소명
            # 제1막 2, 오지않는 보급품
            # 제1막 3, 위기에 처한 기지, chap_1_3
            for i in range(len(read_chap)):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\main\\chap_1\\" + read_chap[i] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 30, 960, 260, cla, img, 0.77)
                if imgs_ is not None:
                    print("chap", read_chap[i])
                    v_.now_chabter = read_chap[i]
                    x_reg = imgs_.x
                    y_reg = imgs_.y
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\move\\move_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(880, 80, 960, 110, cla, img, 0.7)
                    if imgs_ is None:

                        result_ing = tuto_grow_quest_ing(cla)
                        if result_ing == False:
                            click_pos_reg(x_reg, y_reg, cla)
                            break



    except Exception as e:
        print(e)
        return 0

def tuto_grow_quest_ing(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg

    try:
        print("tuto_grow_quest_ing")
        # 잘 안 보이니 일정시간 줘야함.

        ing_ = False
        ing_now = False
        ing_count = 0

        while ing_ is False:
            ing_count += 1
            if ing_count > 30:
                ing_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\quest_ing\\quest_ing_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 70, 810, 110, cla, img, 0.7)
            if imgs_ is not None:
                print("quest_ing_1")
                ing_ = True
                ing_now = True
            time.sleep(0.1)
        return ing_now
    except Exception as e:
        print(e)
        return 0

def tuto_grow_skip(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("tuto_grow_skip")
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(840, 30, 960, 100, cla, img, 0.7)
        if imgs_ is not None:
            print("skip_1")
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\skip_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(640, 470, 720, 570, cla, img, 0.7)
        if imgs_ is not None:
            print("skip_2")

            for i in range(10):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\skip_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(640, 470, 720, 570, cla, img, 0.7)
                if imgs_ is not None:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\skip_2_end.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(640, 410, 720, 570, cla, img, 0.7)
                    if imgs_ is not None:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        click_pos_2(685, 445, cla)
                    break
                time.sleep(0.1)
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\skip_2_end.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(640, 410, 720, 570, cla, img, 0.7)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\level_up_skip.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(280, 620, 600, 1050, cla, img, 0.7)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0

def tuto_grow_complete(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg

    try:
        print("tuto_grow_complete")
        # 퀘스트 완료
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\complete\\complete_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 500, cla, img, 0.7)
        if imgs_ is not None:
            print("complete_1")
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\complete\\complete_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 350, 550, 500, cla, img, 0.7)
            if imgs_ is not None:
                print("complete_3")
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\complete\\complete_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 350, 550, 500, cla, img, 0.7)
                if imgs_ is not None:
                    print("complete_4")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\complete\\complete_5.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 350, 550, 500, cla, img, 0.7)
                    if imgs_ is not None:
                        print("complete_5")
                        click_pos_reg(imgs_.x, imgs_.y, cla)

        # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\complete\\complete_2.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(0, 0, 230, 110, cla, img, 0.7)
        # if imgs_ is not None:
        #     print("complete_2")
        #     click_pos_reg(imgs_.x, imgs_.y, cla)
        # else:
        #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\complete\\complete_2_2.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(0, 0, 230, 110, cla, img, 0.7)
        #     if imgs_ is not None:
        #         print("complete_2_2")
        #         click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0


def tuto_grow_explain(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import out_check, bag_open

    try:
        all_pass = True
        if v_.now_chabter == "chap_1_1":

            # 행성지도 알아볼까요?
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\map\\map_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 130, 250, 250, cla, img, 0.7)
            if imgs_ is not None:
                print("map_1")
                click_pos_2(15, 135,  cla)
                time.sleep(1)


            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\map\\map_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(80, 980, 450, 1050, cla, img, 0.7)
            if imgs_ is not None:
                print("map_2")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)

            for i in range(10):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\map\\map_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None:
                    print("map_title")
                    click_pos_2(940, 50, cla)
                else:
                    break
                time.sleep(0.3)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\map\\map_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(220, 580, 470, 670, cla, img, 0.7)
            if imgs_ is not None:
                print("map_3")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)

                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\map\\map_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None:
                        print("map_title")
                        click_pos_2(940, 50, cla)
                    else:
                        break
                    time.sleep(1)
        if v_.now_chabter == "chap_1_2" or all_pass == True:
            # ㄷㅏ양한 슈트 중 원하는 항목을 보급받을수있엉..
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(140, 340, 450, 450, cla, img, 0.7)
            if imgs_ is not None:
                print("sute_1")
                click_pos_2(50, 280, cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 140, 450, 450, cla, img, 0.7)
            if imgs_ is not None:
                print("sute_2")
                click_pos_2(50, 175, cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(140, 340, 450, 500, cla, img, 0.7)
            if imgs_ is not None:
                print("sute_3")
                click_pos_reg(imgs_.x, imgs_.y, cla)
            # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_5.PNG"
            # img_array = np.fromfile(full_path, np.uint8)
            # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            # imgs_ = imgs_set_(550, 140, 810, 220, cla, img, 0.7)
            # if imgs_ is not None:
            #     print("sute_5")
            #     click_pos_reg(imgs_.x, imgs_.y, cla)
            # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_6.PNG"
            # img_array = np.fromfile(full_path, np.uint8)
            # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            # imgs_ = imgs_set_(550, 140, 810, 420, cla, img, 0.7)
            # if imgs_ is not None:
            #     print("sute_6")
            #     click_pos_reg(imgs_.x, imgs_.y, cla)
            # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_5.PNG"
            # img_array = np.fromfile(full_path, np.uint8)
            # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            # imgs_ = imgs_set_(550, 140, 810, 220, cla, img, 0.7)
            # if imgs_ is not None:
            #     print("sute_5")
            #     click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_select.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(760, 980, 960, 1040, cla, img, 0.7)
            if imgs_ is not None:
                print("sute_select")

                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_select.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(760, 980, 960, 1040, cla, img, 0.7)
                    if imgs_ is not None:
                        click_pos_2(50, 280, cla)
                        time.sleep(0.2)
                        click_pos_2(910, 1010, cla)
                    else:
                        break
                    time.sleep(0.3)

            # 보급 받은 슈트를 장착하러 가볼까요?
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_wear_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(660, 60, 860, 140, cla, img, 0.7)
            if imgs_ is not None:
                print("sute_wear_1")
                click_pos_2(870, 55, cla)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_room_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 90, 80, cla, img, 0.7)
            if imgs_ is not None:
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_room_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 90, 80, cla, img, 0.7)
                    if imgs_ is not None:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_wear_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(260, 910, 480, 980, cla, img, 0.7)
                        if imgs_ is not None:
                            print("sute_wear_2")
                            click_pos_2(480, 1005, cla)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_wear_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(100, 200, 300, 300, cla, img, 0.7)
                        if imgs_ is not None:
                            print("sute_wear_3")
                            click_pos_2(95, 175, cla)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_wear_4.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(740, 940, 880, 1000, cla, img, 0.7)
                        if imgs_ is not None:
                            print("sute_wear_4")
                            click_pos_2(910, 1020, cla)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_wear_5.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 50, 930, 130, cla, img, 0.7)
                        if imgs_ is not None:
                            print("sute_wear_5")
                            click_pos_2(940, 50, cla)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_wear_6.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 750, 870, 810, cla, img, 0.7)
                        if imgs_ is not None:
                            print("sute_wear_6")
                            click_pos_2(885, 835, cla)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_wear_7.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(420, 920, 630, 980, cla, img, 0.7)
                        if imgs_ is not None:
                            print("sute_wear_7")
                            click_pos_2(430, 1005, cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\raven_p_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 100, 100, cla, img, 0.7)
            if imgs_ is not None:
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\raven_p_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 100, 100, cla, img, 0.7)
                    if imgs_ is not None:
                        print("raven_p_title")
                        click_pos_2(940, 50, cla)
                        time.sleep(0.2)

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_wear_7.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(420, 920, 630, 980, cla, img, 0.7)
                        if imgs_ is not None:
                            print("sute_wear_7")
                            click_pos_2(430, 1005, cla)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_wear_8.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(620, 920, 800, 1000, cla, img, 0.7)
                        if imgs_ is not None:
                            print("sute_wear_8")
                            click_pos_2(820, 1015, cla)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_wear_9.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(570, 100, 820, 190, cla, img, 0.7)
                        if imgs_ is not None:
                            print("sute_wear_9")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_wear_10.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(570, 330, 820, 420, cla, img, 0.7)
                        if imgs_ is not None:
                            print("sute_wear_10")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_wear_11.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(570, 330, 820, 420, cla, img, 0.7)
                        if imgs_ is not None:
                            print("sute_wear_11")
                            click_pos_2(865, 320, cla)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_wear_12.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(630, 930, 820, 1000, cla, img, 0.7)
                        if imgs_ is not None:
                            print("sute_wear_12")
                            click_pos_2(865, 1015, cla)
                    else:
                        break
                    time.sleep(0.1)


            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\raven_p_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 100, 100, cla, img, 0.7)
            if imgs_ is not None:
                click_pos_2(940, 50, cla)


        if v_.now_chabter == "chap_1_3":
            # 가디언의 위대한 여정이 시작되었어요
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\gardiun_travel\\gt_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 60, 930, 140, cla, img, 0.7)
            if imgs_ is not None:
                print("gt_1")
                click_pos_2(940, 50, cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\gardiun_travel\\gt_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 300, 860, 360, cla, img, 0.7)
            if imgs_ is not None:
                print("chap_1_3 : gt_2")
                click_pos_2(810, 180, cla)



            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\gardiun_travel\\gardiun_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 120, 80, cla, img, 0.7)
            if imgs_ is not None:
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\gardiun_travel\\gardiun_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 120, 80, cla, img, 0.7)
                    if imgs_ is not None:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\gardiun_travel\\gt_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(60, 160, 320, 240, cla, img, 0.7)
                        if imgs_ is not None:
                            print("gt_3")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            click_pos_2(940, 50, cla)
                        time.sleep(0.1)
                    else:
                        break
                    time.sleep(0.1)

            for i in range(10):
                # 포토모드
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\photo_mode\\photo_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
                if imgs_ is not None:
                    print("photo_title")
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\shot\\shot_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(180, 180, 740, 740, cla, img, 0.7)
                    if imgs_ is not None:
                        click_pos_2(925, 535, cla)
                        break
                # 버스트 모드
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\burst\\burst_mode.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(810, 850, 960, 900, cla, img, 0.7)
                if imgs_ is not None:
                    print("burst_mode")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    break
                time.sleep(0.1)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\burst\\burst_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(890, 900, 960, 1050, cla, img, 0.8)
            if imgs_ is not None:
                burst_mode(cla)
        if v_.now_chabter == "chap_1_4":
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_4_shot\\chap_1_4_shot_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(860, 960, 960, 1050, cla, img, 0.8)
            if imgs_ is not None:
                shot_mode(cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\gardiun_help\\help_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 70, 960, 130, cla, img, 0.8)
            if imgs_ is not None:
                click_pos_2(935, 50, cla)

        if v_.now_chabter == "chap_1_5" or all_pass == True:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\gardiun_travel\\gt_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 300, 860, 360, cla, img, 0.7)
            if imgs_ is not None:
                print("chap_1_5 : gt_2")
                click_pos_2(840, 280, cla)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\spot_quest\\spot_quest_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None:
                print("spot_quest_title")
                for i in range(5):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\spot_quest\\spot_quest_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
                    if imgs_ is not None:
                        click_pos_2(940, 50, cla)
                    else:
                        break
                    time.sleep(0.3)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_5_hoilodo\\chap_1_5_hoilodo_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 70, 930, 130, cla, img, 0.7)
            if imgs_ is not None:
                print("chap_1_5 : chap_1_5_hoilodo_1")

                hoilodo_title_ready = False
                hoilodo_title_ready_count = 0

                while hoilodo_title_ready is False:
                    hoilodo_title_ready_count += 1
                    if hoilodo_title_ready_count > 7:
                        hoilodo_title_ready = True

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_5_hoilodo\\hoilodo_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
                    if imgs_ is not None:
                        hoilodo_title_ready = True
                        print("chap_1_5 : hoilodo_title")
                        click_pos_2(940, 50, cla)
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\gardiun_travel\\gt_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 300, 860, 360, cla, img, 0.7)
                        if imgs_ is not None:
                            print("chap_1_5 : gt_2")
                            click_pos_2(935, 175, cla)
                        else:
                            click_pos_2(935, 50, cla)
                    time.sleep(0.3)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_5_hoilodo\\hoilodo_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None:
                print("spot_quest_title")
                for i in range(5):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_5_hoilodo\\hoilodo_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
                    if imgs_ is not None:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_5_hoilodo\\chap_1_5_hoilodo_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(550, 930, 820, 1000, cla, img, 0.7)
                        if imgs_ is not None:
                            click_pos_2(900, 1015, cla)
                        else:
                            click_pos_2(940, 50, cla)
                    else:
                        break
                    time.sleep(0.3)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_5_wisung\\wisung_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 50, 70, 100, cla, img, 0.7)
            if imgs_ is not None:

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_5_wisung\\wisung_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 70, 700, 350, cla, img, 0.7)
                if imgs_ is not None:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_5_wisung\\wisung_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(630, 890, 860, 970, cla, img, 0.7)
                    if imgs_ is not None:
                        click_pos_2(870, 985, cla)
                    else:
                        click_pos_2(920, 935, cla)
        if v_.now_chabter == "chap_1_5" or v_.now_chabter == "chap_1_6":
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\scan\\scan_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(630, 145, 950, 270, cla, img, 0.7)
            if imgs_ is not None:
                click_pos_2(945, 145, cla)

        if v_.now_chabter == "chap_1_7":
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_jejak\\jejak_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(760, 60, 930, 130, cla, img, 0.7)
            if imgs_ is not None:
                click_pos_2(935, 50, cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_jejak\\friend.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 300, 860, 360, cla, img, 0.7)
            if imgs_ is not None:
                click_pos_2(840, 240, cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_jejak\\jejak_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None:

                jejak_ = False
                jejak_count = 0
                while jejak_ is False:
                    jejak_count += 1
                    if jejak_count > 10:
                        jejak_ = True

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_jejak\\shadow_blade.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(190, 100, 320, 150, cla, img, 0.7)
                    if imgs_ is not None:
                        click_pos_2(865, 1015, cla)
                        jejak_ = True
                        for i in range(20):
                            result = out_check(cla)
                            if result == True:
                                break
                            else:
                                click_pos_2(940, 50, cla)
                            time.sleep(0.5)
                    else:
                        click_pos_2(80, 130, cla)
                    time.sleep(0.3)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_jejak\\jejak_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
                if imgs_ is not None:
                    click_pos_2(940, 50, cla)
                    time.sleep(0.5)
                bag_open(cla)
                time.sleep(0.5)
                click_pos_2(170, 130, cla)
                time.sleep(0.5)
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\confirm\\confirm_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 565, 605, 605, cla, img, 0.7)
                    if imgs_ is not None:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        click_pos_2(940, 50, cla)
                        time.sleep(0.2)
                        break
                    else:
                        click_pos_2(915, 1015, cla)
                        time.sleep(0.3)
                    time.sleep(0.5)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_jejak\\joomogi_select_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 180, 80, cla, img, 0.7)
                if imgs_ is not None:
                    click_pos_2(940, 50, cla)
                    time.sleep(0.2)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_talgut\\chap_1_7_talgut.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(830, 60, 940, 170, cla, img, 0.7)
            if imgs_ is not None:
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_talgut\\talgut_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None:
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_talgut\\chap_1_7_talgut_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(640, 940, 820, 1000, cla, img, 0.7)
                    if imgs_ is not None:
                        click_pos_2(915, 1015, cla)
                        time.sleep(0.2)
                        click_pos_2(940, 50, cla)
                        time.sleep(0.2)
                        break
                    else:
                        click_pos_2(40, 180, cla)
                        time.sleep(0.2)
                    time.sleep(0.3)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_talgut\\talgut_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None:
                click_pos_2(940, 50, cla)
                time.sleep(0.2)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_talgut\\chap_1_7_talgut_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 850, 900, 910, cla, img, 0.7)
            if imgs_ is not None:
                click_pos_2(920, 935, cla)

            # 새로운 컨텐츠가 개방되었어요
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_hybdong\\new_contents.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 60, 940, 140, cla, img, 0.7)
            if imgs_ is not None:
                click_pos_2(940, 50, cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_hybdong\\quest_menu_open.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(880, 20, 960, 100, cla, img, 0.7)
            if imgs_ is not None:
                click_pos_2(940, 50, cla)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_jejak\\friend.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 300, 860, 360, cla, img, 0.7)
            if imgs_ is not None:
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_hybdong\\hyubdong_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 230, 150, 330, cla, img, 0.7)
                    if imgs_ is not None:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    time.sleep(0.1)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_hybdong\\hyubdong_select_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None:
                click_pos_2(290, 535, cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_hybdong\\dark_demenjeon_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None:
                click_pos_2(70, 935, cla)
                time.sleep(0.2)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_hybdong\\book_cancle.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 900, 200, 990, cla, img, 0.7)
                if imgs_ is not None:
                    click_pos_2(70, 935, cla)
                    time.sleep(0.3)
                click_pos_2(940, 50, cla)
                time.sleep(0.2)
        if v_.now_chabter == "chap_1_10":
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_10_kichi_sangjum\\kichi_11.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(520, 470, 620, 570, cla, img, 0.7)
            if imgs_ is not None:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_10_kichi_sangjum\\kichi_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(340, 540, 570, 620, cla, img, 0.7)
                if imgs_ is not None:
                    click_pos_2(580, 530, cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_10_kichi_sangjum\\skill_sangjum_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None:
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_10_kichi_sangjum\\skill_sangjum_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
                    if imgs_ is not None:
                        click_pos_2(940, 50, cla)
                    else:
                        break
                    time.sleep(0.2)

    except Exception as e:
        print(e)
        return 0


def burst_mode(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, mouse_move_cpp, drag_pos_Press, drag_pos_Release

    try:
        print("burst_mode")



        burst_mode_action = True
        burst_mode_count = 0
        while burst_mode_action is True:
            burst_mode_count += 1
            if burst_mode_count > 30:
                burst_mode_action = False

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\burst\\burst_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(890, 890, 960, 1050, cla, img, 0.7)
            if imgs_ is not None:

                # 마우스 이동
                mouse_move_cpp(280, 505, cla)
                # 0.2초
                time.sleep(0.2)

                # 마우스 누르기
                drag_pos_Press()
                # 0.2초
                time.sleep(0.2)

                for i in range(30):
                    x_reg = 280 + (i * 20)
                    # 마우스 이동
                    mouse_move_cpp(x_reg, 505, cla)
                    # 0.2초
                    time.sleep(0.2)

                # 마우스 떼기
                drag_pos_Release()
                # 0.2초
                time.sleep(0.2)



            else:

                burst_mode_action = False

            time.sleep(0.2)


    except Exception as e:
        print(e)
        return 0


def shot_mode(cla):
    import numpy as np
    import cv2
    import pyautogui
    from function import imgs_set_, click_pos_reg, mouse_move_cpp, drag_pos_Press, drag_pos_Release, click_pos_2

    try:
        print("burst_mode")

        click_pos_2(480, 505, cla)
        time.sleep(0.2)

        pyautogui.keyDown('s')
        time.sleep(1)
        pyautogui.keyUp('s')
        time.sleep(0.2)

        pyautogui.keyDown('w')
        time.sleep(0.05)
        pyautogui.keyUp('w')
        time.sleep(0.2)

        shot_ready = True
        shot_ready_count = 0
        while shot_ready is True:
            shot_ready_count += 1
            if shot_ready_count > 20:
                shot_ready = False
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_4_shot\\chap_1_4_shot_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(860, 960, 960, 1050, cla, img, 0.8)
            if imgs_ is not None:
                click_pos_2(480, 505, cla)
                time.sleep(0.2)

                # 마우스 누르기
                drag_pos_Press()

                pyautogui.keyDown('a')
                time.sleep(3)
                pyautogui.keyUp('a')
                time.sleep(0.2)
                pyautogui.keyDown('d')
                time.sleep(3)
                pyautogui.keyUp('d')

                # 마우스 떼기
                drag_pos_Release()

            else:

                shot_ready = False

            time.sleep(0.2)


    except Exception as e:
        print(e)
        return 0


