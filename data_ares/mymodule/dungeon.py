import sys
import time

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def dungeon_start(cla, dungeon):
    try:
        print("dungeon_start")
    except Exception as e:
        print(e)
        return  0


def dungeon_in_title(cla, dungeon):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg
    from action_ares import menu_open
    try:
        print("dungeon_in")

        # 행성파견_1_1, 성운돌파_1_1, 레이드_1_1, 모리아기지_1

        where_dungeon = dungeon.split("_")

        menu_open(cla)

        if where_dungeon[0] == "행성파견" or where_dungeon[0] == "성운돌파":
            click_pos_2(70, 230, cla)
            title = "dojun_title"
        elif where_dungeon[0] == "레이드":
            click_pos_2(70, 280, cla)
            title = "hyubdong_title"
        elif where_dungeon[0] == "모리아기지":
            click_pos_2(70, 330, cla)
            title = "gyungjang_title"

        for i in range(10):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\" + str(title) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                break
            time.sleep(1)



    except Exception as e:
        print(e)
        return 0

def dungeon_in_hangsungpagyun(cla, dungeon):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg
    from action_ares import menu_open, loading_ares
    from schedule import myQuest_play_add
    try:
        print("dungeon_in_hangsungpagyun")

        # 행성파견_1_1, 성운돌파_1_1, 레이드_1_1, 모리아기지_1

        where_dungeon = dungeon.split("_")

        dun_go_ = False
        dun_go_count = 0
        while dun_go_ is False:
            dun_go_count += 1
            if dun_go_count > 7:
                dun_go_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hangsungpagyun_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("행성파견")
                # 완료 여부 파악하기
                # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\hangsungpagyun_clear.PNG"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(72, 30, 770, 70, cla, img, 0.7)
                # if imgs_ is not None and imgs_ != False:
                #     print("이미 완료")
                #     myQuest_play_add(cla, dungeon)
                #     dun_go_ = True
                # else:
                # (100, 185/220/255/290/325/360...
                y_reg = 153 + (int(where_dungeon[1]) * 34)
                # (24/52/80/108, 1015)
                x_reg = (int(where_dungeon[2]) * 28) - 5

                # 자물쇠 있는지 파악
                # y_reg = 153 + (층 * 34)
                # 1 = 163, 187
                # 2 = 163, 221
                # 3 = 163, 255
                # 4 = 163, 289 -20 +20
                # 5 = 163, 323
                # 6 = 163, 358
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\small_lock.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(140, y_reg - 20, 220, y_reg + 20, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print(int(where_dungeon[1]), imgs_)
                    # add 로 완료해버리기
                    myQuest_play_add(cla, dungeon)
                    dun_go_ = True

                else:
                    print("not mini_lock", int(where_dungeon[1]))
                    # 자물쇠 없으니 클릭
                    click_pos_2(100, y_reg, cla)

                    time.sleep(1)

                    # 다시 밑에 자물쇠 확인하기
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\mini_lock.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_reg - 20, 990, x_reg + 20, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("mini_lock", imgs_)
                    else:
                        print("no mini_lock", int(where_dungeon[2]))
                        click_pos_2(x_reg, 1010, cla)
                        time.sleep(0.5)

                        # 1. 입장 누르면 그냥 들어가지고 자동동으로 싸움
                        # click_pos_2(915, 1015, cla)
                        # 2. 반복시...
                        # click_pos_2(815, 1015, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\hangsungpagyun_plus.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(575, 485, 615, 525, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                for k in range(5):
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\hangsungpagyun_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                            else:
                                click_pos_2(815, 1015, cla)

                                time.sleep(1)

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\lack_ticket.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 90, 510, 140, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("던전 입장권 부족")
                                    myQuest_play_add(cla, dungeon)
                                    dun_go_ = True
                                    break
                                else:

                                    for z in range(10):
                                        # full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\dojun_confirm.PNG"
                                        # img_array = np.fromfile(full_path, np.uint8)
                                        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        # imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.7)
                                        # if imgs_ is not None and imgs_ != False:
                                        #     click_pos_reg(imgs_.x, imgs_.y, cla)
                                        #     time.sleep(0.5)

                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\hangsungpagyun_plus.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(575, 485, 615, 525, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        time.sleep(0.5)
                            time.sleep(0.5)
                        # 로딩화면 및 다시 타이틀 화면...
                        for i in range(20):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                loading_ares(cla)
                                break
                            time.sleep(1)

                        ing_ = True
                        ing_count = 0
                        while ing_ is True:
                            ing_count += 1
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hangsungpagyun_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                ing_ = False
                                dun_go_ = True
                                print("행성파견 끝")
                                myQuest_play_add(cla, dungeon)
                            else:
                                timing = ing_count * 5
                                print("행성파견 : " + str(timing) + "초 지남")
                            time.sleep(5)
                time.sleep(0.1)



            else:
                # 행성파견_1_1, 성운돌파_1_1, 레이드_1_1, 모리아기지_1

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\dojun_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\lock.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(260, 410, 470, 555, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("미오픈...완료로 변경")
                        # add...
                        myQuest_play_add(cla, dungeon)
                        dun_go_ = True
                    else:
                        click_pos_2(365, 500, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hangsungpagyun_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(1)
                else:
                    menu_open(cla)

                    click_pos_2(70, 230, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\dojun_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(1)
            time.sleep(1)

        # 밖으로 나가기
        for i in range(10):
            exit_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\dojun_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 50, cla)
                time.sleep(1)
                exit_ = False
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hangsungpagyun_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 50, cla)
                time.sleep(1)
                exit_ = False
            if exit_ == True:
                break
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0



def dungeon_in_sungwoondolpa(cla, dungeon):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg
    from action_ares import menu_open, loading_ares
    from schedule import myQuest_play_add
    try:
        print("dungeon_in_sungwoondolpa")

        # 성운돌파_7

        where_dungeon = dungeon.split("_")

        dun_go_ = False
        dun_go_count = 0
        while dun_go_ is False:
            dun_go_count += 1
            if dun_go_count > 7:
                dun_go_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\sungwoon_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("성운돌파")


                # 1. 순차진행
                # click_pos_2(915, 1015, cla)
                # 2. 도전
                # click_pos_2(815, 1015, cla)

                click_pos_2(815, 1015, cla)

                for i in range(20):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\dojun_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\sungwoondolpa_yes.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        loading_ares(cla)
                        break
                    time.sleep(0.5)



                # 로딩화면 및 다시 타이틀 화면...

                ing_ = True
                ing_count = 0
                while ing_ is True:
                    ing_count += 1
                    if ing_count > 120:
                        ing_ = True
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\sungwoon_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        ing_ = False
                        dun_go_ = True
                        print("성운돌파 끝")
                        myQuest_play_add(cla, dungeon)
                        time.sleep(0.3)
                    else:
                        timing = ing_count * 5
                        print("성운돌파 : " + str(timing) + "초 지남")

                        for k in range(10):

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\sungwoon_fail.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 280, 530, 330, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:

                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\sungwoon_exit.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 990, 630, 1030, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    print("성운돌파 실패")
                                    break
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\sungwoon_clear.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 200, 600, 400, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    ing_count = 0
                                    print("성운돌파 : 클리어 시간 0초로 재설정")
                            time.sleep(0.5)




                time.sleep(0.1)



            else:
                # 행성파견_1_1, 성운돌파_1_1, 레이드_1_1, 모리아기지_1

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\dojun_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\dojun\\lock.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 410, 710, 555, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("미오픈...완료로 변경")
                        # add...
                        myQuest_play_add(cla, dungeon)
                        dun_go_ = True
                    else:
                        click_pos_2(600, 500, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\sungwoon_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(1)
                else:
                    menu_open(cla)

                    click_pos_2(70, 230, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\dojun_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(1)
            time.sleep(1)

        # 밖으로 나가기
        for i in range(10):
            exit_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\dojun_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 50, cla)
                time.sleep(1)
                exit_ = False
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\sungwoon_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 50, cla)
                time.sleep(1)
                exit_ = False
            if exit_ == True:
                break
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0


def dungeon_in_raid(cla, dungeon):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg, mouse_move_cpp
    from action_ares import menu_open, loading_ares
    from schedule import myQuest_play_add
    try:
        print("dungeon_in_raid")

        # 행성파견_1_1, 성운돌파_1_1, 레이드_1_1, 모리아기지_1

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\ready_cancle.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 140, 220, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("레이드 대기중")

        else:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\jadong_in.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 140, 220, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("레이드 jadong_in")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\jadong_in_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 570, 610, 610, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    time.sleep(1)

            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\raid_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 140, 220, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("레이드 raid_ready")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    mouse_move_cpp(500, 500, cla)

                else:
                    where_dungeon = dungeon.split("_")

                    dun_go_ = False
                    dun_go_count = 0
                    while dun_go_ is False:
                        dun_go_count += 1
                        if dun_go_count > 7:
                            dun_go_ = True

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\raid_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("레이드")
                            # (100, 185/220/255/290/325/360...
                            y_reg = 769 + (int(where_dungeon[1]) * 59)
                            # (24/52/80/108, 1015)
                            x_reg = (int(where_dungeon[2]) * 28) - 5

                            # 자물쇠 있는지 파악
                            # # 2 = 97, 887
                            # # 3 = 97, 946
                            # 59 차이
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\raid_small_lock.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(65, y_reg - 30, 130, y_reg + 30, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("미오픈...완료로 변경")
                                print(int(where_dungeon[1]), imgs_)
                                # add 로 완료해버리기
                                myQuest_play_add(cla, dungeon)
                                dun_go_ = True

                            else:
                                print("not mini_lock", int(where_dungeon[1]))
                                # 자물쇠 없으니 클릭
                                click_pos_2(100, y_reg, cla)

                                time.sleep(1)

                                # 다시 밑에 자물쇠 확인하기
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\raid_mini_lock.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(x_reg - 20, 990, x_reg + 20, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("mini_lock", imgs_)
                                else:
                                    print("no mini_lock", int(where_dungeon[2]))
                                    click_pos_2(x_reg, 1010, cla)
                                    time.sleep(0.5)

                                    # 1. 파티생성
                                    # click_pos_2(915, 1015, cla)
                                    # 2. 자동입장...
                                    click_pos_2(815, 1015, cla)

                                    for i in range(20):
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\ready_cancle.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(0, 30, 140, 220, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            dun_go_ = True
                                            break
                                        else:
                                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\raid_title.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_2(940, 50, cla)
                                        time.sleep(1)


                            time.sleep(0.1)



                        else:
                            # 행성파견_1_1, 성운돌파_1_1, 레이드_1_1, 모리아기지_1

                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hyubdong_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\raid_big_lock.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 400, 580, 545, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("미오픈...완료로 변경")
                                    # add...
                                    myQuest_play_add(cla, dungeon)
                                    dun_go_ = True
                                else:
                                    click_pos_2(480, 500, cla)
                                    for i in range(10):
                                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\raid_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        time.sleep(1)
                            else:
                                menu_open(cla)

                                click_pos_2(70, 280, cla)

                                for i in range(10):
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\hyubdong_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    time.sleep(1)
                        time.sleep(1)

    except Exception as e:
        print(e)
        return 0

def moriagiji_start(cla, dungeon):
    from potion_ares import juljun_potion_check
    from jadong import juljun_attack_check
    from action_ares import map_in, clean_screen
    try:
        print("moriagiji_start")

        result_attck = juljun_attack_check_moriagiji(cla, dungeon)
        if result_attck == "none":
            print("처음부터 모리아 시작")
            dungeon_in_moriagiji(cla, dungeon)
        elif result_attck == "moria_ready":
            print("맵 이동 후 공격 하면 됨")
            moriagiji_move(cla)
            moriagiji_attack(cla)
        elif result_attck == "moria_arrive":
            print("공격 상태로 만들면 됨.")
            moriagiji_attack(cla)
        else:
            juljun_potion_check(cla)
    except Exception as e:
        print(e)
        return 0


def dungeon_in_moriagiji(cla, dungeon):
    import numpy as np
    import cv2
    from function import click_pos_2, imgs_set_, click_pos_reg
    from action_ares import menu_open, loading_ares, out_check, clean_screen
    from schedule import myQuest_play_add
    try:
        print("dungeon_in_moriagiji")

        # 행성파견_1_1, 성운돌파_1_1, 레이드_1_1, 모리아기지_1...

        where_dungeon = dungeon.split("_")

        dun_go_ = False
        dun_go_count = 0
        while dun_go_ is False:
            dun_go_count += 1
            if dun_go_count > 7:
                dun_go_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\moria_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:

                print("모리아기지")
                y_reg = 865 + (int(where_dungeon[1]) * 35)



                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\moria_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(100, y_reg, cla)
                        time.sleep(1)
                        click_pos_2(815, 1015, cla)
                        time.sleep(1)

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\already_moria.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(370, 80, 625, 150, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            dun_go_ = True
                            for z in range(3):
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\moria_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(940, 50, cla)
                                else:
                                    break
                                time.sleep(0.5)
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_lack_time.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(450, 80, 550, 140, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                dun_go_ = True
                                myQuest_play_add(cla, dungeon)
                                time.sleep(0.5)
                                for z in range(3):
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\moria_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(940, 50, cla)
                                    else:
                                        break
                                    time.sleep(0.5)
                                break

                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            loading_ares(cla)
                            break
                    time.sleep(0.5)
                if dun_go_ == False:
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_jadong_move.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 370, 900, 800, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(2)

                            for z in range(10):
                                result_out = out_check(cla)
                                if result_out == True:
                                    dun_go_ = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_jadong_move.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(470, 370, 900, 800, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_map_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\spot_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 370, 900, 800, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                result_out = out_check(cla)
                                if result_out == True:
                                    click_pos_2(25, 50, cla)
                                    time.sleep(0.5)
                                    click_pos_2(65, 115, cla)
                                    time.sleep(0.5)
                                else:
                                    clean_screen(cla)
                        time.sleep(1)

                    if dun_go_ == True:

                        time.sleep(10)

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_on.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("auto_on", imgs_)
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_off.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("auto_off", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                        # 절전모드
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    for i in range(10):
                        result_out = out_check(cla)
                        if result_out == True:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("auto_on", imgs_)
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_off.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("auto_off", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)
                            # 절전모드
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        time.sleep(1)
            else:
                # 행성파견_1_1, 성운돌파_1_1, 레이드_1_1, 모리아기지_1

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\contest_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\gyungjang_big_lock.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 400, 580, 545, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("미오픈...완료로 변경")
                        # add...
                        myQuest_play_add(cla, dungeon)
                        dun_go_ = True
                    else:
                        click_pos_2(480, 500, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\moria_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(1)
                else:
                    menu_open(cla)

                    click_pos_2(70, 330, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\gyungjang_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(1)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0

def moriagiji_move(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import clean_screen, out_check
    try:
        print("moria move")
        map_move_ = False
        map_move_count = 0
        while map_move_ is False:
            map_move_count += 1
            if map_move_count > 5:
                map_move_ = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_jadong_move.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(470, 370, 900, 800, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(2)

                for z in range(10):
                    result_out = out_check(cla)
                    if result_out == True:
                        map_move_ = True
                        break
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_jadong_move.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 370, 900, 800, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
            else:

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_map_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\spot_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 370, 900, 800, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    result_out = out_check(cla)
                    if result_out == True:
                        click_pos_2(25, 50, cla)
                        time.sleep(0.5)
                        click_pos_2(65, 115, cla)
                        time.sleep(0.5)
                    else:
                        clean_screen(cla)
            time.sleep(1)
    except Exception as e:
        print(e)
        return 0


def moriagiji_attack(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action_ares import clean_screen, out_check
    try:
        print("moria moriagiji_attack")

        for i in range(3):
            result_out = out_check(cla)
            if result_out == True:
                break
            else:
                clean_screen(cla)
            time.sleep(0.5)

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            drag_pos(405, 605, 945, 605, cla)
        else:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_off.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("auto_off", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)



            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

                for z in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

def juljun_attack_check_moriagiji(cla, where):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import clean_screen, out_check
    try:
        print("juljun_attack_check_moriagiji")
        go_ = "none"

        check_ready = False
        check_ready_count = 0
        while check_ready is False:
            check_ready_count += 1
            if check_ready_count > 5:
                check_ready = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                check_ready = True
                # 먼저 모리아기지인지 파악
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_juljun_map_title_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 50, 90, 90, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    # 이건 이동 못한 상태
                    print("모리아 기지에서 이동 못한 상태")
                    go_ = "moria_ready"
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\gyungjang\\moria_juljun_map_title_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 50, 90, 90, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        # 이건 이동 못한 상태
                        print("모리아 기지인 상태")
                        go_ = "moria_arrive"
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_attack.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 400, 570, 470, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("자동사냥중")
                            go_ = "moria_attack"
                        else:
                            for i in range(10):
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_attack.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 400, 570, 470, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("자동사냥중")
                                    go_ = "moria_attack"
                                    break
                                time.sleep(1)
                    else:
                        print("완전 다른 곳인 상태")

            else:
                print("절전모드 아니다?")
                for i in range(10):
                    result_out = out_check(cla)
                    if result_out == True:


                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            for z in range(10):
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.5)
                        break
                    else:
                        clean_screen(cla)
                    time.sleep(1)

        print("juljun_attack_check_moriagiji", go_)

        return go_
    except Exception as e:
        print(e)
        return 0


def dark_play(cla):
    import numpy as np
    import cv2
    from action_ares import map_in, clean_screen
    from function import click_pos_reg, imgs_set_
    try:
        print("dark_play")

        v_.dark_demen = False

        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\dark_demen.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(770, 90, 950, 180, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("dark_demen", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            v_.dark_demen = True
        else:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\dark_demen_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 90, 950, 180, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("dark_demen_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                v_.dark_demen = True
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\dark_demen_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(770, 90, 950, 180, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("dark_demen_3", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    v_.dark_demen = True
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\dark_demen_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(770, 90, 950, 180, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("dark_demen_4", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        v_.dark_demen = True
        if v_.dark_demen == True:

            dark_ = False
            dark_count = 0
            while dark_ is False:
                dark_count += 1
                if dark_count > 300:
                    dark_ = True
                    v_.dark_demen = False
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\dark_demen_arrived.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(440, 340, 740, 740, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    if dark_count % 20 == 0:
                        print("dark_demen_arrived", imgs_)
                        dark_count = 0
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\dark_clear.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(430, 290, 540, 340, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("dark_clear", imgs_)
                        dark_ = True
                time.sleep(1)
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\dungeon\\hyubdong\\dark_exit.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 1000, 800, 1040, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                v_.dark_demen = False
        return v_.dark_demen
    except Exception as e:
        print(e)
        return 0

