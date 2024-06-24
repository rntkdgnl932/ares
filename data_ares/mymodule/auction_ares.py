import time
# import os
import sys

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def auction_start(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, mouse_move_cpp, click_pos_2
    from action_ares import menu_open
    try:
        print("auction_start")
        auc_complete = False
        auc_complete_count = 0
        while auc_complete is False:
            auc_complete_count += 1
            print("auc_complete_count", auc_complete_count)
            if auc_complete_count > 4:
                auc_complete = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\auction_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:

                auc_complete = True

                print("auction_title : 진입완료")
                auction_ready(cla)
                auction_sell(cla)



            else:

                menu_open(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\auction_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(810, 255, cla)
                    time.sleep(1)

            time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\auction_title.PNG"
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

def auction_ready(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, mouse_move_cpp, click_pos_2
    from action_ares import menu_open
    try:
        print("auction_start")
        auc_complete = False
        auc_complete_count = 0
        while auc_complete is False:
            auc_complete_count += 1
            print("auc_complete_count", auc_complete_count)
            if auc_complete_count > 4:
                auc_complete = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\auction_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:



                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\auction_etc.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(880, 140, 940, 180, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    auc_complete = True
                    time.sleep(0.5)
                else:
                    click_pos_2(250, 100, cla)
                    time.sleep(0.5)
                    click_pos_2(900, 160, cla)
                    time.sleep(0.2)
                    mouse_move_cpp(500, 300, cla)
                    time.sleep(0.2)

                time.sleep(0.5)
            else:
                menu_open(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\auction_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(810, 255, cla)
                    time.sleep(1)

            time.sleep(1)

    except Exception as e:
        print(e)
        return 0

def auction_sell(cla):
    import numpy as np
    import cv2
    import os
    from function import imgs_set_, click_pos_reg, mouse_move_cpp, click_pos_2, int_put_, in_number_check, text_check_get
    from action_ares import menu_open
    from property_ares import my_property_upload
    try:
        print("auction_sell")
        auc_complete = False
        auc_complete_count = 0
        while auc_complete is False:
            auc_complete_count += 1
            print("auc_complete_count", auc_complete_count)
            if auc_complete_count > 4:
                auc_complete = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\auction_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                auc_complete = True



                click_pos_2(580, 1015, cla)
                time.sleep(0.5)

                # click_pos_2(660, 1015, cla)
                # time.sleep(0.5)

                for i in range(3):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\ilgwal_hoisoo.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(440, 440, 520, 500, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\ilgwal_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 560, 610, 620, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)
                            break
                    else:
                        click_pos_2(660, 1015, cla)
                        time.sleep(0.5)
                    time.sleep(0.5)

                # 시작 전에 거래소 재화 서버 업로드
                my_property_upload(cla)

                # 시작
                file_path_0 = "C:\\my_games\\ares\\data_ares\\imgs\\auction\\auction_list_0.txt"
                file_path_1 = "C:\\my_games\\ares\\data_ares\\imgs\\auction\\auction_list_1.txt"
                file_path_2 = "C:\\my_games\\ares\\data_ares\\imgs\\auction\\auction_list_2.txt"
                with open(file_path_0, "r", encoding='utf-8-sig') as file:
                    auction_list_0 = file.read().splitlines()
                with open(file_path_1, "r", encoding='utf-8-sig') as file:
                    auction_list_1 = file.read().splitlines()
                with open(file_path_2, "r", encoding='utf-8-sig') as file:
                    auction_list_2 = file.read().splitlines()

                # 기타 재료 등등

                # click_pos_2(800, 125, cla)
                time.sleep(1)

                for i in range(len(auction_list_1)):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\list\\" + auction_list_1[i] + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(765, 165, 960, 1010, cla, img, 0.93)
                    if imgs_ is not None and imgs_ != False:
                        x_reg = imgs_.x
                        y_reg = imgs_.y
                        click_pos_reg(x_reg, y_reg, cla)
                        for c in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\dnglock_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(780, 1000, 950, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.1)

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\dnglock_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(780, 1000, 950, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:

                            sell_ = False
                            sell_count = 0
                            while sell_ is False:
                                sell_count += 1
                                if sell_count > 4:
                                    sell_ = True
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(440, 370, 520, 410, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sell_ = True

                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\10.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(545, 465, 670, 500, cla, img, 0.97)
                                    if imgs_ is not None and imgs_ != False:
                                        print("10", imgs_)
                                        click_pos_2(405, 675, cla)
                                    else:
                                        print("not 10")

                                        last_sell_ = False
                                        last_sell_count = 0
                                        while last_sell_ is False:
                                            last_sell_count += 1
                                            if last_sell_count > 4:
                                                last_sell_ = True
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_confirm_title.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(440, 410, 520, 450, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                last_sell_ = True
                                                click_pos_2(535, 635, cla)
                                            else:
                                                click_pos_2(555, 675, cla)
                                                for z in range(10):
                                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_confirm_title.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(440, 410, 520, 450, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        break
                                                    time.sleep(0.5)
                                            time.sleep(0.5)
                                else:
                                    click_pos_reg(x_reg, y_reg, cla)
                                    time.sleep(0.5)
                                    click_pos_2(905, 1015, cla)
                                    for z in range(10):
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(440, 370, 520, 410, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        time.sleep(0.5)
                                time.sleep(0.5)

                            time.sleep(1)
                # 전체 클릭
                click_pos_2(790, 120, cla)
                time.sleep(1)

                for i in range(len(auction_list_2)):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\list\\" + auction_list_2[i] + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(765, 165, 960, 1010, cla, img, 0.93)
                    if imgs_ is not None and imgs_ != False:
                        x_reg = imgs_.x
                        y_reg = imgs_.y
                        click_pos_reg(x_reg, y_reg, cla)
                        time.sleep(1)

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\dnglock_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(780, 1000, 950, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:

                            sell_ = False
                            sell_count = 0
                            while sell_ is False:
                                sell_count += 1
                                if sell_count > 4:
                                    sell_ = True
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(440, 370, 520, 410, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sell_ = True
                                    print("무슨물건?", auction_list_2[i])
                                    # re_ = text_check_get(589, 477, 625, 492, cla)
                                    # result_int = int_put_(re_)
                                    # result_num = in_number_check(cla, result_int)

                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\10.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(545, 465, 670, 500, cla, img, 0.97)
                                    if imgs_ is not None and imgs_ != False:
                                        print("10", imgs_)
                                        click_pos_2(405, 675, cla)
                                    else:
                                        print("not 10")
                                        last_sell_ = False
                                        last_sell_count = 0
                                        while last_sell_ is False:
                                            last_sell_count += 1
                                            if last_sell_count > 4:
                                                last_sell_ = True
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_confirm_title.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(440, 410, 520, 450, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                last_sell_ = True
                                                click_pos_2(535, 635, cla)
                                            else:
                                                click_pos_2(555, 675, cla)
                                                for z in range(10):
                                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_confirm_title.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(440, 410, 520, 450, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        break
                                                    time.sleep(0.5)
                                            time.sleep(0.5)
                                else:
                                    click_pos_reg(x_reg, y_reg, cla)
                                    time.sleep(0.5)
                                    click_pos_2(905, 1015, cla)
                                    for z in range(10):
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(440, 370, 520, 410, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        time.sleep(0.5)
                                time.sleep(0.5)

                            time.sleep(1)
                print("무기")
                # 무기

                mouse_move_cpp(500, 300, cla)
                time.sleep(1)


                for i in range(len(auction_list_1)):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\list\\" + auction_list_0[i] + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(765, 165, 960, 1010, cla, img, 0.93)
                    if imgs_ is not None and imgs_ != False:

                        for z in range(5):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\list\\" + auction_list_0[
                                i] + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(765, 165, 960, 1010, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:

                                x_reg = imgs_.x
                                y_reg = imgs_.y
                                click_pos_reg(x_reg, y_reg, cla)
                                time.sleep(1)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\dnglock_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(780, 1000, 950, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:

                                    sell_ = False
                                    sell_count = 0
                                    while sell_ is False:
                                        sell_count += 1
                                        if sell_count > 4:
                                            sell_ = True
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(440, 370, 520, 410, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            sell_ = True

                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\10.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(545, 465, 670, 500, cla, img, 0.97)
                                            if imgs_ is not None and imgs_ != False:
                                                print("10", imgs_)
                                                click_pos_2(405, 675, cla)
                                            else:
                                                print("not 10")

                                                last_sell_ = False
                                                last_sell_count = 0
                                                while last_sell_ is False:
                                                    last_sell_count += 1
                                                    if last_sell_count > 4:
                                                        last_sell_ = True
                                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_confirm_title.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(440, 410, 520, 450, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        last_sell_ = True
                                                        click_pos_2(535, 635, cla)
                                                    else:
                                                        click_pos_2(555, 675, cla)
                                                        for z in range(10):
                                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_confirm_title.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(440, 410, 520, 450, cla, img, 0.8)
                                                            if imgs_ is not None and imgs_ != False:
                                                                break
                                                            time.sleep(0.5)
                                                    time.sleep(0.5)
                                        else:
                                            click_pos_reg(x_reg, y_reg, cla)
                                            time.sleep(0.5)
                                            click_pos_2(905, 1015, cla)
                                            for c in range(10):
                                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_title.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(440, 370, 520, 410, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    break
                                                time.sleep(0.5)
                                        time.sleep(0.5)

                                    time.sleep(1)
                            else:
                                break
                            time.sleep(1)

            else:

                menu_open(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\auction_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(810, 255, cla)
                    time.sleep(0.5)

            time.sleep(1)

    except Exception as e:
        print(e)
        return 0

def auction_sell_folder(cla):
    import numpy as np
    import cv2
    import os
    from function import imgs_set_, click_pos_reg, mouse_move_cpp, click_pos_2, int_put_, in_number_check, text_check_get
    from action_ares import menu_open
    from property_ares import my_property_upload
    try:
        print("auction_sell_folder")
        auc_complete = False
        auc_complete_count = 0
        while auc_complete is False:
            auc_complete_count += 1
            print("auc_complete_count", auc_complete_count)
            if auc_complete_count > 4:
                auc_complete = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\auction_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                auc_complete = True



                click_pos_2(580, 1015, cla)
                time.sleep(0.5)

                # click_pos_2(660, 1015, cla)
                # time.sleep(0.5)

                for i in range(3):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\ilgwal_hoisoo.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(440, 440, 520, 500, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\ilgwal_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 560, 610, 620, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)
                            break
                    else:
                        click_pos_2(660, 1015, cla)
                        time.sleep(0.5)
                    time.sleep(0.5)

                # 시작 전에 거래소 재화 서버 업로드
                my_property_upload(cla)

                # 시작
                file_path_0 = "C:\\my_games\\ares\\data_ares\\imgs\\auction\\auction_list_0.txt"
                file_path_1 = "C:\\my_games\\ares\\data_ares\\imgs\\auction\\auction_list_1.txt"
                file_path_2 = "C:\\my_games\\ares\\data_ares\\imgs\\auction\\auction_list_2.txt"
                with open(file_path_0, "r", encoding='utf-8-sig') as file:
                    auction_list_0 = file.read().splitlines()
                with open(file_path_1, "r", encoding='utf-8-sig') as file:
                    auction_list_1 = file.read().splitlines()
                with open(file_path_2, "r", encoding='utf-8-sig') as file:
                    auction_list_2 = file.read().splitlines()

                # 기타 재료 등등

                # click_pos_2(800, 125, cla)
                time.sleep(1)

                for i in range(len(auction_list_1)):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\list\\" + auction_list_1[i] + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(765, 165, 960, 1010, cla, img, 0.93)
                    if imgs_ is not None and imgs_ != False:
                        x_reg = imgs_.x
                        y_reg = imgs_.y
                        click_pos_reg(x_reg, y_reg, cla)
                        for c in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\dnglock_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(780, 1000, 950, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.1)

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\dnglock_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(780, 1000, 950, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:

                            sell_ = False
                            sell_count = 0
                            while sell_ is False:
                                sell_count += 1
                                if sell_count > 4:
                                    sell_ = True
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(440, 370, 520, 410, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sell_ = True

                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\10.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(545, 465, 670, 500, cla, img, 0.97)
                                    if imgs_ is not None and imgs_ != False:
                                        print("10", imgs_)
                                        click_pos_2(405, 675, cla)
                                    else:
                                        print("not 10")

                                        last_sell_ = False
                                        last_sell_count = 0
                                        while last_sell_ is False:
                                            last_sell_count += 1
                                            if last_sell_count > 4:
                                                last_sell_ = True
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_confirm_title.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(440, 410, 520, 450, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                last_sell_ = True
                                                click_pos_2(535, 635, cla)
                                            else:
                                                click_pos_2(555, 675, cla)
                                                for z in range(10):
                                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_confirm_title.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(440, 410, 520, 450, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        break
                                                    time.sleep(0.5)
                                            time.sleep(0.5)
                                else:
                                    click_pos_reg(x_reg, y_reg, cla)
                                    time.sleep(0.5)
                                    click_pos_2(905, 1015, cla)
                                    for z in range(10):
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(440, 370, 520, 410, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        time.sleep(0.5)
                                time.sleep(0.5)

                            time.sleep(1)
                # 전체 클릭
                click_pos_2(790, 120, cla)
                time.sleep(1)

                for i in range(len(auction_list_2)):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\list\\" + auction_list_2[i] + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(765, 165, 960, 1010, cla, img, 0.93)
                    if imgs_ is not None and imgs_ != False:
                        x_reg = imgs_.x
                        y_reg = imgs_.y
                        click_pos_reg(x_reg, y_reg, cla)
                        time.sleep(1)

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\dnglock_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(780, 1000, 950, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:

                            sell_ = False
                            sell_count = 0
                            while sell_ is False:
                                sell_count += 1
                                if sell_count > 4:
                                    sell_ = True
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(440, 370, 520, 410, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sell_ = True
                                    print("무슨물건?", auction_list_2[i])
                                    # re_ = text_check_get(589, 477, 625, 492, cla)
                                    # result_int = int_put_(re_)
                                    # result_num = in_number_check(cla, result_int)

                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\10.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(545, 465, 670, 500, cla, img, 0.97)
                                    if imgs_ is not None and imgs_ != False:
                                        print("10", imgs_)
                                        click_pos_2(405, 675, cla)
                                    else:
                                        print("not 10")
                                        last_sell_ = False
                                        last_sell_count = 0
                                        while last_sell_ is False:
                                            last_sell_count += 1
                                            if last_sell_count > 4:
                                                last_sell_ = True
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_confirm_title.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(440, 410, 520, 450, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                last_sell_ = True
                                                click_pos_2(535, 635, cla)
                                            else:
                                                click_pos_2(555, 675, cla)
                                                for z in range(10):
                                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_confirm_title.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(440, 410, 520, 450, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        break
                                                    time.sleep(0.5)
                                            time.sleep(0.5)
                                else:
                                    click_pos_reg(x_reg, y_reg, cla)
                                    time.sleep(0.5)
                                    click_pos_2(905, 1015, cla)
                                    for z in range(10):
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(440, 370, 520, 410, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        time.sleep(0.5)
                                time.sleep(0.5)

                            time.sleep(1)
                print("무기")
                # 무기

                mouse_move_cpp(500, 300, cla)
                time.sleep(1)


                for i in range(len(auction_list_1)):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\list\\" + auction_list_0[i] + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(765, 165, 960, 1010, cla, img, 0.93)
                    if imgs_ is not None and imgs_ != False:

                        for z in range(5):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\list\\" + auction_list_0[
                                i] + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(765, 165, 960, 1010, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:

                                x_reg = imgs_.x
                                y_reg = imgs_.y
                                click_pos_reg(x_reg, y_reg, cla)
                                time.sleep(1)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\dnglock_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(780, 1000, 950, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:

                                    sell_ = False
                                    sell_count = 0
                                    while sell_ is False:
                                        sell_count += 1
                                        if sell_count > 4:
                                            sell_ = True
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(440, 370, 520, 410, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            sell_ = True

                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\10.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(545, 465, 670, 500, cla, img, 0.97)
                                            if imgs_ is not None and imgs_ != False:
                                                print("10", imgs_)
                                                click_pos_2(405, 675, cla)
                                            else:
                                                print("not 10")

                                                last_sell_ = False
                                                last_sell_count = 0
                                                while last_sell_ is False:
                                                    last_sell_count += 1
                                                    if last_sell_count > 4:
                                                        last_sell_ = True
                                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_confirm_title.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(440, 410, 520, 450, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        last_sell_ = True
                                                        click_pos_2(535, 635, cla)
                                                    else:
                                                        click_pos_2(555, 675, cla)
                                                        for z in range(10):
                                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_confirm_title.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(440, 410, 520, 450, cla, img, 0.8)
                                                            if imgs_ is not None and imgs_ != False:
                                                                break
                                                            time.sleep(0.5)
                                                    time.sleep(0.5)
                                        else:
                                            click_pos_reg(x_reg, y_reg, cla)
                                            time.sleep(0.5)
                                            click_pos_2(905, 1015, cla)
                                            for c in range(10):
                                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_title.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(440, 370, 520, 410, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    break
                                                time.sleep(0.5)
                                        time.sleep(0.5)

                                    time.sleep(1)
                            else:
                                break
                            time.sleep(1)

            else:

                menu_open(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\auction_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(810, 255, cla)
                    time.sleep(0.5)

            time.sleep(1)

    except Exception as e:
        print(e)
        return 0


