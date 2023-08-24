import sys
import time

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def jadong_start(cla, where):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, drag_pos, click_pos_2
    from potion_ares import juljun_potion_check
    from action_ares import dead_die, out_check, clean_screen
    from dungeon import dark_play
    try:
        print("jadong_start", v_.dark_demen_count)

        jadong_ready = False

        # 아레스에서는 윈도우창에 보이는 v_.onCollection 콜렉션을 다크디멘션으로 대체함
        if v_.onCollection == True:
            if v_.dark_demen_count > 1:
                jadong_ready = True
        else:
            jadong_ready = True

        if jadong_ready == True:
            print("자동사냥 모드")
            dead_die(cla, where)
            result_attck = juljun_attack_check(cla, where)
            if result_attck == False:
                go_spot_in(cla, where)
            else:
                juljun_potion_check(cla)
        else:
            print("다크디멘젼 모드")


            time.sleep(1)

            result_attck = juljun_attack_check(cla, where)
            if result_attck == False:
                go_spot_in(cla, where)
            else:

                for i in range(5):
                    result_out = out_check(cla)
                    if result_out == True:
                        break
                    else:
                        clean_screen(cla)
                    time.sleep(1)

                dark_mode = True
                while dark_mode is True:
                    print("다크디멘젼 모드 중...", v_.dark_demen_count)

                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\gigantomakia_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        dark_mode = False

                        for i in range(5):
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\gigantomakia_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(940, 50, cla)
                            else:
                                break
                            time.sleep(0.5)

                    else:

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_on.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("다크디멘젼 모드 : auto_on", imgs_)

                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\auto_off.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(570, 980, 615, 1030, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("auto_off", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                        result_dead = dead_die(cla, where)
                        if result_dead == True:
                            dark_mode = False
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                result_attck = juljun_attack_check(cla, where)
                                if result_attck == False:
                                    go_spot_in(cla, where)
                                else:
                                    drag_pos(405, 605, 945, 605, cla)


                        if v_.dark_demen_count > 1:
                            dark_mode = False
                        else:
                            result_dark = dark_play(cla)
                            print("다크디멘젼 체크 중...", result_dark)
                            if result_dark == True:
                                go_spot_in(cla, where)

                        time.sleep(60)
                    time.sleep(10)

    except Exception as e:
        print(e)
        return 0


def go_hangsun_map(cla, where):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import out_check, clean_screen
    try:
        print("go_hangsun_map")

        where_split = where.split("/")

        for i in range(3):
            result_out = out_check(cla)
            if result_out == True:
                break
            else:
                clean_screen(cla)
            time.sleep(0.5)

        hangsung_in = False
        hangsung_in_count = 0
        while hangsung_in is False:
            hangsung_in_count += 1
            if hangsung_in_count > 7:
                hangsung_in = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\hangsung_map_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:

                hangsung_in = True
                print("지정한 장소 찾아가자")
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\map_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    if where_split[1] == "edan":
                        spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\edan_map_title.PNG"
                    elif where_split[1] == "elia":
                        spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\elia_map_title.PNG"
                    elif where_split[1] == "loona":
                        spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loona_map_title.PNG"
                    elif where_split[1] == "jalis":
                        spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jalis_map_title.PNG"
                    full_path = spot_pic
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 200, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        hangsung_in = True

                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\hangsung_map.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 980, 100, 1060, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            for i in range(10):
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\hangsung_map_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.5)



                else:
                    # 지도 클릭
                    click_pos_2(25, 50, cla)
                    time.sleep(0.5)
                    click_pos_2(65, 115, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\map_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
                    time.sleep(0.2)
                time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0

def go_spot_in(cla, where):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_2
    try:
        print("go_spot_in")

        where_split = where.split("/")

        spot_in = False
        spot_in_count = 0
        while spot_in is False:
            spot_in_count += 1
            if spot_in_count > 7:
                spot_in = True

            # 에단평원인지, 엘리아인지...행성 이름 파악후 그 행성을 클릭
            if where_split[1] == "edan":
                spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\edan_map_title.PNG"
            elif where_split[1] == "elia":
                spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\elia_map_title.PNG"
            elif where_split[1] == "loona":
                spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loona_map_title.PNG"
            elif where_split[1] == "jalis":
                spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jalis_map_title.PNG"
            full_path = spot_pic
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 200, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                for i in range(20):
                    full_path = spot_pic
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 200, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        spot_in = True
                        go_spot_click(cla, where)
                        break
                    time.sleep(1)
            else:
                go_hangsun_map(cla, where)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\hangsung_map_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:

                    # 에단평원인지, 엘리아인지...행성 이름 파악후 그 행성을 클릭
                    if where_split[1] == "edan":
                        print("edan")
                        # 에단 위치 클릭하기
                        click_pos_2(420, 470, cla)
                        spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\edan_map_title.PNG"
                    elif where_split[1] == "elia":
                        print("elia")
                        # 엘리아 위치 클릭하기
                        click_pos_2(95, 775, cla)
                        spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\elia_map_title.PNG"
                    elif where_split[1] == "loona":
                        print("loona")
                        # 루나 위치 클릭하기
                        click_pos_2(55, 690, cla)
                        spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loona_map_title.PNG"
                    elif where_split[1] == "jalis":
                        print("jalis")
                        # 자리스 위치 클릭하기
                        click_pos_2(10, 320, cla)
                        spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jalis_map_title.PNG"
                    for i in range(20):
                        full_path = spot_pic
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 200, 100, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(1)
                time.sleep(1)

            # where_split[0] => 몬스터레벨 등 = > "_"로 분류
            # map_data = where_split[0].split("_")
            # map_data[0] => 몬스터레벨
            # map_data[1] => 슈트승급 아이템
            # map_data[2] => 채집 아이템
            # map_data[3] => 미네랄
            # map_data[4] => pk, treasure
            # ============================================
            # where_split[1] => 좌표 => "," 로 분류 x1, y1, x2, y2
            # where_split[2] => 사냥터 이름
            # where_split[3] => 행성 이름
    except Exception as e:
        print(e)
        return 0


def go_spot_click(cla, where):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action_ares import maul_go
    import os
    try:
        print("go_spot_click")

        where_split = where.split("/")

        # 사냥터
        dir_path = "C:\\my_games\\ares\\data_ares"
        if where_split[1] == "edan":
            file_path = dir_path + "\\jadong\\ares_edan.txt"
        if where_split[1] == "elia":
            file_path = dir_path + "\\jadong\\ares_elia.txt"
        if where_split[1] == "loona":
            file_path = dir_path + "\\jadong\\ares_loona.txt"
        if where_split[1] == "jalis":
            file_path = dir_path + "\\jadong\\ares_jalis.txt"

        result_data = "none"
        if os.path.isfile(file_path) == True:
            with open(file_path, "r", encoding='utf-8-sig') as file:
                read_data = file.read().splitlines()
                for i in range(len(read_data)):
                    read_ready = read_data[i].split("/")
                    if read_ready[2] == where_split[2]:
                        result_data = read_data[i].split("/")

        # 에단평원인지, 엘리아인지...행성 이름 파악후 그 행성을 클릭
        # where_split[0] => 몬스터레벨 등 = > "_"로 분류
        # map_data = where_split[0].split("_")
        # map_data[0] => 몬스터레벨
        # map_data[1] => 슈트승급 아이템
        # map_data[2] => 채집 아이템
        # map_data[3] => 미네랄
        # map_data[4] => pk, treasure
        # ============================================
        # where_split[1] => 좌표 => "," 로 분류 x1, y1, x2, y2
        # where_split[2] => 사냥터 이름
        # where_split[3] => 행성 이름
        pic_data_ready = result_data[0].split("_")
        pic_data = pic_data_ready[4]
        map_data = result_data[1].split(",")

        spot_in = False
        spot_in_count = 0
        while spot_in is False:
            spot_in_count += 1
            if spot_in_count > 3:
                print("일딴 마을 가서 정비하고 오자")
                spot_in = True
                maul_go(cla)
            if where_split[1] == "edan":
                print("edan")
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\edan_map_title.PNG"
            elif where_split[1] == "elia":
                print("elia")
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\elia_map_title.PNG"
            elif where_split[1] == "loona":
                print("loona")
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loona_map_title.PNG"
            elif where_split[1] == "jalis":
                print("jalis")
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jalis_map_title.PNG"

            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 200, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                drag_pos(200, 200, 800, 800, cla)
                time.sleep(0.5)
                for i in range(5):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_move.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1060, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        spot_in = True
                        jadong_arrive(cla, where)
                        break
                    else:

                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(int(map_data[0]), int(map_data[1]), int(map_data[2]), int(map_data[3]), cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(int(map_data[0]), int(map_data[1]), int(map_data[2]), int(map_data[3]), cla,
                                              img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_point_3.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(int(map_data[0]), int(map_data[1]), int(map_data[2]),
                                                  int(map_data[3]), cla,
                                                  img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    print("사냥터가 무언가에 가려져이싸.")
                                    spot_moglog(cla, where)
                    time.sleep(1)

            time.sleep(1)

            # where_split[0] => 몬스터레벨 등 = > "_"로 분류
            # map_data = where_split[0].split("_")
            # map_data[0] => 몬스터레벨
            # map_data[1] => 슈트승급 아이템
            # map_data[2] => 채집 아이템
            # map_data[3] => 미네랄
            # map_data[4] => pk, treasure
            # ============================================
            # where_split[1] => 좌표 => "," 로 분류 x1, y1, x2, y2
            # where_split[2] => 사냥터 이름
            # where_split[3] => 행성 이름
    except Exception as e:
        print(e)
        return 0

def jadong_arrive(cla, where):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import clean_screen, dead_die
    try:
        print("jadong_arrive")

        isloading = False
        moving_ = False

        walking = False
        walking_count = 0

        for i in range(50):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("loding")
                isloading = True
                break

            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_moving.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(815, 935, 915, 1030, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    moving_ = True
                    break
                else:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\title\\map_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 570, 610, 610, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\attack_ready.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(815, 935, 915, 1030, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            walking_count += 1
                            print("loading before walking_count", walking_count)
                            if walking_count > 20:
                                walking = True
                                break
            time.sleep(0.5)

        dead_die(cla, where)

        if isloading == False and moving_ == False:
            # 가까운곳 이동했을 경우...
            # 공격하기

            auto_on_click(cla)

            # click_pos_2(595, 1010, cla)
            time.sleep(1)
            # 절전모드
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            if isloading == True:

                isloading = True
                loading_count = 0
                while isloading is True:
                    loading_count += 1
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loding.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 400, 700, 700, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("loding", loading_count)
                    else:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_moving.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(815, 935, 915, 1030, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("사냥터이동중")
                            moving_ = True
                            isloading = False
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\attack_ready.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(815, 935, 915, 1030, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                walking_count += 1
                                print("loading after walking_count", walking_count)
                                if walking_count > 20:
                                    walking = True
                                    isloading = False
                    time.sleep(1)

            if moving_ == True:
                moving_count = 0
                while moving_ is True:
                    moving_count += 1
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_moving.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(815, 935, 915, 1030, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("사냥터이동중", moving_count)
                    else:

                        where_split = where.split("/")
                        where_in_data = where_split[3].split("_")

                        if where_in_data[4] == ("pk1" or "pk2"):
                            time.sleep(20)

                        moving_ = False
                        # 공격하기
                        auto_on_click(cla)
                        # click_pos_2(595, 1010, cla)
                        time.sleep(1)
                        # 절전모드
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
        if walking == True:
            # 공격하기
            auto_on_click(cla)
            time.sleep(1)
            # 절전모드
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

        time.sleep(5)
        result_attack = juljun_attack_check(cla, where)
        if result_attack == False:
            clean_screen(cla)
            time.sleep(1)
            # 공격하기
            auto_on_click(cla)
            time.sleep(1)
            # 절전모드
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\juljun_mode_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 780, 50, 930, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        print(e)
        return 0


def auto_on_click(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg
    try:
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
    except Exception as e:
        print(e)
        return 0


def juljun_attack_check(cla, where):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    try:
        print("juljun_attack_check")
        go_ = False
        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 580, 560, 630, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_attack.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 400, 570, 470, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("자동사냥중")
                go_ = True
            else:
                for i in range(10):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\check\\juljun_attack.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 400, 570, 470, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("자동사냥중")
                        go_ = True
                        break
                    time.sleep(1)
        return go_
    except Exception as e:
        print(e)
        return 0


def spot_moglog(cla, where):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    try:
        print("spot_moglog")
        # 사냥/elia/버려진땅/30_no_no_no_pk1

        where_split = where.split("/")

        # 사냥터
        dir_path = "C:\\my_games\\ares\\data_ares"
        if where_split[1] == "edan":
            file_path = dir_path + "\\jadong\\ares_edan_moglog.txt"
        if where_split[1] == "elia":
            file_path = dir_path + "\\jadong\\ares_elia_moglog.txt"
        if where_split[1] == "loona":
            file_path = dir_path + "\\jadong\\ares_loona_moglog.txt"
        if where_split[1] == "jalis":
            file_path = dir_path + "\\jadong\\ares_jalis_moglog.txt"

        with open(file_path, "r", encoding='utf-8-sig') as file:
            read_data = file.read().splitlines()
            for i in range(len(read_data)):
                read_ready = read_data[i].split("/")
                if read_ready[0] == where_split[2]:
                    x_reg = 110
                    y_reg = int(read_ready[1])
                    break
        for k in range(10):
            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\moglog_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(95, 90, 170, 130, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(x_reg, y_reg, cla)
                for z in range(3):
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\jadong_move.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1060, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(1)
                break
            else:
                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\moglog_title_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 70, 60, 260, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)


    except Exception as e:
        print(e)
        return 0