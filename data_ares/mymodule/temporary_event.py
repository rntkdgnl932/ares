import sys
import time

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def event_dungeon_start(cla, dungeon):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg
    from action_ares import menu_open
    from potion_ares import juljun_potion_check
    try:
        print("event dungeon_start")

        dun_in = False

        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                # 먼저 event  dungeon 파악
                for k in range(3):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\event\\event_spot_" + str(k) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 50, 100, 90, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        where_event = "event_spot_" + str(i)

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_attack.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 400, 570, 470, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print(where_event)
                            dun_in = True
                            break
                break
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for o in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
        if dun_in == True:
            juljun_potion_check(cla)
        else:
            dungeon_in_event(cla, dungeon)


    except Exception as e:
        print(e)
        return  0


def dungeon_in_title(cla, dungeon):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg
    from action_ares import menu_open
    try:
        print("dungeon_in")

        where_dungeon = dungeon.split("_")

        menu_open(cla)

        if where_dungeon[0] == "이벤트":
            click_pos_2(70, 230, cla)
            title = "dojun_title"

        for i in range(10):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\" + str(title) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                break
            time.sleep(1)



    except Exception as e:
        print(e)
        return 0

def not_available(cla):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg
    from action_ares import out_check, clean_screen, confirm_all
    try:
        print("not_available")

        # 행성파견_1_1, 성운돌파_1_1, 레이드_1_1, 모리아기지_1

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\not_available.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 90, 500, 140, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            for i in range(5):
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(780, 60, cla)
                    time.sleep(1)
                    for z in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\quest_out_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 570, 600, 610, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            confirm_all(cla)
                            break
                        time.sleep(0.3)
                    break
                else:
                    clean_screen(cla)
                time.sleep(1)



    except Exception as e:
        print(e)
        return 0


