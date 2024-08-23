import time
import sys


sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_

def dead_die(cla, schedule):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from get_items import get_item_start
    from massenger import line_to_me
    from schedule import myQuest_play_add
    from potion_ares import maul_potion_get

    try:
        print("dead_die")

        deaded = False

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_potal.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(270, 800, 600, 1030, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            deaded = True
            click_pos_reg(imgs_.x, imgs_.y, cla)

            for i in range(10):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("loding")
                    loading_ares(cla)
                    break
                time.sleep(1)
            for i in range(10):
                result_out = out_check(cla)
                if result_out == True:
                    break
                time.sleep(1)
            # 물약 사자~!
            result_maul = maul_go(cla)
            if result_maul == True:
                maul_potion_get(cla)

        if deaded == True:
            if schedule == "튜토육성":
                get_item_start(cla)
                why = "튜토하다 죽었다. 손 좀 보자"
                line_to_me(cla, why)
            elif schedule == "메인퀘스트":
                get_item_start(cla)
                why = "메인퀘하다 죽었다. 손 좀 보자"
                line_to_me(cla, why)
                myQuest_play_add(cla, schedule)
            elif "지역퀘스트" in schedule:
                get_item_start(cla)
                why = "지역퀘스트 죽었다. 손 좀 보자"
                line_to_me(cla, why)
                myQuest_play_add(cla, schedule)

        deaded2 = False

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_before.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(150, 60, 185, 105, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            deaded = True
            deaded2 = True
        else:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_before_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(150, 60, 185, 105, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                deaded = True
                deaded2 = True

        if deaded2 == True:

            for i in range(10):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_before2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 380, 530, 430, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    break
                time.sleep(0.3)

            dead_ = False
            dead_count = 0
            while dead_ is False:
                dead_count += 1
                if dead_count > 5:
                    dead_ = True
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_before2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 380, 530, 430, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    dead_ = True
                    for i in range(20):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_before2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(420, 380, 530, 430, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:

                            click_pos_2(475, 655, cla)
                            time.sleep(0.5)

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_before_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 560, 585, 615, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                        else:
                            break
                        time.sleep(1)


                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_before.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(150, 60, 185, 105, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_before_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 60, 185, 105, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)

        # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(280, 40, 960, 300, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_potal.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(270, 800, 600, 1030, cla, img, 0.7)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_reg(imgs_.x, imgs_.y, cla)
        # else:
        #     full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_potal.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(270, 800, 600, 1030, cla, img, 0.7)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_reg(imgs_.x, imgs_.y, cla)

        if deaded == True or deaded2 == True:
            if '타루크기지' in schedule:
                v_.talook_dead += 1
                print("타루크기지 카운트", v_.talook_dead)
                if v_.talook_dead > 3:
                    myQuest_play_add(cla, schedule)
                    time.sleep(0.1)

        return deaded
    except Exception as e:
        print(e)
        return 0

def clean_screen(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, drag_pos, click_pos_2
    from massenger import line_to_me
    from main_grow import grow_skip, grow_complete
    from log_ares import character_change
    from schedule import myQuest_play_check
    from stop_event18 import _stop_please
    import os

    try:
        print("clean_screen")

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\game_ares_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            for i in range(2):

                print("클린스크린 순환", i + 1)

                # 절전모드일 경우 풀기
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    drag_pos(405, 605, 945, 605, cla)


                # 캐릭 선택 화면
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\character_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 110, 70, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    result_schedule = myQuest_play_check(cla, "check")
                    print("result_schedule", result_schedule)
                    character_id = result_schedule[0][1]
                    result_schedule_ = result_schedule[0][2]

                    character_change(cla, character_id)
                    time.sleep(0.2)

                # 팝업창 끄기
                _stop_please(cla)

                # 지역퀘스트 골드창 그기
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\region_quest\\region_gold_click_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(340, 380, 440, 450, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y - 100, cla)
                    time.sleep(1)
                    confirm_all(cla)



                # 죽었을때
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_potal.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(270, 800, 600, 1030, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    result_schedule = myQuest_play_check(cla, "check")
                    print("clean_screen => dead_die : result_schedule", result_schedule)

                    dead_die(cla, result_schedule)

                # 도전 등 시간 표시일때 닫기

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\time_close_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(115, 60, 160, 110, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("바깥화면")

                else:
                    print("바깥화면 아님...")
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\time.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(810, 30, 960, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(940, 50, cla)

                        for t in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\time_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 555, 630, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:

                                    loading_ares(cla)
                                    break
                            time.sleep(0.3)

                # 메뉴 닫기
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\menu\\friend.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(810, 290, 870, 350, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(935, 50, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\menu\\friend2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(810, 290, 870, 350, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(935, 50, cla)
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\menu\\menu_dojun.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 200, 100, 360, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(935, 50, cla)
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\menu\\menu_hyubdong.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 200, 100, 360, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(935, 50, cla)
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\menu\\menu_gyungjang.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 200, 100, 360, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(935, 50, cla)

                # 아이템 소환 후 닫기
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\sohwan_exit.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 970, 700, 1050, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)

                # skip
                grow_skip(cla)
                grow_complete(cla)

                # post 받고 난 후
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\post_get.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 400, 560, 460, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                # 이벤트 보상 닫기
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\space_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 620, 540, 700, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\space_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 620, 540, 700, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)


                # event 닫기
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\x_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(745, 360, 800, 400, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                # 적대 길드 닫기
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\oppose_guild.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 430, 530, 480, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(540, 600, cla)

                # 각종 활성화 되어 있는 title 닫기
                for z in range(3):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\x_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(915, 20, 960, 70, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\clean_screen\\x_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(915, 20, 960, 70, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            break
                    time.sleep(0.1)

                result_out = out_check(cla)
                if result_out == True:
                    break

        else:
            print("clean_screen : 아레스 꺼져있는지 10초간 다시 검사하기")
            is_ares = False

            for i in range(10):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\game_ares_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    is_ares = True
                    break
            if is_ares == False:
                why = "아레스 꺼진게 확실하다"
                print(why)
                line_to_me(cla, why)

                dir_path = "C:\\my_games\\load\\ares"
                file_path = dir_path + "\\start.txt"
                # cla.txt
                cla_data = str(cla) + "cla"
                file_path2 = dir_path + "\\" + cla_data + ".txt"
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    data = 'no'
                    file.write(str(data))
                    time.sleep(0.2)
                with open(file_path2, "w", encoding='utf-8-sig') as file:
                    data = cla
                    file.write(str(data))
                    time.sleep(0.2)
                os.execl(sys.executable, sys.executable, *sys.argv)



    except Exception as e:
        print(e)
        return 0

def out_check(cla):
    import numpy as np
    import cv2
    from function import imgs_set_
    from massenger import line_to_me

    try:
        print("out_check")

        go_ = False

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            juljun_time_check(cla)
        else:

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\out\\camera.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 970, 40, 1015, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                go_ = True
                v_.screen_error = 0
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    go_ = True
                    v_.screen_error = 0
                else:
                    v_.screen_error += 1
                    print("v_.screen_error 200 이상일 때 메세지", v_.screen_error)
                    if v_.screen_error > 200:
                        why = "화면에 버튼 사라지는 에러"
                        line_to_me(cla, why)
                        v_.screen_error = 0

        return go_
    except Exception as e:
        print(e)
        return 0

def menu_open(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from get_items import get_post

    try:
        print("menu_open")
        menu_look = False
        menu_look_count = 0
        while menu_look is False:
            menu_look_count += 1
            if menu_look_count > 7:
                menu_look = True


            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\menu\\friend.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(810, 290, 870, 350, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_post_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 350, 830, 375, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    get_post(cla)
                else:
                    menu_look = True
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\menu\\friend2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(810, 290, 870, 350, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\get_items\\get_post_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 350, 830, 375, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        get_post(cla)
                    else:
                        menu_look = True
                else:
                    result_out = out_check(cla)

                    if result_out == True:
                        click_pos_2(935, 40, cla)
                    else:
                        clean_screen(cla)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0


def menu_open_just(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("menu_open_just")
        menu_look = False
        menu_look_count = 0
        while menu_look is False:
            menu_look_count += 1
            if menu_look_count > 5:
                menu_look = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\menu\\friend.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(810, 290, 870, 350, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                menu_look = True
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\menu\\friend2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(810, 290, 870, 350, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    menu_look = True
                else:
                    result_out = out_check(cla)

                    if result_out == True:
                        click_pos_2(935, 40, cla)
                    else:
                        clean_screen(cla)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0

def bag_open(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("bag_open")
        bag_look = False
        bag_look_count = 0
        while bag_look is False:
            bag_look_count += 1
            if bag_look_count > 5:
                bag_look = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\bag\\bag_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                bag_look = True
            else:
                menu_open(cla)
                click_pos_2(900, 50, cla)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0

def moving_m(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg

    try:
        print("moving_m")

        move_ = False
        move_count = 0

        while move_ is False:
            move_count += 1
            if move_count > 100:
                move_ = True

            time.sleep(3)
            now_moving = False

            # 고정 위치...의미 있음
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\move\\move_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(880, 80, 960, 110, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("move_2222222222222222222222222") # 추후에 지워야할듯?
                move_count = 0
                now_moving = True
            else:
                move_ = True
            time.sleep(0.1)


        return now_moving
    except Exception as e:
        print(e)
        return 0


# def shot_all(cla):
#     import numpy as np
#     import cv2
#     from function import imgs_set_, click_pos_reg
#
#     try:
#         print("shot_all")
#
#         shots_ = False
#
#         full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\shot\\shot_1.PNG"
#         img_array = np.fromfile(full_path, np.uint8)
#         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#         imgs_ = imgs_set_(180, 180, 740, 740, cla, img, 0.7)
#         if imgs_ is not None and imgs_ != False:
#             shots_ = True
#
#         full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\shot\\shot_2.PNG"
#         img_array = np.fromfile(full_path, np.uint8)
#         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#         imgs_ = imgs_set_(180, 180, 740, 740, cla, img, 0.7)
#         if imgs_ is not None and imgs_ != False:
#             shots_ = True
#
#         shots_count = 0
#         while shots_ is True:
#             shots_count += 1
#             if shots_count > 30:
#                 shots_ = False
#             full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\shot\\shot_1.PNG"
#             img_array = np.fromfile(full_path, np.uint8)
#             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#             imgs_ = imgs_set_(180, 180, 740, 740, cla, img, 0.7)
#             if imgs_ is not None and imgs_ != False:
#                 shots_count = 0
#                 click_pos_reg(imgs_.x, imgs_.y, cla)
#
#             full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\shot\\shot_2.PNG"
#             img_array = np.fromfile(full_path, np.uint8)
#             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#             imgs_ = imgs_set_(180, 180, 740, 740, cla, img, 0.7)
#             if imgs_ is not None and imgs_ != False:
#                 shots_count = 0
#                 click_pos_reg(imgs_.x, imgs_.y, cla)
#             time.sleep(0.1)
#
#
#
#
#     except Exception as e:
#         print(e)
#         return 0

def confirm_all(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg

    try:
        print("confirm_all")

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\confirm\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 560, 610, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 1_7 가방 열어서..
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\confirm\\confirm_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 565, 605, 605, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 2_1 지역퀘스트
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\region_quest_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 560, 600, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_1_region_quest\\soolock.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 620, 580, 660, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 2_2 드레스 확인
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\tuto\\explain\\chap_2_2_select_dress\\dress_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 560, 610, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # map maul
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 560, 610, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 자동사냥
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # potion
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\potion\\potion_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 600, 570, 660, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 몬스터 도감
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\powerup\\monster_dogam_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 580, 580, 630, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 수집
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\soojib\\soojib_setting_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 640, 640, 680, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 분해
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 600, 600, 640, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        # 분해2
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\boonhae\\boonhae_confirm2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 640, 570, 670, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        # 행성파견
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\hangsungpagyun_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        # 레이드 자동입장
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\jadong_in_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 570, 610, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        # 도전(행성파견, 성운돌파)
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\dojun_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        # 성운돌파
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\sungwoondolpa_yes.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # dead
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dead\\dead_before_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 560, 585, 615, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 다크디멘젼
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\dark_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 560, 560, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 던전 투력 부족 승인하기
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\dun_in_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 560, 600, 610, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        print(e)
        return 0


def maul_go(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("maul_go")
        for i in range(3):
            result_out = out_check(cla)
            if result_out == True:
                break
            else:
                clean_screen(cla)
            time.sleep(0.5)

        maul_in = False
        maul_in_count = 0
        while maul_in is False:
            maul_in_count += 1
            print("maul_in_count", maul_in_count)
            if maul_in_count > 7:
                maul_in = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\gwangjang.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 50, 50, 100, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("마을 도착")
                maul_in = True

            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\map_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\gardiun_tower_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 10, 150, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        for i in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\gwangjang.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 50, 50, 100, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("광장 도착1", imgs_)
                                maul_in = True
                                break
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\gwangjang2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 50, 50, 100, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("광장 도착2", imgs_)
                                    maul_in = True
                                    break
                                else:
                                    click_pos_2(940, 50, cla)
                            time.sleep(2)
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 560, 610, 610, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            x_reg = imgs_.x
                            y_reg = imgs_.y
                            for i in range(10):

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("loding")
                                    loading = True
                                    loading_count = 0
                                    while loading is True:
                                        loading_count += 1
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            print("loding", loading_count)
                                        else:
                                            loading = False
                                        time.sleep(1)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\gwangjang.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 50, 50, 100, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("광장 도착", imgs_)
                                    maul_in = True
                                    break
                                else:
                                    click_pos_reg(x_reg, y_reg, cla)
                                time.sleep(2)

                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\gardiun_tower.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 940, 120, 1010, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                for i in range(10):
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\maul\\confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 560, 610, 610, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    time.sleep(0.2)

                else:
                    # 지도 클릭
                    map_in(cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\map_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
                    time.sleep(0.2)
        return maul_in


    except Exception as e:
        print(e)
        return 0

def loading_ares(cla):
    import numpy as np
    import cv2
    from function import imgs_set_

    try:
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("loding")
            loading = True
            loading_count = 0
            while loading is True:
                loading_count += 1
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("loding", loading_count)
                else:
                    loading = False
                time.sleep(1)
    except Exception as e:
        print(e)
        return 0



def map_in(cla):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_
    try:
        print("map_in")
        clean_screen(cla)
        time.sleep(0.5)

        click_pos_2(25, 50, cla)
        time.sleep(0.1)
        click_pos_2(65, 115, cla)

        quest_ing = False

        for i in range(5):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\map\\not_open_map.png"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 90, 700, 160, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                quest_ing = True
                click_pos_2(780, 60, cla)
                time.sleep(0.2)
                confirm_all(cla)
                break
            time.sleep(0.1)

            if quest_ing == True:
                break

        if quest_ing == True:
            for i in range(10):
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(25, 50, cla)
                    time.sleep(0.1)
                    click_pos_2(65, 115, cla)
                    break
                time.sleep(0.5)

        for i in range(10):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\map_in.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 100, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0

def mine_check(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2, text_check_get, in_number_check, int_put_
    from schedule import myQuest_play_add

    try:
        print("mine_check")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3

        gold_ = 0
        dia_ = 0
        gold_check = False
        dia_check1 = False
        dia_check2 = False

        monster_in = False
        monster_in_count = 0
        while monster_in is False:
            monster_in_count += 1
            if monster_in_count > 7:
                monster_in = True
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\auction_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 150, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                monster_in = True
                print("거래소 오픈")

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\property\\gold.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 30, 800, 70, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("gold", imgs_)
                    gold_check = True
                    # 749
                    x_reg_1 = imgs_.x - plus
                    for i in range(4):
                        read_gold = text_check_get(x_reg_1 + 10 + i, 35, 825, 55, cla)
                        if read_gold == "":
                            print("골드 못 읽음")
                        else:
                            print("read_gold", read_gold)
                            break
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\property\\gold2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(650, 30, 800, 70, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("gold2", imgs_)
                        gold_check = True
                        # 749
                        x_reg_1 = imgs_.x - plus
                        for i in range(4):
                            read_gold = text_check_get(x_reg_1 + 10 + i, 40, 825, 55, cla)
                            if read_gold == "":
                                print("골드 못 읽음")
                            else:
                                print("read_gold", read_gold)
                                break
                if gold_check == True:
                    digit_ready = in_number_check(read_gold)
                    print("digit_ready", digit_ready)
                    if digit_ready == True:
                        read_data_int = int(int_put_(read_gold))
                        print("read_data_int", read_data_int)
                        gold_ = read_data_int

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\property\\dia.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 30, 800, 70, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("dia", imgs_)
                    dia_check1 = True
                    x_reg_2 = imgs_.x - plus
                    # 675
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\property\\dia2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(650, 30, 800, 70, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("dia2", imgs_)
                        dia_check1 = True
                        x_reg_2 = imgs_.x - plus
                        # 675
                if dia_check1 == True:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\property\\dia_end.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(650, 30, 870, 70, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("dia_end", imgs_)
                        dia_check2 = True
                        x_reg_2_2 = imgs_.x - plus
                        # 726
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\property\\dia_end2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(650, 30, 870, 70, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("dia_end2", imgs_)
                            dia_check2 = True
                            x_reg_2_2 = imgs_.x - plus
                            # 726
                if dia_check2 == True:
                    for i in range(4):
                        read_dia = text_check_get(x_reg_2 + 10 + i, 40, x_reg_2_2 - 5, 55, cla)
                        if read_dia == "":
                            print("다이아 못 읽음")
                        else:
                            print("read_dia", read_dia)
                            break

                    digit_ready = in_number_check(read_dia)
                    print("digit_ready", digit_ready)
                    if digit_ready == True:
                        read_data_int = int(int_put_(read_dia))
                        print("read_data_int", read_data_int)
                        dia_ = read_data_int


            else:
                menu_open(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\auction_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\menu\\friend.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(810, 290, 870, 350, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(810, 240, cla)
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\action\\menu\\friend2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(810, 290, 870, 350, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(810, 240, cla)

                    time.sleep(1)






        return gold_, dia_

    except Exception as e:
        print(e)
        return 0





def juljun_time_check(cla):
    import numpy as np
    import cv2
    import os
    from function import imgs_set_
    from datetime import datetime
    from massenger import line_to_me
    try:
        print("juljun_time_check")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3

        nowTime = int(datetime.today().strftime("%M"))

        print("nowTime", nowTime)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_time\\slush.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(440, 75, 530, 135, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("slush", imgs_)
            x_start = imgs_.x - plus

            now_time = ""

            for i in range(10):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_time\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_start, 75, 600, 135, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("자리", i, imgs_)

            for i in range(10):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_time\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_start, 75, x_start + 42, 135, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("10 자리", i, imgs_)
                    x_start = imgs_.x - plus
                    now_time += str(i)
                    break

            for i in range(10):
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_time\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_start, 75, x_start + 42, 135, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("1 자리", i, imgs_)
                    now_time += str(i)
                    break



            if now_time == "":
                print("값이 없다")
            else:
                now_time = int(now_time)
                print("now_time", now_time)

                if nowTime >= 50 and now_time < 10:
                    now_time += 60
                elif now_time >= 50 and nowTime < 10:
                    nowTime += 60

                result_cal = abs(nowTime - now_time)

                if result_cal > 19:
                    print("멈춰있는 상태", result_cal)

                    why = str(result_cal) + "분 차이...다운되거나 인터넷이 끊긴것이 확실하다"
                    print(why)
                    line_to_me(cla, why)

                    dir_path = "C:\\my_games\\load\\ares"
                    file_path = dir_path + "\\start.txt"
                    # cla.txt
                    cla_data = str(cla) + "cla"
                    file_path2 = dir_path + "\\" + cla_data + ".txt"
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        data = 'no'
                        file.write(str(data))
                        time.sleep(0.2)
                    with open(file_path2, "w", encoding='utf-8-sig') as file:
                        data = cla
                        file.write(str(data))
                        time.sleep(0.2)
                    os.execl(sys.executable, sys.executable, *sys.argv)

                else:
                    print("정상 작동 중", result_cal)

    except Exception as e:
        print(e)
        return 0









