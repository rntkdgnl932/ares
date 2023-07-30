import sys
import time
import requests

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_

def go_test():
    import numpy as np
    import cv2
    import pyautogui
    from function import imgs_set_, mouse_move_cpp, drag_pos_Press, drag_pos_Release, click_pos_2, click_pos_reg, how_many_pic
    from get_items import get_event, get_post, get_gardiun_pass, get_gardiun_rank, bag_item_open

    print("tst")
    cla = "one"

    burst_mode_action_right = True

    mouse_move_cpp(180, 505, cla)
    # 0.2초
    time.sleep(0.2)
    # 마우스 누르기
    drag_pos_Press()
    # 0.2초
    time.sleep(0.2)

    for i in range(10):

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\burst\\ares_right_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1050, cla, img, 0.7)
        if imgs_ is not None:
            burst_mode_action_right = False
        else:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\burst\\ares_right_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1050, cla, img, 0.7)
            if imgs_ is not None:
                burst_mode_action_right = False
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\burst\\ares_left_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1050, cla, img, 0.7)
        if imgs_ is not None:
            burst_mode_action_right = True
        else:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\burst\\ares_left_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1050, cla, img, 0.7)
            if imgs_ is not None:
                burst_mode_action_right = True
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\burst\\ares_left_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1050, cla, img, 0.7)
                if imgs_ is not None:
                    burst_mode_action_right = True
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\burst\\ares_left_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1050, cla, img, 0.7)
                    if imgs_ is not None:
                        burst_mode_action_right = True

        if burst_mode_action_right == True:
            x_reg = 180 + (i * 60)
            # 마우스 이동
            mouse_move_cpp(x_reg, 505, cla)
        else:
            break
    # 마우스 떼기
    drag_pos_Release()
    # 0.2초
    time.sleep(0.2)

    # address = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
    # result_many = how_many_pic(270, 370, 310, 700, address, cla)
    # print("result_many", result_many)

    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\main\\chap_1\\chap_1_00.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(700, 30, 960, 260, cla, img, 0.77)
    # if imgs_ is not None:
    #     print("보여", imgs_)
    # else:
    #     print("안보여")

    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\move\\move_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(700, 30, 960, 130, cla, img, 0.7)
    # if imgs_ is not None:
    #     print("보여", imgs_)
    # else:
    #     print("안보여")

    # re_ = text_check_get(425, 525, 455, 545, cla)
    # print("r", re_)




