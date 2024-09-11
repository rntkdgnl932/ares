import time
# import os
import sys


sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def _stop_please(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("_stop_please")

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



