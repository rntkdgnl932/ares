import time
# import os
import sys

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def gardiun_mission_start(cla, schedule):
    from potion_ares import juljun_potion_check
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg
    try:
        print("gardiun_mission_start")
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\gardiun_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 10, 70, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_select2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(735, 955, 815, 1025, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)
                gardiun_mission_get(cla, schedule)
        else:
            result_quest = juljun_quest_check(cla)
            if result_quest == False:
                gardiun_mission_get(cla, schedule)
            else:
                juljun_potion_check(cla)
    except Exception as e:
        print(e)
        return 0


def gardiun_mission_get(cla, schedule):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import maul_go, map_in, loading_ares, confirm_all
    from potion_ares import maul_potion_gardiun
    from schedule import myQuest_play_add
    try:
        print("gardiun_mission_get")

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\gardiun_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 10, 70, 100, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("가디언 미션 진입 ㅇㅋ")
        else:
            maul_go(cla)
            maul_potion_gardiun(cla)
            # map_in(cla)


        mission_get_ = False
        mission_get_count = 0
        while mission_get_ is False:
            mission_get_count += 1
            if mission_get_count > 7:
                mission_get_ = True


            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\gardiun_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 70, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_select2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(735, 955, 815, 1025, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\complete_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(175, 110, 200, 1040, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("complete_point_2", imgs_)
                    for get in range(20):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\gardiun_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 70, 100, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\complete_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(175, 110, 200, 1040, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x - 100, imgs_.y + 15, cla)
                                time.sleep(0.5)
                                click_pos_2(855, 1015, cla)
                                time.sleep(0.5)
                                click_pos_reg(imgs_.x - 100, imgs_.y + 15, cla)
                                time.sleep(0.5)
                            else:
                                break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\complete\\complete_3.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 350, 550, 500, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("gardiun_complete_3")
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                            time.sleep(0.5)
                else:
                    # 모두 수락하기
                    print("모두 수락하기")
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 570, 610, 610, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            mission_get_ = True

                            for z in range(20):
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("loding...")
                                    loading_ares(cla)
                                    break
                                time.sleep(0.7)

                            moving_count = 0
                            for k in range(20):
                                moving_count += 1
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_moving.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(815, 935, 915, 1030, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("사냥터이동중", moving_count)
                                    time.sleep(1)
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    time.sleep(1)
                                time.sleep(0.7)

                            break
                        else:

                            # r 등급 취소하기
                            print("r 등급 취소하기r 등급 취소하기r 등급 취소하기")
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\r_grade.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(5, 110, 60, 1040, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)

                                for g in range(10):
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\r_grade.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(5, 110, 60, 1040, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(1)

                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\give_up_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(860, 990, 960, 1040, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(2)
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\give_up_confirm.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(480, 560, 600, 610, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(1)

                                    else:
                                        break
                                    time.sleep(1)

                                print("리프레시")
                                for r in range(10):
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\r_grade.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(5, 110, 60, 1040, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\mission_refresh_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(430, 460, 510, 500, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_2(480, 590, cla)
                                        else:
                                            click_pos_2(90, 1015, cla)
                                    else:
                                        break
                                    time.sleep(1)
                            # 수락하기 버튼
                            print("수락하기 버튼수락하기 버튼수락하기 버튼")
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_soolock.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 990, 900, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_move.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(780, 990, 840, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)
                                else:
                                    # 1.96
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_map_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(940, 50, cla)
                                    else:
                                        click_pos_2(800, 1010, cla)
                                    time.sleep(1)

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\anymore_no_soolyung.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 80, 620, 140, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("더이상 수령할수 없음...미션 시작하기")

                                time.sleep(0.5)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_start_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(150, 240, 200, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                    click_pos_2(815, 1015, cla)
                                    time.sleep(0.5)

                            else:

                                any_more = False

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\anymore_no_soolyung_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 80, 700, 140, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    any_more = True
                                    print("더이상 수령할수 없음...미션 시작하기2")
                                else:
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\anymore_no_soolyung_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(300, 80, 700, 140, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        any_more = True
                                        print("더이상 수령할수 없음...미션 시작하기3")

                                if any_more == True:
                                    time.sleep(0.5)

                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_start_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(150, 240, 200, 1040, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.5)
                                        click_pos_2(815, 1015, cla)
                                        time.sleep(0.5)

                                        # confirm
                                        confirm_all(cla)
                                    else:


                                        # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_complete.PNG"
                                        # img_array = np.fromfile(full_path, np.uint8)
                                        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        # imgs_ = imgs_set_(140, 940, 210, 1010, cla, img, 0.8)
                                        # if imgs_ is not None and imgs_ != False:

                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_complete_zero.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(140, 940, 210, 1010, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("가디언 스케쥴 완료")
                                            mission_get_ = True
                                            myQuest_play_add(cla, schedule)
                                            click_pos_2(940, 50, cla)
                                            break
                                        else:
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_complete_zero2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(140, 940, 210, 1010, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("가디언 스케쥴 완료2")
                                                mission_get_ = True
                                                myQuest_play_add(cla, schedule)
                                                click_pos_2(940, 50, cla)
                                                break
                                        # else:
                                        #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_start_1.PNG"
                                        #     img_array = np.fromfile(full_path, np.uint8)
                                        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        #     imgs_ = imgs_set_(150, 240, 200, 1040, cla, img, 0.8)
                                        #     if imgs_ is not None and imgs_ != False:
                                        #         click_pos_reg(imgs_.x, imgs_.y, cla)
                                        #         time.sleep(0.5)
                                        #         click_pos_2(815, 1015, cla)
                                        #         time.sleep(0.5)

                        time.sleep(1)

                    # R 등급 빼기
            else:
                map_in(cla)
                time.sleep(0.5)
                print("가디언npc 찾자")
                for i in range(10):

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_move.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1060, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jadong_move : break", i)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for c in range(20):
                            print("gardiun_title", c)
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\gardiun_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 70, 100, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("gardiun_title : break", c, imgs_)
                                break
                            else:
                                print("gardiun_title : ing", c)
                            time.sleep(2)
                        break
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_npc.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 300, 660, 700, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_npc2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 300, 660, 700, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\ran_npc.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 300, 660, 700, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_move.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 0, 960, 1060, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("jadong_move : ing", i)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(1)
                                        map_in(cla)
                                        time.sleep(0.5)
                    time.sleep(0.5)
                # for z in range(10):
                #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\gardiun_title.PNG"
                #     img_array = np.fromfile(full_path, np.uint8)
                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #     imgs_ = imgs_set_(800, 990, 900, 1040, cla, img, 0.8)
                #     if imgs_ is not None and imgs_ != False:
                #         break
                #     time.sleep(1)
            time.sleep(0.5)
        time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\gardiun_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 70, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                # r 등급 취소하기
                print("r 취소리")
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\r_grade.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(5, 110, 60, 1040, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)

                    for g in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\r_grade.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(5, 110, 60, 1040, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\give_up_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(860, 990, 960, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(2)
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\give_up_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 560, 600, 610, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)

                        else:
                            break
                        time.sleep(1)

                    for r in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\r_grade.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(5, 110, 60, 1040, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\mission_refresh_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 460, 510, 500, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(480, 590, cla)
                            else:
                                click_pos_2(90, 1015, cla)
                        else:
                            break
                        time.sleep(1)

                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_start_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(150, 240, 200, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        click_pos_2(815, 1015, cla)
                        time.sleep(0.5)
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\gardiun_soolock.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 990, 900, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\anymore_no_soolyung_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 80, 700, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("더이상 수령할수 없음...나가기")
                            click_pos_2(940, 50, cla)

            else:
                break
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0


def gardiun_quest_click_before(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg

    try:
        print("region_quest_click_before")

        ing_now = False

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\gardiun_mission\\click_check_gardiun.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 110, 935, 145, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("click_check")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            ing_now = True
        return ing_now
    except Exception as e:
        print(e)
        return 0


def juljun_quest_check(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, drag_pos
    from action_ares import out_check, clean_screen, juljun_time_check
    try:
        print("juljun_quest_check")
        go_ = False

        quest_check = False
        quest_check_count = 0
        while quest_check is False:
            quest_check_count += 1
            if quest_check_count > 5:
                quest_check = True
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:

                # 시간체크
                juljun_time_check(cla)

                quest_check = True

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_quest_ing.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 400, 570, 470, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("가디언 퀘스트중1")
                    go_ = True
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_quest_complete.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 400, 570, 470, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("가디언 완료...???")
                        time.sleep(10)
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_quest_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 400, 570, 470, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("가디언 완료...!!!")
                            go_ = False
                        else:
                            print("가디언 온전히 완료 아님...")
                            go_ = True
                    else:
                        for k in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_quest.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 400, 570, 470, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("가디언 퀘스트중2")
                                go_ = True
                                break
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_ready.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 400, 570, 470, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("가디언 퀘스트 : 대기중")
                                go_ = False
                                break
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_attack.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 400, 570, 470, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("가디언 퀘스트 : 자동사냥중")
                                go_ = False
                                break
                            time.sleep(1)
            else:
                result_out = out_check(cla)
                if result_out == True:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    clean_screen(cla)
                time.sleep(1)

        if go_ == True:
            print("v_.gardiun_juljun_count : 60번 마다 체크하기", v_.gardiun_juljun_count)
            v_.gardiun_juljun_count += 1
            if v_.gardiun_juljun_count > 59:
                v_.gardiun_juljun_count = 0
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    # 시간체크
                    juljun_time_check(cla)

                    drag_pos(405, 605, 945, 605, cla)
                    time.sleep(1)
                    for i in range(10):
                        result_out = out_check(cla)
                        if result_out == True:

                            result_gardiun_ing = gardiun_quest_ing(cla)

                            if result_gardiun_ing == True:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)
                                    break
                            else:
                                go_ = False
                                break
                        time.sleep(1)



        return go_
    except Exception as e:
        print(e)
        return 0

def gardiun_quest_ing(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg

    try:
        print("gardiun : gardiun_quest_ing")

        ing_1 = False
        ing_2 = False

        for i in range(15):

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\quest_ing\\quest_ing_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 100, 800, 180, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("gardiun : quest_ing_1...1")

                click_pos_reg(imgs_.x + 50, imgs_.y, cla)

                time.sleep(0.5)

                click_pos_reg(imgs_.x + 50, imgs_.y, cla)

                ing_1 = True
                break

            time.sleep(0.1)

        time.sleep(0.5)

        if ing_1 == True:

            for i in range(15):

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\quest_ing\\quest_ing_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 100, 800, 180, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("gardiun : quest_ing_1...2")
                    ing_2 = True
                    break
                time.sleep(0.1)



        return ing_2
    except Exception as e:
        print(e)
        return 0

