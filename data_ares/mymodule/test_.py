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
    import random
    from function import imgs_set_, mouse_move_cpp, drag_pos_Press, drag_pos_Release, click_pos_2, click_pos_reg, how_many_pic, drag_pos, text_check_get, int_put_, in_number_check
    from get_items import get_event, get_post, get_gardiun_pass, get_gardiun_rank, bag_item_open, get_item_start, get_mission_bosang, get_sangjum_sohwan, get_season, get_season_pass
    from action_ares import out_check, clean_screen, maul_go, dead_die, menu_open, loading_ares, mine_check, juljun_time_check, confirm_all
    from jadong import go_hangsun_map
    from powerup_ares import soohosuk, hoilodo, monster_dogam
    from soojib_boonhae import soojib, soojib_setting, boonhae_start, boonhae_ready, boonhae_setting_bc, boonhae_setting_c, soojib_boonhae_start, boonhae_bangugoo, boonhae_module
    from dungeon import dungeon_in_hangsungpagyun, dungeon_in_moriagiji, dark_play, dungeon_in_raid
    from potion_ares import maul_potion_get, maul_potion_get_full
    from chaejib import chaejib_start, chaejib_setting, chaejib_go, chaejib_maps
    from gardiun_mission import gardiun_mission_get
    from auction_ares import auction_start, auction_sell
    from guild_ares import guild_attendance
    from log_ares import character_change
    from property_ares import my_property_upload
    from season_dungeon import season_dungeon_in_battle
    from auction_ares import auction_start, auction_ready, auction_sell_folder_jangbi, auction_sell_folder_etc_item
    from stop_event18 import _stop_please


    print("tst")
    cla = "one"

    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3

    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\sell_title.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(440, 360, 520, 410, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("sell_title", imgs_)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\10.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(545, 460, 670, 500, cla, img, 0.97)
        if imgs_ is not None and imgs_ != False:
            print("10", imgs_)

    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\etc_item\\studyed.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(750, 130, 950, 1000, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("studyed...", imgs_)

    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\r_grade.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(5, 110, 60, 1040, cla, img, 0.7)
    if imgs_ is not None and imgs_ != False:
        print("r_grade", imgs_)

    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\gardiun_title.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(10, 10, 70, 100, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("gardiun_title", imgs_)

    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_select.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(735, 955, 815, 1025, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("gardiun_select", imgs_)

    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\give_up_confirm.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(480, 560, 600, 610, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("give_up_confirm", imgs_)

    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\event\\event_spot_1.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(10, 50, 100, 90, cla, img, 0.7)
    if imgs_ is not None and imgs_ != False:
        print("event_spot_1")
    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\event\\event_spot_2.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(10, 50, 100, 90, cla, img, 0.7)
    if imgs_ is not None and imgs_ != False:
        print("event_spot_2")
    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\18_1.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
    if imgs_ is not None and imgs_ != False:
        print("18_1")

    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\event\\arlim_title.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(430, 450, 520, 520, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("arlim_title", imgs_)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\download.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 500, 620, 600, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("download", imgs_)
            click_pos_2(480, 590, cla)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\downloading.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 1000, 100, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("downloading", imgs_)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\resource_loading.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(370, 880, 540, 930, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("resource_loading", imgs_)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\18\\screen_touch.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(370, 880, 540, 930, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("screen_touch", imgs_)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\event\\arlim_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 560, 620, 620, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("arlim_confirm", imgs_)

    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_on.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(530, 980, 615, 1030, cla, img, 0.7)
    if imgs_ is not None and imgs_ != False:
        print("auto_on", imgs_)
    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_off.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(530, 980, 615, 1030, cla, img, 0.7)
    if imgs_ is not None and imgs_ != False:
        print("auto_off", imgs_)




# 300, 8001 700 1000
    # my_property_upload(cla)
    # 0
    # 390
    # 416
    # 1
    # 423
    # 449
    # 2
    # 456
    # 482
    # 3
    # 489
    # 515
    # 4
    # 522
    # 548
    # 5
    # 555
    # 581
    # 6
    # 588
    # 614

    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(270, 456, 310, 482, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("받기 시작", imgs_)

    # url = "https://raw.githubusercontent.com/rntkdgnl932/ares/master/data_ares/get_items/get_event.txt"
    #
    # response = requests.get(url, headers={'Cache-Control': 'no-cache'})
    # read_event = response.text.splitlines()

    # print("get_item_test", read_event)
    # get_event(cla)
    # time.sleep(0.1)
    #
    # drag_pos(240, 670, 240, 420, cla)



    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\buy_complete.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(430, 240, 540, 280, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("buy_complete", imgs_)
    #
    # else:
    #     print("sdg", imgs_)
    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\clicked.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(80, 115, 120, 165, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("clizzzzzzzzzzzzzzzcked", imgs_)
    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(270, 380, 310, 700, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("sdg", imgs_)

    # url = "https://raw.githubusercontent.com/rntkdgnl932/ares/master/data_ares/get_items/get_event.txt"
    #
    # response = requests.get(url, headers={'Cache-Control': 'no-cache'})
    # # response = requests.get(url, headers={'Cache-Control': 'no-cache'})
    # data = response.text.splitlines()
    #
    # print("server_get_ares", data)
    #
    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\auction\\dnglock_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(780, 1000, 950, 1030, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("dnglock_2", imgs_)

    # re_ = text_check_get(595, 477, 620, 492, cla)
    # print("3자리", re_)
    # result_int = int_put_(re_)
    # result_num = in_number_check(cla, result_int)
    # if result_num == True:
    #     print("숫자다", re_)
    #     print("숫자다222", result_int)
    # else:
    #     print("숫자 아니다", re_)
    #
    # re_ = text_check_get(589, 477, 625, 492, cla)
    # print("4자리", re_)
    # result_int = int_put_(re_)
    # result_num = in_number_check(cla, result_int)
    # if result_num == True:
    #     print("숫자다", re_)
    #     print("숫자다222", result_int)
    # else:
    #     print("숫자 아니다", re_)

    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\clicked.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(80, 80, 120, 300, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("clicked", imgs_)

    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(120, 120, 170, 330, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #
    #     hoilodo_point = False
    #
    #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_3.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(150, 310, 800, 880, cla, img, 0.8)
    #     if imgs_ is not None and imgs_ != False:
    #         print("hoilodo_point_3", imgs_)
    #         click_pos_reg(imgs_.x - 10, imgs_.y + 7, cla)
    #         hoilodo_point = True
    #         time.sleep(0.5)
    #     else:
    #         full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_4.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(150, 310, 800, 880, cla, img, 0.8)
    #         if imgs_ is not None and imgs_ != False:
    #             print("hoilodo_point_4", imgs_)
    #             click_pos_reg(imgs_.x - 10, imgs_.y + 7, cla)
    #             hoilodo_point = True
    #             time.sleep(0.5)
    #         else:
    #             full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_5.PNG"
    #             img_array = np.fromfile(full_path, np.uint8)
    #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #             imgs_ = imgs_set_(150, 310, 800, 880, cla, img, 0.8)
    #             if imgs_ is not None and imgs_ != False:
    #                 print("hoilodo_point_5", imgs_)
    #                 click_pos_reg(imgs_.x - 10, imgs_.y + 7, cla)
    #                 hoilodo_point = True
    #                 time.sleep(0.5)
    #             else:
    #                 full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_6.PNG"
    #                 img_array = np.fromfile(full_path, np.uint8)
    #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #                 imgs_ = imgs_set_(150, 310, 800, 880, cla, img, 0.8)
    #                 if imgs_ is not None and imgs_ != False:
    #                     print("hoilodo_point_6", imgs_)
    #                     click_pos_reg(imgs_.x - 10, imgs_.y + 7, cla)
    #                     hoilodo_point = True
    #                     time.sleep(0.5)
    #                 else:
    #                     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_7.PNG"
    #                     img_array = np.fromfile(full_path, np.uint8)
    #                     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #                     imgs_ = imgs_set_(150, 310, 800, 880, cla, img, 0.8)
    #                     if imgs_ is not None and imgs_ != False:
    #                         print("hoilodo_point_7", imgs_)
    #                         click_pos_reg(imgs_.x - 10, imgs_.y + 7, cla)
    #                         hoilodo_point = True
    #                         time.sleep(0.5)
    #                     else:
    #                         full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\hoilodo_point_8.PNG"
    #                         img_array = np.fromfile(full_path, np.uint8)
    #                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #                         imgs_ = imgs_set_(150, 310, 800, 880, cla, img, 0.8)
    #                         if imgs_ is not None and imgs_ != False:
    #                             print("hoilodo_point_8", imgs_)
    #                             click_pos_reg(imgs_.x - 10, imgs_.y + 7, cla)
    #                             hoilodo_point = True
    #                             time.sleep(0.5)

    # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\gardiun_rank_point_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(100, 50, 900, 100, cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("gardiun_rank_point_1", imgs_)

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

    # re_ = text_check_get(570, 470, 640, 500, cla)
    # print("r", re_)




