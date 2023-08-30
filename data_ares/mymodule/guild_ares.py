import sys
import time

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def guild_attendance(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import menu_open
    try:
        print("guild_attendance")

        attendance = False
        guild_count = 0
        while attendance is False:
            guild_count += 1
            if guild_count > 7:
                attendance = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\guild_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                time.sleep(0.2)

                # 길드 정보
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\guild\\guild_information.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 75, 80, 120, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)

                    attendance = True
                    # 길드 출석
                    for i in range(5):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\guild\\box_open.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(520, 580, 610, 650, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                            click_pos_2(55, 1015, cla)
                            time.sleep(0.5)
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\guild\\attendance_check.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 980, 200, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.7)

                    # 길드 기부
                    for i in range(5):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\guild\\guild_donation_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(440, 360, 515, 405, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\guild\\gold.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(340, 390, 430, 480, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.7)

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\guild\\max.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(540, 550, 620, 600, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.7)

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\guild\\guild_donation_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(390, 650, 570, 700, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.7)
                                break

                        else:

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\guild\\guild_donation.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 980, 200, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.7)

                    # 길드 멤버
                    for t in range(2):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\guild\\guild_member.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(80, 75, 160, 120, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                        click_pos_2(825, 1015, cla)
                        time.sleep(0.5)
                        click_pos_2(925, 1015, cla)
                        time.sleep(0.5)

                else:
                    attendance = True

            else:
                menu_open(cla)
                time.sleep(0.5)
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\guild\\menu_guild.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(780, 210, 960, 360, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\guild_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)

        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\guild_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 50, cla)
            else:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0




