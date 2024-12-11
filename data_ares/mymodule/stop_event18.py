import time
# import os
import sys


sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def _stop_please(cla):
    import numpy as np
    import cv2
    import os
    from function import imgs_set_, click_pos_reg, click_pos_2
    from massenger import line_to_me
    try:
        print("_stop_please")

        is_update = False

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\download.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 500, 620, 600, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("download", imgs_)
            is_update = True
            click_pos_2(480, 590, cla)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\downloading.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 1000, 100, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("downloading", imgs_)
            is_update = True

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\resource_loading.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(370, 880, 540, 930, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("resource_loading", imgs_)
            is_update = True

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\screen_touch.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(370, 880, 540, 930, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("screen_touch", imgs_)
            is_update = True

        is_update_count = 0
        is_update_counting = 0
        while is_update is True:
            is_update_count += 1
            if is_update_count > 7200:
                why = "업뎃한지 두시간이 지나버렸다...꺼버리겠다..."
                line_to_me(cla, why)

                dir_path = "C:\\my_games\\load\\ares"
                file_path = dir_path + "\\start.txt"
                # cla.txt
                cla_data = str(cla) + "cla"
                file_path2 = dir_path + "\\" + cla_data + ".txt"
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    data = 'no'
                    file.write(str(data))
                    time.sleep(0.2)
                with open(file_path2, "w", encoding='utf-8-sig') as file:
                    data = cla
                    file.write(str(data))
                    time.sleep(0.2)
                os.execl(sys.executable, sys.executable, *sys.argv)

            elif is_update_count > 3600:
                why = "업뎃한지 한시간이 지나버렸다..."
                line_to_me(cla, why)
            is_update_counting += 1

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\character_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 110, 80, v_.now_cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                is_update = False
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\download.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 500, 620, 600, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("download", is_update_counting, "초")
                    click_pos_2(480, 590, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\downloading.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 1000, 100, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("downloading", is_update_counting, "초")
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\resource_loading.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(370, 880, 540, 930, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("resource_loading", is_update_counting, "초")
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\screen_touch.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(370, 880, 540, 930, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("screen_touch", is_update_counting, "초")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                print("update...ing...", is_update_counting, "초")

            time.sleep(1)

        stop = True
        stop_count = 0
        while stop is True:
            stop_count += 1
            if stop_count > 5:
                stop = False
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\18_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("18_1")
                stop_count = 0
                click_pos_reg(imgs_.x, imgs_.y, cla)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\18_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("18_2")
                stop_count = 0
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\plz_stop18.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 800, 700, 1000, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("plz_stop18")
                stop_count = 0
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\server_update.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 500, 560, 560, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(480, 590, cla)
                stop = False

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\season_start.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(320, 340, 440, 400, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("season_start")
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\season_start2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 460, 530, 510, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("season_start2")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\season_start3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(320, 330, 440, 410, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("season_start3")
                        click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sohwan__confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 970, 700, 1050, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.2)

            # 아이템 기간 만료료
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\manlyo.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(420, 380, 530, 420, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\manlyo_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 640, 530, 680, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\manlyo_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 500, 530, 800, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.2)

            time.sleep(0.2)

    except Exception as e:
        print(e)
        return 0



