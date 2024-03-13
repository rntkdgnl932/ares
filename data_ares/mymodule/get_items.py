import time
import sys
import requests

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_


def get_item_start(cla):
    from action_ares import maul_go
    from potion_ares import maul_potion_get
    from guild_ares import guild_attendance
    try:
        print("get_item_start..")
        get_event(cla)
        time.sleep(0.1)
        get_sangjum_sohwan(cla)
        time.sleep(0.1)
        get_post(cla)
        time.sleep(0.1)
        get_gardiun_pass(cla)
        time.sleep(0.1)
        get_season_pass(cla)
        time.sleep(0.1)
        get_gardiun_rank(cla)
        time.sleep(0.1)
        get_mission_bosang(cla)
        time.sleep(0.1)
        guild_attendance(cla)
        time.sleep(0.1)
        bag_item_open(cla)
        time.sleep(0.3)
        result_maul = maul_go(cla)
        if result_maul == True:
            maul_potion_get(cla)




    except Exception as e:
        print(e)
        return 0

def get_event(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, how_many_pic, click_pos_2, drag_pos
    from action_ares import menu_open
    try:
        print("get_event")

        # dir_path = "C:\\my_games\\ares"
        # file_path = dir_path + "\\data_ares\\get_items\\get_event.txt"
        #
        # with open(file_path, "r", encoding='utf-8-sig') as file:
        #     read_event = file.read().splitlines()

        url = "https://raw.githubusercontent.com/rntkdgnl932/ares/master/data_ares/get_items/get_event.txt"

        response = requests.get(url, headers={'Cache-Control': 'no-cache'})
        read_event = response.text.splitlines()

        drag_num = 0

        y_plus = 0

        # 첫번째 y값 기준 : 399, 각 단계별로 33픽셀 차이
        event_ready = False
        event_ready_count = 0
        while event_ready is False:
            event_ready_count += 1
            if event_ready_count > 5:
                event_ready = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(440, 350, 515, 400, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("event 창 열렸다.")
                event_ready = True

                # # 포인트 갯수 알아내기
                # address = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                # result_many = how_many_pic(270, 370, 310, 700, address, cla)
                # print("result_many", result_many)
                #
                # if result_many != 0:

                for z in range(len(read_event)):

                    y_up = 403 + (z * 33) - 13
                    y_down = 403 + (z * 33) + 13



                    is_drag = read_event[z].split(":")

                    if is_drag[1] == "drag":
                        for i in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\get_items\\drag_img\\last_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(190, 660, 310, 690, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                drag_num = z
                                break
                            else:
                                drag_pos(240, 670, 240, 420, cla)
                                time.sleep(0.5)
                                drag_pos(240, 670, 240, 420, cla)

                            time.sleep(1)

                    print(z + 1, is_drag[1])

                    # elif is_drag[1] == "pass":
                    #     y_plus += 40

                    if is_drag[1] != "pass":
                        if drag_num == 0:
                            # 현재 이벤트 번호 및 파악할 포인트
                            print(z + 1, y_up, y_down)
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(270, y_up, 310, y_down, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print(z + 1, "받기 시작")
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(270, y_up, 310, y_down, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)
                                    time.sleep(0.5)
                                    aim_reg = "none"
                                    for i in range(len(read_event)):
                                        y_average = 399
                                        cal_ = read_event[i].split(":")
                                        y_reg_1 = y_average - 15 - 33 + (33 * int(cal_[0]))
                                        y_reg_2 = y_average + 15 - 33 + (33 * int(cal_[0]))
                                        if y_reg_1 < imgs_.y < y_reg_2:
                                            print(i, imgs_)
                                            # 드래그일 경우 다시...
                                            aim_reg = read_event[i]
                                            break
                                    if aim_reg != "none":
                                        print("aim_reg", aim_reg)
                                        result_aim_reg = aim_reg.split(":")
                                        # 추려낸 결과 ex => 2:seven
                                        get_event_click(imgs_.x, imgs_.y, result_aim_reg[1], cla)
                                        time.sleep(0.5)
                            else:
                                print(z + 1, "포인트가 안보여")
                        else:
                            # 아랫칸 있을때만...
                            # 업데이트때마다 now_x + (z * 33) - 13 여기서 now_x 숫자 변경해줘야함
                            # z 는 0 부터 시작함에 주의...
                            # now_y = 현재y값 - (z * 33)
                            # 총길이 11일때 330, 12일때 300, 13일때 265, 14일떼 230, 15일때 200

                            now_y = 200
                            y_up = now_y + (z * 33) - 13
                            y_down = now_y + (z * 33) + 13

                            # 현재 이벤트 번호 및 파악할 포인트
                            print(z + 1, y_up, y_down)

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(270, y_up, 310, y_down, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print(z + 1, "받기 시작")
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(270, y_up, 310, y_down, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)
                                    time.sleep(0.5)
                                    aim_reg = "none"
                                    for i in range(len(read_event)):
                                        y_average = 399
                                        cal_ = read_event[i].split(":")
                                        y_reg_1 = y_average - 15 - 33 + (33 * int(cal_[0]))
                                        y_reg_2 = y_average + 15 - 33 + (33 * int(cal_[0]))
                                        if y_reg_1 < imgs_.y < y_reg_2:
                                            print("aim_reg", i, imgs_)
                                            # 드래그일 경우 다시...
                                            aim_reg = read_event[i]
                                            break
                                    if aim_reg != "none":
                                        print("aim_reg", aim_reg)
                                        result_aim_reg = aim_reg.split(":")
                                        # 추려낸 결과 ex => 2:seven
                                        get_event_click(imgs_.x, imgs_.y, result_aim_reg[1], cla)
                                        time.sleep(0.5)
                            else:
                                print(z + 1, "포인트가 안보여")


                            # if is_drag[0] == "11":
                            #     get_event_click_drag(240, 540, "fourteen", cla)
                            #
                            # elif is_drag[0] == "12":
                            #     get_event_click_drag(240, 575, "fourteen", cla)
                            #
                            # elif is_drag[0] == "13":
                            #     get_event_click_drag(240, 610, "seven_six", cla)
                            #
                            # elif is_drag[0] == "14":
                            #     get_event_click_drag(240, 640, "four", cla)
                            #
                            # elif is_drag[0] == "15":
                            #     get_event_click_drag(240, 675, "seven_six", cla)





                    time.sleep(0.2)

                # 이벤트 창 닫기
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\x_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(745, 360, 800, 400, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                # 여기엔 드래그가 있는지 파악 후 있다면 기존 오딘과 같은 방식으로 get_event_drag.txt 만들어서 좌표와 클릭할 함수 설정해서 받도록...추후예정
                time.sleep(0.1)
            else:
                menu_open(cla)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 20, 830, 50, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 8, imgs_.y + 10, cla)
                else:
                    print("이벤트 안 보이나?")
                    click_pos_2(810, 60, cla)
                    time.sleep(1)

            time.sleep(1)



    except Exception as e:
        print(e)
        return 0

def get_event_click(reg_x, reg_y, how, cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2, random_int

    try:
        print("get_event_click", how)

        if cla == "one":
            reg_x = reg_x
        if cla == "two":
            reg_x = reg_x - 960
        if cla == "three":
            reg_x = reg_x - 960 - 960
        if cla == "four":
            reg_x = reg_x - 960 - 960 - 960

        get_complete = False
        if how == "four":
            for i in range(15):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(reg_x - 20, reg_y - 20, reg_x + 20, reg_y + 20, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    # 여기 받기 부분이 how에 따라 달라짐.
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 580, 780, 680, cla, img, 0.77)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        time.sleep(0.1)
                        break
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 580, 780, 680, cla, img, 0.77)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        time.sleep(0.1)
                        break
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 580, 780, 680, cla, img, 0.77)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        time.sleep(0.1)
                        break
                time.sleep(0.1)
        elif how == "six":
            for i in range(15):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(reg_x - 20, reg_y - 20, reg_x + 20, reg_y + 20, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    # 여기 받기 부분이 how에 따라 달라짐.
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 530, 780, 680, cla, img, 0.77)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        time.sleep(0.3)
                        for k in range(random_int()):
                            click_pos_2(reg_x, reg_y, cla)
                            time.sleep(0.1)
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 530, 780, 680, cla, img, 0.77)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        time.sleep(0.3)
                        for k in range(random_int()):
                            click_pos_2(reg_x, reg_y, cla)
                            time.sleep(0.1)
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(490, 530, 780, 680, cla, img, 0.77)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        time.sleep(0.3)
                        for k in range(random_int()):
                            click_pos_2(reg_x, reg_y, cla)
                            time.sleep(0.1)
                else:
                    break
                time.sleep(0.1)
        elif how == "seven":
            for i in range(15):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(reg_x - 20, reg_y - 20, reg_x + 20, reg_y + 20, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    # 여기 받기 부분이 how에 따라 달라짐.
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 590, 780, 680, cla, img, 0.77)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        time.sleep(0.1)
                        break
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 590, 780, 680, cla, img, 0.77)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        time.sleep(0.1)
                        break
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 590, 780, 680, cla, img, 0.77)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        time.sleep(0.1)
                        break
                time.sleep(0.1)
        elif how == "fourteen":
            for i in range(15):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(reg_x - 20, reg_y - 20, reg_x + 20, reg_y + 20, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    # 여기 받기 부분이 how에 따라 달라짐.
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 515, 780, 550, cla, img, 0.77)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                        time.sleep(0.1)
                        break
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(330, 515, 780, 550, cla, img, 0.77)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                            time.sleep(0.1)
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_4.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 515, 780, 550, cla, img, 0.77)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                time.sleep(0.1)
                                break
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 590, 780, 620, cla, img, 0.77)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                    time.sleep(0.1)
                                    break
                                else:
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(330, 590, 780, 620, cla, img, 0.77)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                        time.sleep(0.1)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_4.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(330, 590, 780, 620, cla, img, 0.77)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                            time.sleep(0.1)
                                            break
                time.sleep(0.1)
        elif how == "seven_six":
            for i in range(15):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(reg_x - 20, reg_y - 20, reg_x + 20, reg_y + 20, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    # 여기 받기 부분이 how에 따라 달라짐.

                    clicked = False

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_5.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(345, 500, 780, 530, cla, img, 0.77)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        clicked = True
                        time.sleep(0.1)
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_6.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(345, 500, 780, 530, cla, img, 0.77)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                            clicked = True
                            time.sleep(0.1)
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_7.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(345, 500, 780, 530, cla, img, 0.77)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                                clicked = True
                                time.sleep(0.1)

                    if clicked == True:
                        for k in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_seven_six_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(515, 525, 780, 680, cla, img, 0.77)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                time.sleep(0.5)
                                for z in range(random_int()):
                                    click_pos_2(reg_x, reg_y, cla)
                                    time.sleep(0.1)
                            time.sleep(0.1)
                else:
                    break
                time.sleep(0.1)
        elif how == "pass":
            print("수동으로 받자")

        time.sleep(0.3)
        if how != "pass":
            for i in range(random_int()):
                click_pos_2(reg_x, reg_y, cla)
                time.sleep(0.1)


    except Exception as e:
        print(e)
        return 0

def get_event_click_drag(reg_x, reg_y, how, cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2, random_int

    try:
        print("get_event_click_drag", how)

        # if cla == "one":
        #     reg_x = reg_x
        # if cla == "two":
        #     reg_x = reg_x - 960
        # if cla == "three":
        #     reg_x = reg_x - 960 - 960
        # if cla == "four":
        #     reg_x = reg_x - 960 - 960 - 960

        click_pos_2(reg_x, reg_y, cla)
        time.sleep(1)

        if how == "four":
            for i in range(15):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(490, 580, 780, 680, cla, img, 0.77)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.1)
                    break
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(490, 580, 780, 680, cla, img, 0.77)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.1)
                    break
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(490, 580, 780, 680, cla, img, 0.77)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.1)
                    break
                time.sleep(0.1)
        elif how == "six":
            for i in range(15):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(490, 530, 780, 680, cla, img, 0.77)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.1)
                    break
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(490, 530, 780, 680, cla, img, 0.77)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.1)
                    break
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(490, 530, 780, 680, cla, img, 0.77)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.1)
                    break
                time.sleep(0.1)
        elif how == "seven":
            for i in range(15):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 590, 780, 680, cla, img, 0.77)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.1)
                    break
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 590, 780, 680, cla, img, 0.77)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.1)
                    break
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 590, 780, 680, cla, img, 0.77)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.1)
                    break
                time.sleep(0.1)
        elif how == "fourteen":
            for i in range(15):
                # 여기 받기 부분이 how에 따라 달라짐.
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 515, 780, 680, cla, img, 0.77)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.1)
                    break
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 515, 780, 680, cla, img, 0.77)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.1)
                    break
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_4.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 515, 780, 680, cla, img, 0.77)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.1)
                    break
                time.sleep(0.1)
        elif how == "seven_six":
            for i in range(10):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_point_5.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(345, 495, 780, 530, cla, img, 0.77)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                    time.sleep(0.1)

                    for k in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_event_seven_six_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(515, 525, 780, 680, cla, img, 0.77)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                            time.sleep(0.5)
                            for z in range(random_int() + 1):
                                click_pos_2(reg_x, reg_y, cla)
                                time.sleep(0.1)
                        time.sleep(0.1)
                else:
                    break

                time.sleep(0.3)
        elif how == "pass":
            print("수동으로 받자")

        time.sleep(0.3)
        for i in range(random_int()):
            click_pos_2(reg_x, reg_y, cla)
            time.sleep(0.1)


    except Exception as e:
        print(e)
        return 0


