import time
import sys


sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_

def dead_die(cla, schedule):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg
    from get_items import get_item_start
    from massenger import line_to_me
    from schedule import myQuest_play_add

    try:
        print("dead_die")

        deaded = False

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_potal.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(270, 800, 600, 1030, cla, img, 0.7)
        if imgs_ is not None:
            deaded = True
            click_pos_reg(imgs_.x, imgs_.y, cla)

        if deaded == True:
            if schedule == "튜토육성":
                get_item_start(cla)
                why = "튜토하다 죽었다. 손 좀 보자"
                line_to_me(cla, why)
            if schedule == "메인퀘스트":
                get_item_start(cla)
                why = "메인퀘하다 죽었다. 손 좀 보자"
                line_to_me(cla, why)
                # myQuest_play_add(cla, schedule)

        # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(280, 40, 960, 300, cla, img, 0.7)
        # if imgs_ is not None:
        #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_potal.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(270, 800, 600, 1030, cla, img, 0.7)
        #     if imgs_ is not None:
        #         click_pos_reg(imgs_.x, imgs_.y, cla)
        # else:
        #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_potal.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(270, 800, 600, 1030, cla, img, 0.7)
        #     if imgs_ is not None:
        #         click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0

def clean_screen(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg

    try:
        print("clean_screen")

        # post 받고 난 후
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\post_get.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 400, 560, 460, cla, img, 0.7)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 이벤트 보상 닫기
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\space_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 620, 540, 700, cla, img, 0.7)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\space_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 620, 540, 700, cla, img, 0.7)
            if imgs_ is not None:
                click_pos_reg(imgs_.x, imgs_.y, cla)

        # event 닫기
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\x_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(745, 360, 800, 400, cla, img, 0.7)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 각종 활성화 되어 있는 title 닫기
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\x_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(915, 20, 960, 70, cla, img, 0.7)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)




    except Exception as e:
        print(e)
        return 0

def out_check(cla):
    import numpy as np
    import cv2
    from function import imgs_set_

    try:
        print("out_check")

        go_ = False

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\out\\camera.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 970, 40, 1015, cla, img, 0.7)
        if imgs_ is not None:
            go_ = True

        return go_
    except Exception as e:
        print(e)
        return 0

def menu_open(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("menu_open")
        menu_look = False
        menu_look_count = 0
        while menu_look is False:
            menu_look_count += 1
            if menu_look_count > 5:
                menu_look = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\menu\\friend.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(810, 290, 870, 350, cla, img, 0.7)
            if imgs_ is not None:
                menu_look = True
            else:
                result_out = out_check(cla)

                if result_out == True:
                    click_pos_2(935, 40, cla)
                else:
                    clean_screen(cla)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0

def bag_open(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("bag_open")
        bag_look = False
        bag_look_count = 0
        while bag_look is False:
            bag_look_count += 1
            if bag_look_count > 5:
                bag_look = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\bag\\bag_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None:
                bag_look = True
            else:
                menu_open(cla)
                click_pos_2(900, 50, cla)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0

def moving_m(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg

    try:
        print("moving_m")

        move_ = False
        move_count = 0

        while move_ is False:
            move_count += 1
            if move_count > 100:
                move_ = True

            time.sleep(3)
            now_moving = False

            # 고정 위치...의미 있음
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\move\\move_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(880, 80, 960, 110, cla, img, 0.7)
            if imgs_ is not None:
                print("move_2222222222222222222222222") # 추후에 지워야할듯?
                move_count = 0
                now_moving = True
            else:
                move_ = True
            time.sleep(0.1)


        return now_moving
    except Exception as e:
        print(e)
        return 0


# def shot_all(cla):
#     import numpy as np
#     import cv2
#     from function import imgs_set_, click_pos_reg
#
#     try:
#         print("shot_all")
#
#         shots_ = False
#
#         full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\shot\\shot_1.PNG"
#         img_array = np.fromfile(full_path, np.uint8)
#         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#         imgs_ = imgs_set_(180, 180, 740, 740, cla, img, 0.7)
#         if imgs_ is not None:
#             shots_ = True
#
#         full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\shot\\shot_2.PNG"
#         img_array = np.fromfile(full_path, np.uint8)
#         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#         imgs_ = imgs_set_(180, 180, 740, 740, cla, img, 0.7)
#         if imgs_ is not None:
#             shots_ = True
#
#         shots_count = 0
#         while shots_ is True:
#             shots_count += 1
#             if shots_count > 30:
#                 shots_ = False
#             full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\shot\\shot_1.PNG"
#             img_array = np.fromfile(full_path, np.uint8)
#             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#             imgs_ = imgs_set_(180, 180, 740, 740, cla, img, 0.7)
#             if imgs_ is not None:
#                 shots_count = 0
#                 click_pos_reg(imgs_.x, imgs_.y, cla)
#
#             full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\shot\\shot_2.PNG"
#             img_array = np.fromfile(full_path, np.uint8)
#             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#             imgs_ = imgs_set_(180, 180, 740, 740, cla, img, 0.7)
#             if imgs_ is not None:
#                 shots_count = 0
#                 click_pos_reg(imgs_.x, imgs_.y, cla)
#             time.sleep(0.1)
#
#
#
#
#     except Exception as e:
#         print(e)
#         return 0

def confirm_all(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg

    try:
        print("confirm_all")

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\confirm\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 560, 610, 610, cla, img, 0.7)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 1_7 가방 열어서..
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\confirm\\confirm_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 565, 605, 605, cla, img, 0.7)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 2_1 지역퀘스트
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\region_quest_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 560, 600, 610, cla, img, 0.7)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\soolock.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 620, 580, 660, cla, img, 0.7)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 2_2 드레스 확인
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_select_dress\\dress_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 560, 610, 610, cla, img, 0.7)
        if imgs_ is not None:
            click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        print(e)
        return 0




