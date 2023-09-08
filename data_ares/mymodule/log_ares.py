import time
# import os
import sys

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def log_start():
    print("log_start")

def character_change(cla, character_id):
    import numpy as np
    import cv2
    import os
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import out_check, clean_screen, menu_open, loading_ares
    from massenger import line_to_me
    from stop_event18 import _stop_please
    try:
        print("character_select")

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\character_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 10, 110, 70, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("character_title", imgs_)

        print("^^")
        cha_select = False
        cha_select_count = 0
        while cha_select is False:
            cha_select_count += 1
            if cha_select_count > 10:
                cha_select = True
                line_to_me(cla, "처음 스타트 화면에 문제가 있다.")

            # 캐릭터 선택 화면
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\character_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 110, 70, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\log\\game_in_ares.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 620, 900, 680, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    # 좌표
                    x_reg = imgs_.x
                    y_reg = imgs_.y

                    for li in range(2):
                        if int(character_id) == 1:
                            click_pos_2(95, 440, cla)
                        elif int(character_id) == 2:
                            click_pos_2(95, 485, cla)
                        elif int(character_id) == 3:
                            click_pos_2(95, 530, cla)

                        time.sleep(0.3)

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\character_edit_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 110, 70, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)


                    click_pos_reg(x_reg, y_reg, cla)
                    time.sleep(0.5)

                    in_game = False
                    in_game_count = 0
                    while in_game is False:
                        in_game_count += 1
                        if in_game_count > 40:
                            in_game = True
                            line_to_me(cla, "게임화면 진입에 문제가 있다.")
                        result_out = out_check(cla)
                        if result_out == True:
                            cha_select = True
                            in_game = True

                            _stop_please(cla)

                            # 현재 진입한 캐릭터 번호(id)

                            dir_path = "C:\\my_games\\ares"
                            if cla == 'one':
                                file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
                            if cla == 'two':
                                file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
                            if cla == 'three':
                                file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
                            if cla == 'four':
                                file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"

                            # read_id = '0'

                            is_out = False
                            is_out_count = 0
                            while is_out is False:
                                is_out_count += 1
                                if is_out_count > 15:
                                    is_out = True
                                if os.path.isfile(file_path) == True:
                                    with open(file_path, "r", encoding='utf-8-sig') as file:
                                        read_id = file.read()
                                        if str(character_id) == str(read_id):
                                            is_out = True
                                        else:
                                            with open(file_path, "w", encoding='utf-8-sig') as file:
                                                file.write(str(character_id))
                                        time.sleep(0.3)
                                else:
                                    with open(file_path, "w", encoding='utf-8-sig') as file:
                                        file.write(str(character_id))

                                # if str(character_id) == str(read_id):
                                #     is_out = True
                                # else:
                                #     with open(file_path, "w", encoding='utf-8-sig') as file:
                                #         file.write(str(character_id))
                                time.sleep(0.3)


                        else:
                            print("진입중")
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                loading_ares(cla)
                        time.sleep(0.5)

                    time.sleep(0.2)




            else:
                # 추후 대기중 화면 설정하기
                # 대기중 화면이 아닐때

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\log\\change_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 555, 630, 630, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_select = False
                    is_select_count = 0
                    while is_select is False:
                        is_select_count += 1
                        if is_select_count > 30:
                            is_select = True
                            line_to_me(cla, "캐릭 선택화면으로 가는 것에 문제가 있다.")
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\character_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 110, 70, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            is_select = True
                        time.sleep(0.5)
                else:
                    menu_open(cla)
                    time.sleep(0.1)
                    click_pos_2(990, 370, cla)
                    wait_y = False
                    wait_y_count = 0
                    while wait_y is False:
                        wait_y_count += 1
                        if wait_y_count > 20:
                            wait_y = True
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\log\\change_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 555, 630, 630, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            wait_y = True
                        time.sleep(0.3)
                time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0



