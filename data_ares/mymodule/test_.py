import sys
import os
import time
import requests

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_

def go_test():
    import numpy as np
    import cv2
    import pyautogui
    from function import imgs_set_, mouse_move_cpp, drag_pos_Press, drag_pos_Release, click_pos_2, click_pos_reg, how_many_pic, drag_pos
    from get_items import get_event, get_post, get_gardiun_pass, get_gardiun_rank, bag_item_open, get_event, get_item_start
    from action_ares import out_check, clean_screen, maul_go
    from jadong import go_hangsun_map
    from powerup_ares import soohosuk, hoilodo, monster_dogam
    from soojib_boonhae import soojib, soojib_setting, boonhae
    from dungeon import dungeon_in_hangsungpagyun, dungeon_in_moriagiji, dark_play
    from potion_ares import maul_potion_get
    from chaejib import chaejib_start, chaejib_setting, chaejib_go, chaejib_maps
    from gardiun_mission import gardiun_mission_get
    print("tst")
    cla = "one"
    v_.now_cla = cla


    burst_mode_action_right = True

    # mouse_move_cpp(180, 505, cla)
    # # 0.2초
    # time.sleep(0.2)
    # # 마우스 누르기
    # drag_pos_Press()
    # # 0.2초
    # time.sleep(0.2)

    # go_hangsun_map(cla, "where")

    # click_pos_reg(860, 1015, cla)
    # time.sleep(1)

    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\ares_start_ready.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(0, 50, 960, 1030, v_.now_cla, img, 0.7)
    if imgs_ is not None and imgs_ != False:
        print("매크로를 내려야 실행됨...10초", imgs_)



    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\click_check.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(900, 110, 935, 145, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("click_check", imgs_)
    # else:
    #     print("not click_check")

    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_npc.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(300, 300, 660, 700, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("gardiun_npc", imgs_)
    # else:
    #     print("not gardiun_npc")

    # dungeon_in_moriagiji(cla, "모리아기지_1")

    # get_item_start(cla)

    # # 2 = 97, 887
    # # 3 = 97, 946
    # 59 차이
    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_on.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("auto_on", imgs_)
    # else:
    #     print("not auto_on")
    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_off.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("auto_off", imgs_)
    # else:
    #     print("not auto_off")

    # # y_reg = 153 + (층 * 34)
    # # 1 = 163, 187
    # # 2 = 163, 221
    # # 3 = 163, 255
    # # 4 = 163, 289 -20 +20
    # # 5 = 163, 323
    # # 6 = 163, 358
    # for i in range(7):
    #     y_lock = 153 + ( i * 34)
    #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\small_lock.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(140, y_lock - 20, 220, y_lock + 20, cla, img, 0.8)
    #     if imgs_ is not None and imgs_ != False:
    #         print(i, imgs_)
    #     else:
    #         print("not mini_lock", i)
    #     time.sleep(0.1)

    # 28...
    # 2 = 51, 1010
    # 3 = 79, 1010
    # for i in range(5):
    #     if i != 0:
    #         x_lock = (i * 28) - 5
    #         full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\mini_lock.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(x_lock - 20, 990, x_lock + 20, 1040, cla, img, 0.8)
    #         if imgs_ is not None and imgs_ != False:
    #             print("mini_lock", imgs_)
    #         else:
    #             print("no mini_lock", i)


    # for z in range(10):
    #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm3.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(500, 570, 570, 610, cla, img, 0.8)
    #     if imgs_ is not None and imgs_ != False:
    #         click_pos_reg(imgs_.x, imgs_.y, cla)
    #         break
    #     else:
    #         full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_last_title.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(440, 390, 510, 430, cla, img, 0.8)
    #         if imgs_ is not None and imgs_ != False:
    #             full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm2.PNG"
    #             img_array = np.fromfile(full_path, np.uint8)
    #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #             imgs_ = imgs_set_(500, 640, 570, 670, cla, img, 0.8)
    #             if imgs_ is not None and imgs_ != False:
    #                 click_pos_reg(imgs_.x, imgs_.y, cla)
    #         else:
    #             click_pos_2(865, 1015, cla)
    #             time.sleep(0.5)
    #         time.sleep(0.5)







    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_c_off.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(310, 430, 380, 470, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("soojib_setting_c_off", imgs_)
    # else:
    #     print("not soojib_setting_c_off")
    #
    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_b_off.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(370, 430, 440, 470, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("soojib_setting_b_off", imgs_)
    # else:
    #     print("not soojib_setting_b_off")
    #
    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_all_off.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(255, 475, 325, 525, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("soojib_setting_all_off", imgs_)
    # else:
    #     print("not soojib_setting_all_off")




    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(60, 60, 220, 110, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("hoilodo_point_1", imgs_)
    # else:
    #     print("hoilodo_point_1.")
    # #
    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(120, 120, 170, 330, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("hoilodo_point_2", imgs_)
    # else:
    #     print("hoilodo_point_2.")
    #
    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_3.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(150, 310, 800, 880, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("hoilodo_point_3", imgs_)
    # else:
    #     print("hoilodo_point_3.")
    #
    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_4.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(150, 310, 800, 880, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("hoilodo_point_4", imgs_)
    # else:
    #     print("hoilodo_point_4.")


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




