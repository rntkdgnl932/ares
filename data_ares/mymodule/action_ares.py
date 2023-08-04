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
    from potion_ares import maul_potion_get

    try:
        print("dead_die")

        deaded = False

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_potal.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(270, 800, 600, 1030, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            deaded = True
            click_pos_reg(imgs_.x, imgs_.y, cla)

            for i in range(10):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("loding")
                    loading_ares(cla)
                    break
                time.sleep(1)
            for i in range(10):
                result_out = out_check(cla)
                if result_out == True:
                    break
                time.sleep(1)
            # 물약 사자~!
            result_maul = maul_go(cla)
            if result_maul == True:
                maul_potion_get(cla)

        if deaded == True:
            if schedule == "튜토육성":
                get_item_start(cla)
                why = "튜토하다 죽었다. 손 좀 보자"
                line_to_me(cla, why)
            if schedule == "메인퀘스트":
                get_item_start(cla)
                why = "메인퀘하다 죽었다. 손 좀 보자"
                line_to_me(cla, why)
                myQuest_play_add(cla, schedule)

        # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(280, 40, 960, 300, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_potal.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(270, 800, 600, 1030, cla, img, 0.7)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_reg(imgs_.x, imgs_.y, cla)
        # else:
        #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_potal.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(270, 800, 600, 1030, cla, img, 0.7)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0

def clean_screen(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, drag_pos
    from massenger import line_to_me

    try:
        print("clean_screen")

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\game_ares_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            for i in range(3):
                # 절전모드일 경우 풀기
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    drag_pos(405, 605, 945, 605, cla)

                # post 받고 난 후
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\post_get.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 400, 560, 460, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                # 이벤트 보상 닫기
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\space_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 620, 540, 700, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\space_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 620, 540, 700, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                # event 닫기
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\x_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(745, 360, 800, 400, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                # 각종 활성화 되어 있는 title 닫기
                for z in range(3):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\x_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(915, 20, 960, 70, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        break
                    time.sleep(0.1)

                result_out = out_check(cla)
                if result_out == True:
                    break

        else:
            print("clean_screen : 아레스 꺼져있는지 10초간 다시 검사하기")
            is_ares = False

            for i in range(10):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\game_ares_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    is_ares = True
                    break
            if is_ares == False:
                why = "아레스 꺼진게 확실하다"
                print(why)
                line_to_me(cla, why)

                dir_path = "C:\\my_games\\load\\ares"
                file_path = dir_path + "\\start.txt"

                with open(file_path, "w", encoding='utf-8-sig') as file:
                    data = 'no'
                    file.write(str(data))



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
        if imgs_ is not None and imgs_ != False:
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
            if imgs_ is not None and imgs_ != False:
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
            if imgs_ is not None and imgs_ != False:
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
            if imgs_ is not None and imgs_ != False:
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
#         if imgs_ is not None and imgs_ != False:
#             shots_ = True
#
#         full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\shot\\shot_2.PNG"
#         img_array = np.fromfile(full_path, np.uint8)
#         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#         imgs_ = imgs_set_(180, 180, 740, 740, cla, img, 0.7)
#         if imgs_ is not None and imgs_ != False:
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
#             if imgs_ is not None and imgs_ != False:
#                 shots_count = 0
#                 click_pos_reg(imgs_.x, imgs_.y, cla)
#
#             full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\shot\\shot_2.PNG"
#             img_array = np.fromfile(full_path, np.uint8)
#             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#             imgs_ = imgs_set_(180, 180, 740, 740, cla, img, 0.7)
#             if imgs_ is not None and imgs_ != False:
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
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 1_7 가방 열어서..
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\confirm\\confirm_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 565, 605, 605, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 2_1 지역퀘스트
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\region_quest_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 560, 600, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\soolock.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 620, 580, 660, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 2_2 드레스 확인
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_select_dress\\dress_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 560, 610, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # map maul
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 560, 610, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 자동사냥
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # potion
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\potion_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 600, 570, 660, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 몬스터 도감
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_dogam_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 580, 580, 630, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 수집
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 640, 640, 680, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 분해
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 600, 600, 640, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        # 분해2
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 640, 570, 670, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        # 행성파견
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\hangsungpagyun_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        # 레이드 자동입장
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\jadong_in_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 570, 610, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        # 도전(행성파견, 성운돌파)
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\dojun_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        # 성운돌파
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\sungwoondolpa_yes.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0


def maul_go(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("maul_go")
        for i in range(3):
            result_out = out_check(cla)
            if result_out == True:
                break
            else:
                clean_screen(cla)
            time.sleep(0.5)

        maul_in = False
        maul_in_count = 0
        while maul_in is False:
            maul_in_count += 1
            if maul_in_count > 7:
                maul_in = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\gwangjang.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 50, 50, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                maul_in = True

            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\map_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\gardiun_tower_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 10, 150, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        for i in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\gwangjang.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 50, 50, 100, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("광장 도착", imgs_)
                                maul_in = True
                                break
                            else:
                                click_pos_2(940, 50, cla)
                            time.sleep(2)
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 560, 610, 610, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            x_reg = imgs_.x
                            y_reg = imgs_.y
                            for i in range(10):

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("loding")
                                    loading = True
                                    loading_count = 0
                                    while loading is True:
                                        loading_count += 1
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            print("loding", loading_count)
                                        else:
                                            loading = False
                                        time.sleep(1)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\gwangjang.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 50, 50, 100, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("광장 도착", imgs_)
                                    maul_in = True
                                    break
                                else:
                                    click_pos_reg(x_reg, y_reg, cla)
                                time.sleep(2)

                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\gardiun_tower.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 940, 120, 1010, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                for i in range(10):
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 560, 610, 610, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    time.sleep(0.2)

                else:
                    # 지도 클릭
                    click_pos_2(25, 50, cla)

                    time.sleep(0.3)

                    click_pos_2(65, 115, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\map_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
                    time.sleep(0.2)
        return maul_in


    except Exception as e:
        print(e)
        return 0

def loading_ares(cla):
    import numpy as np
    import cv2
    from function import imgs_set_

    try:
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("loding")
            loading = True
            loading_count = 0
            while loading is True:
                loading_count += 1
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("loding", loading_count)
                else:
                    loading = False
                time.sleep(1)
    except Exception as e:
        print(e)
        return 0



def map_in(cla):
    from function import click_pos_2
    try:
        clean_screen(cla)

        click_pos_2(25, 50, cla)
        time.sleep(0.5)
        click_pos_2(65, 115, cla)
    except Exception as e:
        print(e)
        return 0

