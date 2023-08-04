import sys
import time

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def main_grow_start(cla, schedule):
    from action_ares import confirm_all, dead_die
    try:
        print("main_grow_start")
        dead_die(cla, schedule)
        grow_main(cla, schedule)
        grow_skip(cla)
        grow_complete(cla)
        grow_explain(cla)
        confirm_all(cla)
    except Exception as e:
        print(e)
        return 0


def grow_main(cla, schedule):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from schedule import myQuest_play_add
    from action_ares import out_check

    try:
        print("grow_main")

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_challenge\\friend.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 300, 860, 360, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(935, 50, cla)

        result_out = out_check(cla)
        if result_out == True:
            drag_pos(405, 605, 805, 805, cla)
            time.sleep(1)


        file_path = "C:\\my_games\\ares\\data_ares\\imgs\\tuto\\main\\chaps\\chaps.txt"
        with open(file_path, "r", encoding='utf-8-sig') as file:
            read_chap = file.read().splitlines()

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_jejak\\friend.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 300, 860, 360, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(935, 50, cla)
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\x_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(915, 20, 960, 70, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        for i in range(len(read_chap)):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\main\\chaps\\" + read_chap[i] + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 60, 960, 100, cla, img, 0.77)
            if imgs_ is not None and imgs_ != False:
                print("chap", read_chap[i])
                v_.now_chabter = read_chap[i]
                x_reg = imgs_.x
                y_reg = imgs_.y
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\move\\move_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                if v_.now_chabter == "chap_2_1":
                    imgs_ = imgs_set_(880, 80, 960, 110, cla, img, 0.7)
                else:
                    imgs_ = imgs_set_(880, 80, 960, 170, cla, img, 0.7)
                if imgs_ is None:

                    result_ing = grow_quest_ing(cla)
                    if result_ing == False:
                        click_pos_reg(x_reg, y_reg, cla)
                        break
                        # if v_.now_chabter == "chap_2_1":
                        #     grow_sub(cla)
                        #
                        # else:
                        #
                        #     click_pos_reg(x_reg, y_reg, cla)
                        #     break



    except Exception as e:
        print(e)
        return 0



def grow_quest_ing(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg

    try:
        print("grow_quest_ing")
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
            if v_.now_chabter == "chap_2_1":
                imgs_ = imgs_set_(750, 70, 810, 110, cla, img, 0.7)
            else:
                imgs_ = imgs_set_(750, 70, 810, 180, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("quest_ing_1")
                ing_ = True
                ing_now = True
            time.sleep(0.1)
        return ing_now
    except Exception as e:
        print(e)
        return 0

def grow_skip(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("grow_skip")
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(840, 30, 960, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("skip_1")
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\skip_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(640, 470, 720, 570, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("skip_2")

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
                time.sleep(0.1)
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\skip_2_end.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(640, 410, 720, 570, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\skip\\level_up_skip.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(280, 620, 600, 1050, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)
        return 0

def grow_complete(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg

    try:
        print("grow_complete")
        # 퀘스트 완료
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\complete\\complete_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 500, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("complete_1")
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\complete\\complete_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 350, 550, 500, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("complete_3")
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\complete\\complete_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 350, 550, 500, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("complete_4")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\complete\\complete_5.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 350, 550, 500, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("complete_5")
                        click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        print(e)
        return 0


def grow_explain(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import out_check, bag_open
    from schedule import myQuest_play_add

    try:
        new_contents = False
        # 새로운 컨텐츠가 개방되었어요
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_hybdong\\new_contents.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 60, 940, 140, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(940, 50, cla)
            new_contents = True
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_1_7_hybdong\\quest_menu_open.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(880, 20, 960, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(940, 50, cla)
            new_contents = True
        # if new_contents == True:
        #     for i in range(10):
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_challenge\\friend.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 300, 860, 360, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(100, 230, cla)
            time.sleep(0.5)
            click_pos_2(100, 280, cla)
            time.sleep(0.5)
            click_pos_2(100, 330, cla)
            time.sleep(0.5)
                # else:
                #     break
                # time.sleep(0.5)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_raid\\chap_2_raid.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 520, 440, 570, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_sungwoondolpa\\sungwoondolpa_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 520, 570, 570, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_sungwoondolpa\\sungwoondolpa_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            for i in range(5):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_sungwoondolpa\\sungwoondolpa_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(940, 50, cla)
                else:
                    break
                time.sleep(0.3)


        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_raid\\chap_2_raid_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:

            for i in range(5):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_raid\\chap_2_raid_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(940, 50, cla)
                else:
                    break
                time.sleep(0.5)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_8_gigantomakia\\chap_2_1_8_gigantomakia.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(550, 520, 700, 570, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_8_gigantomakia\\gigantomakia_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_8_gigantomakia\\book.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(760, 990, 880, 1060, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                click_pos_2(335, 545, cla)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_8_gigantomakia\\book_cancle.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(760, 990, 880, 1060, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.2)
                click_pos_2(940, 50, cla)


            click_pos_2(335, 545, cla)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_daymos\\daymos_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(170, 520, 280, 570, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_daymos\\daymos_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            for i in range(5):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_daymos\\daymos_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(940, 50, cla)
                else:
                    break
                time.sleep(0.3)

        # chap_2_2_2 or chap_2_1_3
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_2_moria_giji\\chap_2_2_2_moria_giji.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 520, 450, 570, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_2_moria_giji\\moria_giji_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            for i in range(10):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_2_moria_giji\\moria_giji_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(940, 50, cla)
                else:
                    break
                time.sleep(0.2)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_7_shot\\chap_2_1_7_shot.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(370, 250, 590, 320, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x - 110, imgs_.y - 60, cla)
            print("수동으로만 가능")

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_select_dress\\select_dress_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 700, 1030, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x - 110, imgs_.y - 60, cla)
            v_.now_chabter = "chap_2_1_2"

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\sute\\sute_room_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 10, 90, 80, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(940, 50, cla)

        if v_.now_chabter == "chap_2_1_1" or v_.now_chabter == "chap_2_1_3":

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\region_quest_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("region_quest_title")
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\region_quest_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 560, 600, 610, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\region_quest_ing.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 100, 960, 330, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\region_quest_list.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(150, 100, 960, 330, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                    time.sleep(0.5)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\soolock.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(470, 620, 580, 660, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\photo_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(930, 530, cla)
            # 버스트 모드
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\burst\\burst_mode.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(810, 850, 960, 900, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("burst_mode")
                click_pos_reg(imgs_.x, imgs_.y, cla)
            # 도전
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_challenge\\friend.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 300, 860, 360, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_challenge\\challenge_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 170, 150, 270, cla, img, 0.77)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.1)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_challenge\\challenge_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(360, 530, cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_challenge\\hangsung_help_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_challenge\\hangsung_help_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(940, 50, cla)
                    else:
                        break
                    time.sleep(0.3)
        if v_.now_chabter == "chap_2_1_2" or v_.now_chabter == "chap_2_1_22":
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_select_dress\\select_dress_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 980, 950, 1040, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(130, 160, cla)
                time.sleep(0.2)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_select_dress\\dress_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 560, 610, 610, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_select_dress\\select_dress_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(670, 70, 850, 130, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(870, 55, cla)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_select_dress\\select_dress_22.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(820, 20, 910, 90, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_select_dress\\sute_room_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 50, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_select_dress\\sute_room_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_select_dress\\select_dress_4.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 700, 1030, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x - 110, imgs_.y - 60, cla)
                            # click_pos_2(150, 170, cla)
                            time.sleep(0.5)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_select_dress\\select_dress_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(200, 800, 800, 1000, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(535, 1005, cla)
                            time.sleep(0.5)

                        click_pos_2(915, 1015, cla)
                        time.sleep(0.5)
                        click_pos_2(940, 50, cla)
                        time.sleep(0.5)
                    else:
                        break
                    time.sleep(0.5)
        if v_.now_chabter == "chap_2_2_1" or v_.now_chabter == "chap_2_1_3":
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\gardiun_rank_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_1_gardiun_rank\\g_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(125, 55, 920, 120, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.7)

                    else:
                        click_pos_2(940, 50, cla)
                        time.sleep(1)
                        # 메이퀘스트 끝내기(수동조작)
                        myQuest_play_add(cla, "메인퀘스트")
                        break

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_1_gardiun_rank\\g_touch.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 610, 580, 660, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.7)

                    time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0