def dungeon_in_event(cla, dungeon):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function import click_pos_2, imgs_set_, click_pos_reg
    from action_ares import menu_open, loading_ares, out_check, clean_screen
    from schedule import myQuest_play_add
    try:
        print("dungeon_in_event")

        # 이벤트 던전

        # ex) 이벤트_3_1

        where_dungeon = dungeon.split("_")

        dun_go_ = False
        dun_go_count = 0
        while dun_go_ is False:
            dun_go_count += 1
            if dun_go_count > 7:
                dun_go_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\event\\event_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("event dungeon")

                if int(where_dungeon[1]) > 4:
                    y_data = 4
                else:
                    y_data = int(where_dungeon[1])

                y_reg = 845 + (y_data * 35)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\event\\event_lock.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, y_reg - 20, 50, y_reg + 20, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print(int(where_dungeon[1]), imgs_)
                    # add 로 완료해버리기
                    myQuest_play_add(cla, dungeon)
                    dun_go_ = True

                else:
                    print("not event_lock", int(where_dungeon[1]))
                    # 자물쇠 없으니 클릭
                    click_pos_2(100, y_reg, cla)

                    time.sleep(0.5)
                    click_pos_2(865, 1015, cla)

                    time.sleep(0.1)
                    for i in range(10):

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\event\\event_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\already_moria.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(370, 80, 625, 150, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("이미 event dungeon에 있다.", dungeon)
                                # dun_go_ = True
                                for z in range(3):
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\event\\event_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(940, 50, cla)
                                    else:
                                        break
                                    time.sleep(0.5)
                                break
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_lack_time.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(450, 80, 550, 140, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("eent dungeon 끝", dungeon)
                                    dun_go_ = True

                                    myQuest_play_add(cla, dungeon)
                                    time.sleep(0.5)
                                    for z in range(3):
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\moria_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_2(940, 50, cla)
                                        else:
                                            break
                                        time.sleep(0.5)
                                    break

                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                loading_ares(cla)
                                break
                        time.sleep(0.5)
                    #입장완료 파악하기
                    print('event 입징완료')
                    if dun_go_ == False:
                        for x in range(10):
                            move_ = False

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_jadong_move.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 900, 1030, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                move_ = True
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_jadong_move2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 0, 900, 1030, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    move_ = True

                            if move_ == True:

                                for z in range(10):
                                    result_out = out_check(cla)
                                    if result_out == True:
                                        dun_go_ = True
                                        break
                                    else:
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_jadong_move.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(0, 0, 900, 1030, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_jadong_move2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(0, 0, 900, 1030, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)
                                break
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_map_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    # 랜덤 이동하도록 설정하기

                                    plus = 0

                                    if cla == "two":
                                        plus = 960
                                    if cla == "three":
                                        plus = 960 * 2
                                    if cla == "four":
                                        plus = 960 * 3

                                    for i in range(10):
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moglog_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(100, 85, 170, 135, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moglog_click.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(0, 85, 60, 300, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.5)
                                        time.sleep(0.5)

                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_spot_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 170, 100, 800, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        moria_spot = full_path
                                    else:
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_spot_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(30, 170, 100, 800, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            moria_spot = full_path

                                    last_i = 0

                                    full_path = moria_spot
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    for i in pyautogui.locateAllOnScreen(img, region=(30 + plus, 170, 70, 600),
                                                                         confidence=0.8):
                                        last_i += 1

                                    print("last_i", last_i)
                                    result_i = random.randint(0, int(last_i))

                                    last_i = 0

                                    full_path = moria_spot
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    for i in pyautogui.locateAllOnScreen(img, region=(30 + plus, 170, 70, 600),
                                                                         confidence=0.8):

                                        last_i += 1

                                        if last_i == result_i:
                                            last_x = i.left
                                            if cla == "two":
                                                last_x = last_x - 960
                                            if cla == "three":
                                                last_x = last_x - 960 - 960
                                            if cla == "four":
                                                last_x = last_x - 960 - 960 - 960
                                            last_y = i.top

                                            print("check point!!!!!!!!!!!!!", i, last_x, last_y)
                                            click_pos_2(last_x, last_y, cla)

                                        time.sleep(0.3)

                                    #
                                else:
                                    result_out = out_check(cla)
                                    if result_out == True:
                                        click_pos_2(25, 50, cla)
                                        time.sleep(0.5)
                                        click_pos_2(65, 115, cla)
                                        time.sleep(0.5)
                                    else:
                                        clean_screen(cla)
                            time.sleep(1)

                        if dun_go_ == True:

                            time.sleep(5)
                            for i in range(30):
                                result_out = out_check(cla)
                                if result_out == True:
                                    break
                                else:
                                    print("이동대기")
                                time.sleep(1)
                            # 여기에 이동 넣기
                            for i in range(30):
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_moving.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(815, 935, 915, 1030, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("타고 이동중")
                                else:
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\move_walking.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(815, 935, 915, 1030, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("걸어서 이동중")
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_on.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                    else:
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_on.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                time.sleep(1)

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("auto_on", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_off.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("auto_off", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)
                            # 절전모드
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        for i in range(10):
                            result_out = out_check(cla)
                            if result_out == True:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_on.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("auto_on", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.1)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_off.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("auto_off", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)
                                # 절전모드
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            time.sleep(1)

                time.sleep(0.1)



            else:
                # 행성파견_1_1, 성운돌파_1_1, 레이드_1_1, 모리아기지_1

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\dojun_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(760, 500, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\event\\event_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(1)

                else:
                    menu_open(cla)

                    click_pos_2(70, 230, cla)

                    for i in range(10):

                        not_available(cla)

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\dojun_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.7)
            time.sleep(1)

        # 밖으로 나가기
        for i in range(10):
            exit_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\dojun_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 50, cla)
                time.sleep(1)
                exit_ = False
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\event\\event_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 50, cla)
                time.sleep(1)
                exit_ = False
            if exit_ == True:
                break
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0
