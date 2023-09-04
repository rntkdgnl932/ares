import sys
import time

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def soojib_boonhae_start(cla):
    try:
        print("soojib_boonhae_start")
        soojib(cla)
        time.sleep(0.2)
        boonhae_start(cla)
    except Exception as e:
        print(e)
        return 0


def soojib(cla):
    import numpy as np
    import cv2

    from action_ares import menu_open
    from function import click_pos_2, imgs_set_
    try:
        print("soojib")

        collection_ = False
        collection_count = 0
        while collection_ is False:
            collection_count += 1
            print("collection_count", collection_count)
            if collection_count > 15:
                collection_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\soojib_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("soojib_title : 진입완료")

                collection_ = True


                # 이벤트

                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(90, 260, 115, 310, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(65, 285, cla)
                    time.sleep(0.5)

                soojib_start(cla)

                time.sleep(0.2)

                # 전체
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(90, 105, 115, 155, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(65, 130, cla)
                    time.sleep(0.5)

                time.sleep(0.2)


                for i in range(4):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(210, 990, 250, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("조건설정 on")
                        soojib_start(cla)
                        break
                    else:
                        print("조건설정 off")
                        soojib_setting(cla)
                        time.sleep(0.5)
                    time.sleep(0.5)


            else:

                menu_open(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\soojib_title.PNG"
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
                            imgs_ = imgs_set_(920, 80, 960, 120, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                ispoint = True
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\menu_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(920, 80, 960, 120, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    ispoint = True

                            if ispoint == True:
                                click_pos_2(930, 110, cla)
                            else:
                                collection_ = True
                                break
                    time.sleep(1)

            time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\soojib_title.PNG"
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
        return  0


def soojib_setting(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, mouse_move_cpp
    try:
        print("soojib_setting")

        collection_setting_ = False
        collection_setting_count = 0
        while collection_setting_ is False:
            collection_setting_count += 1
            if collection_setting_count > 7:
                collection_setting_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 640, 640, 680, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("soojib_setting_confirm", imgs_)

                soojib_setting_complete = False

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_c_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(310, 430, 380, 470, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("soojib_setting_c_on", imgs_)
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_b_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 430, 440, 470, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("soojib_setting_b_on", imgs_)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_all_on.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(255, 475, 325, 525, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("soojib_setting_all_on", imgs_)
                            soojib_setting_complete = True

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_a_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 430, 500, 470, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_s_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(490, 430, 560, 470, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_r_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(540, 430, 610, 470, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)

                        else:
                            print("not soojib_setting_all_on")
                    else:
                        print("not soojib_setting_b_on")
                else:
                    print("not soojib_setting_c_on")

                print("soojib_setting_complete", soojib_setting_complete)

                if soojib_setting_complete == False:

                    # 우선 비어있는 자리 체크부터 하기
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_c_off.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(310, 430, 380, 470, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_b_off.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 430, 440, 470, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_all_off.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(255, 475, 325, 525, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                    mouse_move_cpp(480, 840, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 640, 640, 680, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        collection_setting_ = True
                time.sleep(0.5)

            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_off.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(120, 990, 250, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

            time.sleep(1)



    except Exception as e:
        print(e)
        return 0

def soojib_start(cla):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg
    from action_ares import confirm_all
    try:
        print("soojib_start")

        collection_start_ = False
        collection_start_count = 0
        while collection_start_ is False:
            collection_start_count += 1
            if collection_start_count > 50:
                collection_start_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\no_again_look.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(430, 600, 550, 650, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
                confirm_all(cla)
                time.sleep(0.5)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 640, 640, 680, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("soojib_start : soojib_setting_confirm", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)
            else:

                click_ready = False

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_click_point3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 120, 770, 770, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    click_ready = True
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_click_point2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 120, 770, 770, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        click_ready = True
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_click_point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 120, 770, 770, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            click_ready = True
                time.sleep(0.2)
                if click_ready == True:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\no_again_look.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(430, 600, 550, 650, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        confirm_all(cla)
                        time.sleep(0.5)


                    click_pos_2(915, 1015, cla)
                else:
                    collection_start_ = True
                    # # 이건 어차피 A 등급 이상 있으면 반복되는 상황...그래서 삭제 예정
                    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_all_point.PNG"
                    # img_array = np.fromfile(full_path, np.uint8)
                    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    # imgs_ = imgs_set_(80, 65, 115, 100, cla, img, 0.8)
                    # if imgs_ is not None and imgs_ != False:
                    #     print("soojib_all_point", imgs_)
                    #     click_pos_2(155, 95, cla)
                    #     time.sleep(0.2)
                    #     click_pos_2(55, 95, cla)
                    #     time.sleep(0.5)
                    # else:
                    #     collection_start_ = True
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0


def boonhae_start(cla):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg
    from action_ares import menu_open
    try:
        print("boonhae_start")
        boonhae_complete = False
        boonhae_complete_count = 0
        while boonhae_complete is False:
            boonhae_complete_count += 1
            print("boonhae_complete_count", boonhae_complete_count)
            if boonhae_complete_count > 4:
                boonhae_complete = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\invenroty_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("invenroty_title : 진입완료")

                boonhae_complete = True

                # 분해 전 착용
                boonhae_ready(cla)

                # 무기 분해
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(80, 80, 120, 125, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(50, 110, cla)
                    time.sleep(0.5)

                boonhae_moogi(cla)
                time.sleep(0.5)
                # 성물 분해
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(80, 115, 120, 165, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(50, 145, cla)
                    time.sleep(0.5)

                boonhae_sungmool(cla)


            else:

                menu_open(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\invenroty_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(900, 50, cla)
                    time.sleep(1)

            time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\invenroty_title.PNG"
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


def boonhae_ready(cla):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg, mouse_move_cpp
    from action_ares import menu_open
    try:
        print("boonhae_ready")
        boonhae_complete = False
        boonhae_complete_count = 0
        while boonhae_complete is False:
            boonhae_complete_count += 1
            print("boonhae_complete_count", boonhae_complete_count)
            if boonhae_complete_count > 4:
                boonhae_complete = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\invenroty_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("invenroty_title : 진입완료")



                # 슈트룸
                click_pos_2(905, 50, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\suit_room_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)

                # 첫번째 슈트
                click_pos_2(40, 180, cla)
                time.sleep(0.5)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\suitroom_jadongjangchak.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 640, 260, 680, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

                # 두번째 슈트
                click_pos_2(95, 180, cla)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\suitroom_jadongjangchak.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 640, 260, 680, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

                # 세번째 슈트
                click_pos_2(150, 180, cla)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\suitroom_jadongjangchak.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 640, 260, 680, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\suit_room_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
                    mouse_move_cpp(420, 675, cla)
                    time.sleep(0.2)
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\invenroty_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            boonhae_complete = True
                            break
                        time.sleep(0.5)





            else:

                menu_open(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\invenroty_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(900, 50, cla)
                    time.sleep(1)

            time.sleep(1)



    except Exception as e:
        print(e)
        return 0



def boonhae_moogi(cla):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg
    from action_ares import menu_open
    try:
        print("boonhae_moogi")
        boonhae_complete = False
        boonhae_complete_count = 0
        while boonhae_complete is False:
            boonhae_complete_count += 1
            print("boonhae_complete_count", boonhae_complete_count)
            if boonhae_complete_count > 4:
                boonhae_complete = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\invenroty_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("invenroty_title : 진입완료")

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_last_click_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 990, 930, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("분해 진행")
                    # 마무리하기

                    for z in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 570, 570, 610, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            boonhae_complete = True
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_last_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(440, 390, 510, 430, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(500, 640, 570, 670, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                click_pos_2(865, 1015, cla)
                                time.sleep(0.5)
                            time.sleep(0.5)
                        time.sleep(0.5)



                    
                else:
                    print("일괄분해 누른 후 셋팅하기")
                    boonhae_setting_bc(cla)
                    time.sleep(1)

                    is_on = False

                    for i in range(6):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_last_click_on.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 990, 930, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            is_on = True
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\no_select_item.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(790, 520, 930, 570, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                is_on = True
                                boonhae_complete = True
                                break
                        time.sleep(0.5)
                    if is_on == False:
                        boonhae_complete_count += 2
                    time.sleep(1)


            else:

                menu_open(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\invenroty_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(900, 50, cla)
                    time.sleep(1)

            time.sleep(1)



    except Exception as e:
        print(e)
        return 0


def boonhae_setting_bc(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, mouse_move_cpp
    try:
        print("boonhae_setting")
        boonhae_set_complete = False
        boonhae_complete_count = 0
        while boonhae_set_complete is False:
            boonhae_complete_count += 1
            print("boonhae_complete_count", boonhae_complete_count)
            if boonhae_complete_count > 15:
                boonhae_set_complete = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 600, 600, 640, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("boonhae_confirm", imgs_)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_setting_b_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 470, 420, 510, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_setting_c_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 470, 370, 510, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        last_set = True
                        for i in range(5):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(405, 470, 630, 510, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("checked", imgs_)
                                last_set = False
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                print("not checked")
                                break
                            time.sleep(0.5)

                        if last_set == True:
                            boonhae_set_complete = True

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_setting_b_off.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 470, 420, 510, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_setting_c_off.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 470, 370, 510, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

                mouse_move_cpp(480, 840, cla)
                time.sleep(0.5)

            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_select.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(130, 990, 240, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                else:
                    print("일괄분해 누른 후 셋팅하기")
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\ilgwal_boonhae.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(640, 990, 750, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 600, 600, 640, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0


def boonhae_sungmool(cla):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg
    from action_ares import menu_open
    try:
        print("boonhae_sungmool")
        boonhae_complete = False
        boonhae_complete_count = 0
        while boonhae_complete is False:
            boonhae_complete_count += 1
            print("boonhae_complete_count", boonhae_complete_count)
            if boonhae_complete_count > 4:
                boonhae_complete = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\invenroty_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("invenroty_title : 진입완료")

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_last_click_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 990, 930, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("분해 진행")
                    # 마무리하기

                    for z in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 570, 570, 610, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            boonhae_complete = True
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_last_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(440, 390, 510, 430, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(500, 640, 570, 670, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                click_pos_2(865, 1015, cla)
                                time.sleep(0.5)
                            time.sleep(0.5)
                        time.sleep(0.5)


                else:
                    print("일괄분해 누른 후 셋팅하기")
                    boonhae_setting_c(cla)
                    time.sleep(1)

                    is_on = False

                    for i in range(6):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_last_click_on.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 990, 930, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            is_on = True
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\no_select_item.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(790, 520, 930, 570, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                is_on = True
                                boonhae_complete = True
                                break
                        time.sleep(0.5)
                    if is_on == False:
                        boonhae_complete_count += 2
                    time.sleep(1)


            else:

                menu_open(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\invenroty_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(900, 50, cla)
                    time.sleep(1)

            time.sleep(1)



    except Exception as e:
        print(e)
        return 0

def boonhae_setting_c(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, mouse_move_cpp
    try:
        print("boonhae_setting")
        boonhae_set_complete = False
        boonhae_complete_count = 0
        while boonhae_set_complete is False:
            boonhae_complete_count += 1
            print("boonhae_complete_count", boonhae_complete_count)
            if boonhae_complete_count > 15:
                boonhae_set_complete = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 570, 600, 620, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("boonhae_confirm", imgs_)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_setting_c_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 480, 370, 540, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_setting_b_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 480, 420, 540, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:


                        last_set = True
                        for i in range(5):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(410, 490, 630, 540, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("checked", imgs_)
                                last_set = False
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                print("not checked")
                                break
                            time.sleep(0.5)

                        if last_set == True:
                            boonhae_set_complete = True

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_setting_c_off.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 480, 370, 540, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_setting_b_off.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 480, 420, 540, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

                mouse_move_cpp(480, 840, cla)
                time.sleep(0.5)

            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_select.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(130, 990, 240, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                else:
                    print("일괄분해 누른 후 셋팅하기")
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\ilgwal_boonhae.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(640, 990, 750, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 570, 600, 620, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0

