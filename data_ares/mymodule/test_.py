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

    bag_item_open(cla)
    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_challenge\\friend.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(800, 300, 860, 360, cla, img, 0.7)
    if imgs_ is not None:
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_challenge\\challenge_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 170, 150, 270, cla, img, 0.77)
        if imgs_ is not None:
            print("보여", imgs_)
        else:
            print("안보여")

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




