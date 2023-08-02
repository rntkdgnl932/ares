import sys
import time
import requests

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_

def go_test():
    import numpy as np
    import cv2
    import pyautogui
    from function import imgs_set_, mouse_move_cpp, drag_pos_Press, drag_pos_Release, click_pos_2, click_pos_reg, how_many_pic, drag_pos
    from get_items import get_event, get_post, get_gardiun_pass, get_gardiun_rank, bag_item_open
    from action_ares import out_check
    from jadong import go_hangsun_map
    print("tst")
    cla = "one"

    burst_mode_action_right = True

    # mouse_move_cpp(180, 505, cla)
    # # 0.2초
    # time.sleep(0.2)
    # # 마우스 누르기
    # drag_pos_Press()
    # # 0.2초
    # time.sleep(0.2)

    # go_hangsun_map(cla, "where")

    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\attack_ready.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(815, 935, 915, 1030, cla, img, 0.7)
    if imgs_ is not None and imgs_ != False:
        print("사냥터이동중", imgs_)
    else:
        print("attack_ready.")


    # # 마우스 떼기
    # drag_pos_Release()
    # # 0.2초
    # time.sleep(0.2)

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