def get_post(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import menu_open

    try:
        print("get_post")
        post_ready = False
        post_ready_count = 0
        while post_ready is False:
            post_ready_count += 1
            if post_ready_count > 5:
                post_ready = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\post_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("post 창 열렸다.")
                post_ready = True


                for i in range(5):

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_post_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(65, 85, 115, 155, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("보여", imgs_)
                        click_pos_reg(imgs_.x - 40, imgs_.y, cla)
                        time.sleep(0.2)
                        for z in range(5):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\post_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(715, 1015, cla)
                            else:
                                click_pos_2(715, 1015, cla)
                                time.sleep(0.1)
                                click_pos_2(715, 1015, cla)
                                break
                        time.sleep(0.3)
                    else:
                        break
                    time.sleep(0.3)

                # 이벤트 창 닫기
                for i in range(5):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\post_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(940, 50, cla)
                    else:
                        break
                    time.sleep(0.2)
                time.sleep(0.1)
            else:
                menu_open(cla)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_post_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 350, 830, 375, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 8, imgs_.y + 10, cla)
                else:
                    post_ready = True
            time.sleep(1)




    except Exception as e:
        print(e)
        return 0


def get_gardiun_pass(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import menu_open

    try:
        print("get_gardiun_pass")
        gardiun_ready = False
        gardiun_ready_count = 0
        while gardiun_ready is False:
            gardiun_ready_count += 1
            if gardiun_ready_count > 5:
                gardiun_ready = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\gardiun_pass_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("gardiun_pass 창 열렸다.")
                gardiun_ready = True


                for i in range(2):
                    click_pos_2(100, 100, cla)
                    time.sleep(1)
                    click_pos_2(660, 1015, cla)
                    time.sleep(0.2)
                    click_pos_2(795, 1015, cla)
                    time.sleep(0.2)

                for i in range(2):
                    click_pos_2(200, 100, cla)
                    time.sleep(1)
                    click_pos_2(660, 1015, cla)
                    time.sleep(0.2)
                    click_pos_2(795, 1015, cla)
                    time.sleep(0.2)


                # 이벤트 창 닫기
                for i in range(5):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\gardiun_pass_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(940, 50, cla)
                    else:
                        break
                    time.sleep(0.2)
                time.sleep(0.1)
            else:
                menu_open(cla)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_post_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(930, 210, 960, 250, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 8, imgs_.y + 10, cla)
                else:
                    gardiun_ready = True
            time.sleep(1)




    except Exception as e:
        print(e)
        return 0

def get_season_pass(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import menu_open

    try:
        print("get_season_pass")
        gardiun_ready = False
        gardiun_ready_count = 0
        while gardiun_ready is False:
            gardiun_ready_count += 1
            if gardiun_ready_count > 5:
                gardiun_ready = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hondon_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("hondon_title 창 열렸다.")
                gardiun_ready = True


                for i in range(2):
                    click_pos_2(110, 100, cla)
                    time.sleep(1)
                    click_pos_2(695, 1015, cla)
                    time.sleep(0.2)
                    click_pos_2(795, 1015, cla)
                    time.sleep(0.2)



                # 이벤트 창 닫기
                for i in range(5):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hondon_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(940, 50, cla)
                    else:
                        break
                    time.sleep(0.2)
                time.sleep(0.1)
            else:
                menu_open(cla)
                click_pos_2(65, 165, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hondon_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.3)

            time.sleep(1)




    except Exception as e:
        print(e)
        return 0

def get_gardiun_rank(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import menu_open

    try:
        print("get_gardiun_rank")
        gardiun_ready = False
        gardiun_ready_count = 0
        while gardiun_ready is False:
            gardiun_ready_count += 1
            if gardiun_ready_count > 5:
                gardiun_ready = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\gardiun_rank_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("gardiun_rank 창 열렸다.")
                gardiun_ready = True

                for i in range(4):
                    click_pos_2(50, 1015, cla)
                    time.sleep(0.2)

                for i in range(100):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\gardiun_rank_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(100, 50, 900, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:

                        x_reg = imgs_.x - 25
                        y_reg = imgs_.y + 20

                        click_pos_reg(x_reg, y_reg, cla)
                        time.sleep(0.5)
                        for k in range(5):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\gardiun_rank_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                click_pos_reg(x_reg, y_reg, cla)
                                time.sleep(0.2)
                            time.sleep(0.3)
                    else:
                        time.sleep(1)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\gardiun_rank_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\gardiun_rank_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(100, 50, 900, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                x_reg = imgs_.x - 25
                                y_reg = imgs_.y + 20

                                click_pos_reg(x_reg, y_reg, cla)
                            else:
                                break
                        else:
                            click_pos_2(480, 680, cla)
                            time.sleep(0.2)
                    time.sleep(1)

                # 이벤트 창 닫기
                for i in range(5):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\gardiun_rank_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(940, 50, cla)
                    else:
                        break
                    time.sleep(0.2)
                time.sleep(0.1)
            else:
                menu_open(cla)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_post_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(930, 85, 960, 120, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 8, imgs_.y + 10, cla)
                else:
                    gardiun_ready = True
            time.sleep(1)




    except Exception as e:
        print(e)
        return 0


def get_season(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import menu_open

    try:
        print("get_season")
        season_ready = False
        season_ready_count = 0
        while season_ready is False:
            season_ready_count += 1
            if season_ready_count > 5:
                season_ready = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hondon_title2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("hondon_title2 창 열렸다.")
                season_ready = True

                # 패스 받기

                for i in range(3):

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\season_get\\season_pass_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(130, 980, 240, 1040, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(700, 1020, cla)
                        time.sleep(0.2)
                        click_pos_2(800, 1020, cla)
                        time.sleep(0.2)
                        break
                    else:
                        click_pos_2(115, 100, cla)
                        time.sleep(0.2)
                        for k in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\season_get\\season_pass_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(130, 980, 240, 1040, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.5)

                # 시즌 수집 등록하기



                for i in range(4):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\season_get\\soojib_hyogwa_information.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(810, 110, 910, 150, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:

                        point_count = 0
                        for k in range(20):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\season_get\\season_soojib_point.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(560, 140, 800, 970, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                                time.sleep(0.3)
                                click_pos_2(915, 1020, cla)
                                time.sleep(0.3)
                            else:
                                point_count += 1
                                if point_count > 2:
                                    print("수집포인트", point_count)
                                    break
                            time.sleep(0.3)

                        break

                    else:

                        for k in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\season_get\\soojib_hyogwa_information.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(810, 110, 910, 150, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                click_pos_2(185, 100, cla)
                                time.sleep(0.1)
                            time.sleep(0.5)
                    time.sleep(0.5)

                # 이벤트 창 닫기
                for i in range(5):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hondon_title2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(940, 50, cla)
                    else:
                        break
                    time.sleep(0.2)
                time.sleep(0.1)
            else:
                menu_open(cla)
                click_pos_2(60, 160, cla)
                time.sleep(0.1)
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hondon_title2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)
            time.sleep(1)




    except Exception as e:
        print(e)
        return 0

def bag_item_open(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import menu_open
    from tuto_grow import tuto_grow_skip

    try:
        print("bag_item_open")
        bag_item_open_ready = False
        bag_item_open_ready_count = 0
        while bag_item_open_ready is False:
            bag_item_open_ready_count += 1
            if bag_item_open_ready_count > 5:
                bag_item_open_ready = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\bag_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("bag 창 열렸다.")
                bag_item_open_ready = True


                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(90, 290, 115, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(50, 320, cla)
                    time.sleep(0.5)


                dir_path = "C:\\my_games\\ares"
                file_path = dir_path + "\\data_ares\\imgs\\get_items\\sohwan_list\\sohwan_list.txt"

                with open(file_path, "r", encoding='utf-8-sig') as file:
                    read_sohwan = file.read().splitlines()

                for i in range(len(read_sohwan)):
                    is_sohwan = False
                    for x in range(5):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\max.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(515, 565, 570, 610, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            is_sohwan = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_2(525, 625, cla)
                            time.sleep(0.2)
                            click_pos_2(525, 625, cla)
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sohwan_list\\" + read_sohwan[i] + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(125, 75, 800, 600, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                                click_pos_2(900, 1015, cla)
                                for k in range(10):
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\max.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(515, 565, 570, 610, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    time.sleep(0.5)
                        time.sleep(0.3)
                    if is_sohwan == True:

                        exit_ready = False
                        exit_ready_count = 0
                        while exit_ready is False:
                            exit_ready_count += 1
                            if exit_ready_count > 20:
                                exit_ready = True

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sohwan_exit.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 950, 800, 1050, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sohwan_continue2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 950, 800, 1050, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    exit_ready_count = 0
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.2)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sohwan_exit.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 950, 800, 1050, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.2)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    exit_ready = True
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\barobogi.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(390, 970, 550, 1050, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.2)
                                else:
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sohwan__confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(300, 970, 700, 1050, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.2)
                                    else:
                                        tuto_grow_skip(cla)
                            time.sleep(0.4)

                        for y in range(100):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\bag_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\barobogi.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(390, 970, 550, 1050, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.2)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sohwan_continue2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 950, 800, 1050, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.2)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sohwan_exit.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 950, 800, 1050, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.2)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sohwan__confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 970, 700, 1050, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.2)
                                else:
                                    tuto_grow_skip(cla)
                            time.sleep(1)
                for z in range(5):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sohwan_exit.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 970, 700, 1050, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\bag_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                    time.sleep(1)

                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(90, 290, 115, 350, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(50, 320, cla)
                    time.sleep(0.5)

                dir_path = "C:\\my_games\\ares"
                file_path = dir_path + "\\data_ares\\imgs\\get_items\\box_list\\box_list.txt"

                with open(file_path, "r", encoding='utf-8-sig') as file:
                    read_box = file.read().splitlines()

                for i in range(len(read_box)):
                    is_box = False
                    for x in range(5):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\max.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(515, 565, 570, 610, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            is_box = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_2(525, 625, cla)
                            time.sleep(0.2)
                            click_pos_2(525, 625, cla)
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\box_list\\" + read_box[
                                i] + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(125, 75, 800, 600, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                                click_pos_2(900, 1015, cla)
                                for k in range(10):
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\max.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(515, 565, 570, 610, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    time.sleep(0.5)
                        time.sleep(0.3)
                    if is_box == True:
                        for b in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\clicked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(90, 290, 115, 350, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                click_pos_2(50, 320, cla)
                            time.sleep(0.5)



                # bag 창 닫기
                for i in range(5):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\bag_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(940, 50, cla)
                    else:
                        break
                    time.sleep(0.2)
                time.sleep(0.1)
            else:
                menu_open(cla)
                time.sleep(0.2)
                click_pos_2(905, 55, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\bag_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)
            time.sleep(1)




    except Exception as e:
        print(e)
        return 0

def get_mission_bosang(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import menu_open

    try:
        print("get_mission_bosang")
        mission_ready = False
        mission_ready_count = 0
        while mission_ready is False:
            mission_ready_count += 1
            if mission_ready_count > 5:
                mission_ready = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\mission_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("get_mission_bosang 창 열렸다.")
                mission_ready = True

                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_mission_bosang_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(130, 840, 960, 870, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("get_mission_bosang_point_1 -80, +10 ", imgs_)
                        click_pos_reg(imgs_.x - 80, imgs_.y + 10, cla)

                        for x in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\mission_get_complete.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 400, 530, 445, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.2)


                        for y in range(5):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\mission_get_complete.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 400, 530, 445, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("get_mission_bosang_point_1 -80, +10 ", imgs_)
                                click_pos_reg(imgs_.x - 80, imgs_.y + 10, cla)
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\mission_get_cancle.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(390, 560, 450, 610, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                break
                            time.sleep(0.2)
                        for z in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\mission_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                click_pos_2(470, 930, cla)
                            time.sleep(0.2)
                time.sleep(1)
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\mission_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(424, 934, cla)
                    time.sleep(0.5)


                for i in range(10):

                    is_point = False

                    for z in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\mission_get_arescoin_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(230, 970, 960, 1015, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("mission_get_arescoin_1 ", imgs_)
                            click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                            is_point = True
                            break
                        else:
                            # break
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\mission_get_arescoin_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(230, 970, 960, 1015, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("mission_get_arescoin_1 ", imgs_)
                                click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                                is_point = True
                                break
                        time.sleep(0.2)

                    if is_point == True:
                        for x in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\mission_get_complete.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 400, 530, 445, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.2)

                        for y in range(5):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\mission_get_complete.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 400, 530, 445, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("get_mission_bosang_point_1 -80, +10 ", imgs_)
                                click_pos_reg(imgs_.x - 80, imgs_.y + 10, cla)
                            else:
                                break
                            time.sleep(0.3)
                        for z in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\mission_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                click_pos_2(470, 930, cla)
                            time.sleep(0.2)
                    else:
                        break


            else:
                menu_open(cla)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_post_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(865, 255, 900, 290, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x - 8, imgs_.y + 10, cla)
                else:
                    mission_ready = True
            time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\mission_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 50, cla)
            else:
                break
            time.sleep(0.2)
        time.sleep(0.1)



    except Exception as e:
        print(e)
        return 0


def get_sangjum_sohwan(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import menu_open

    try:
        print("get_sangjum_sohwan")
        sohwan_ready = False
        sohwan_ready_count = 0
        while sohwan_ready is False:
            sohwan_ready_count += 1
            if sohwan_ready_count > 5:
                sohwan_ready = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\sangjum_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("sangjum_title 열렸다.")


                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\gold_sohwan.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 165, 70, 215, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("gold_sohwan 열렸다.")

                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\clicked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(90, 165, 115, 215, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\gold_sohwan.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 165, 70, 215, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                    sohwan_ready = True

                    # 슈트
                    print("슈트")
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\buy_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 240, 220, 280, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break

                        else:

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\sohwan_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 390, 600, 420, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\max.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 540, 530, 590, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\gold_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(500, 630, 560, 690, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\exit.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(370, 970, 545, 1035, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                else:
                                    click_pos_2(200, 260, cla)
                                    for k in range(10):
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\sohwan_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(470, 390, 600, 420, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\soolyung.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(430, 390, 520, 450, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                break
                                        time.sleep(0.1)
                            time.sleep(0.5)

                    # 오퍼레이터
                    print("오퍼레이터")
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\buy_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(290, 240, 400, 280, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break

                        else:

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\sohwan_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 390, 600, 420, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\max.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 540, 530, 590, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\gold_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(500, 630, 560, 690, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\exit.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(370, 970, 545, 1035, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                else:
                                    click_pos_2(350, 260, cla)
                                    for k in range(10):
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\sohwan_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(470, 390, 600, 420, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\soolyung.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(430, 390, 520, 450, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                break
                                        time.sleep(0.1)
                            time.sleep(0.5)

                    # 탈것 소환
                    print("탈것")
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\buy_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(430, 240, 540, 280, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break

                        else:

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\sohwan_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 390, 600, 420, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\max.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 540, 530, 590, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\gold_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(500, 630, 560, 690, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\exit.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(370, 970, 545, 1035, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                else:
                                    click_pos_2(500, 260, cla)
                                    for k in range(10):
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\sohwan_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(470, 390, 600, 420, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\soolyung.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(430, 390, 520, 450, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                break
                                        time.sleep(0.1)
                            time.sleep(0.5)
                    # 데코 소환
                    print("데코")
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\buy_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 240, 680, 280, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break

                        else:

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\sohwan_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 390, 600, 420, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\max.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 540, 530, 590, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\gold_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(500, 630, 560, 690, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\exit.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(370, 970, 545, 1035, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                else:
                                    click_pos_2(650, 260, cla)
                                    for k in range(10):
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\sohwan_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(470, 390, 600, 420, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\soolyung.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(430, 390, 520, 450, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                break
                                        time.sleep(0.1)
                            time.sleep(0.5)

                    # 몬스터코어 소환
                    print("몬스터코어")
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\buy_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(740, 240, 840, 280, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break

                        else:

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\sohwan_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 390, 600, 420, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\max.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 540, 530, 590, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\gold_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(425, 630, 560, 690, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\exit.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(370, 970, 545, 1035, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                else:
                                    click_pos_2(790, 260, cla)
                                    for k in range(10):
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\sohwan_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(470, 390, 600, 420, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\soolyung.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(430, 390, 520, 450, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                break
                                        time.sleep(0.1)
                            time.sleep(0.5)


                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\gold_sohwan.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 165, 70, 215, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\sohwan_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(150, 55, 250, 120, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("sohwan_click 열렸다.")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)



            else:
                menu_open(cla)
                time.sleep(0.1)
                click_pos_2(840, 60, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\sangjum_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.3)
            time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\sangjum_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 50, cla)
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sangjum_sohwan\\exit.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(370, 970, 445, 1035, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                else:
                    break
            time.sleep(0.2)
        time.sleep(0.1)



    except Exception as e:
        print(e)
        return 0
