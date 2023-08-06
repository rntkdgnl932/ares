import time
# import os
import sys

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def chaejib_start(cla):
    from function import click_pos_2
    from schedule import myQuest_play_add
    try:

        print("chaejib_start")
        result_maps = chaejib_maps()
        # 30_no_no_no_pk1/270,830,330,890/버려진땅/elia
        # 아래로 변환하기
        # 사냥/elia/버려진땅/30_no_no_no_pk1

        # print("result_maps[0]", result_maps[0])
        # where_ready = result_maps[0].split("/")
        # where = "사냥/" + str(where_ready[3]) + "/" + str(where_ready[2]) + "/" + str(where_ready[0])
        #
        # print("where", where)
        chaejib_setting(cla)
        for i in range(len(result_maps)):
            print(i + 1, "번째 맵 채집 시작!!!")
            where_ready = result_maps[i].split("/")
            where = "사냥/" + str(where_ready[3]) + "/" + str(where_ready[2]) + "/" + str(where_ready[0])
            result_quest = go_spot_in(cla, where)
            if result_quest == False:
                break
        time.sleep(1)
        # add
        myQuest_play_add(cla, "채집")
        click_pos_2(945, 100, cla)



    except Exception as e:
        print(e)
        return 0

def chaejib_maps():
    try:

        print("chaejib_maps")

        dir_path = "C:\\my_games\\ares\\data_ares"
        file_path1 = dir_path + "\\jadong\\ares_edan.txt"
        file_path2 = dir_path + "\\jadong\\ares_elia.txt"
        file_path3 = dir_path + "\\jadong\\ares_loona.txt"

        result_chaejib_maps = []

        with open(file_path1, "r", encoding='utf-8-sig') as file:
            read_data = file.read().splitlines()
            for i in range(len(read_data)):
                read_ready1 = read_data[i].split("/")[0].split("_")[2]
                read_ready2 = read_data[i].split("/")[0].split("_")[3]
                if read_ready1 != "no" or read_ready2 !="no":
                    result_chaejib_maps.append(read_data[i])
        with open(file_path2, "r", encoding='utf-8-sig') as file:
            read_data = file.read().splitlines()
            for i in range(len(read_data)):
                read_ready1 = read_data[i].split("/")[0].split("_")[2]
                read_ready2 = read_data[i].split("/")[0].split("_")[3]
                if read_ready1 != "no" or read_ready2 !="no":
                    result_chaejib_maps.append(read_data[i])
        with open(file_path3, "r", encoding='utf-8-sig') as file:
            read_data = file.read().splitlines()
            for i in range(len(read_data)):
                read_ready1 = read_data[i].split("/")[0].split("_")[2]
                read_ready2 = read_data[i].split("/")[0].split("_")[3]
                if read_ready1 != "no" or read_ready2 !="no":
                    result_chaejib_maps.append(read_data[i])
        print("result_chaejib_maps", result_chaejib_maps)


        return result_chaejib_maps
    except Exception as e:
        print(e)
        return 0

def chaejib_setting(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2, mouse_move_cpp
    from action_ares import out_check, clean_screen
    try:
        print("chaejib_setting")
        # 사냥/elia/버려진땅/30_no_no_no_pk1

        # where_split = where.split("/")

        for i in range(5):
            result_out = out_check(cla)
            if result_out == True:
                break
            else:
                clean_screen(cla)
            time.sleep(1)

        chaejib_ready = False
        chaejib_ready_count = 0
        while chaejib_ready is False:
            chaejib_ready_count += 1
            if chaejib_ready_count > 7:
                chaejib_ready = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\scan_setting.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(440, 390, 510, 430, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\3_5.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 420, 645, 465, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("3_5", imgs_)
                    click_pos_2(600, 445, cla)
                else:
                    print("not 3_5")
                    click_pos_2(530, 445, cla)

                time.sleep(0.5)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\monster_off.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(550, 455, 720, 495, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("monster_off", imgs_)
                else:
                    print("not monster_off")
                    click_pos_2(600, 475, cla)

                time.sleep(0.5)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\user_off.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(550, 520, 720, 570, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("user_off", imgs_)
                else:
                    print("not user_off")
                    click_pos_2(600, 545, cla)

                time.sleep(0.5)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\npc_off.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(550, 595, 720, 640, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("npc_off", imgs_)
                else:
                    print("not npc_off")
                    click_pos_2(600, 615, cla)

                time.sleep(0.5)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\chaejib_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(555, 625, 720, 670, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("chaejib_on", imgs_)
                else:
                    print("not chaejib_on")
                    click_pos_2(670, 645, cla)

                    time.sleep(0.2)

                    mouse_move_cpp(475, 735, cla)

                time.sleep(0.5)

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\monster_off.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(550, 455, 720, 495, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\user_off.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(550, 520, 720, 570, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\npc_off.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(550, 595, 720, 640, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\chaejib_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(555, 625, 720, 670, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("채집셋팅 완료")
                                click_pos_2(475, 735, cla)
                                chaejib_ready = True
            else:

                click_pos_2(945, 145, cla)
                time.sleep(0.5)
                click_pos_2(780, 90, cla)
            time.sleep(1)



    except Exception as e:
        print(e)
        return 0

def chaejib_go(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2, mouse_move_cpp
    try:
        print("chaejib_go")
        # 사냥/elia/버려진땅/30_no_no_no_pk1

        # where_split = where.split("/")

        click_pos_2(945, 145, cla)

        chaejib_ready = False
        chaejib_ready_count = 0
        while chaejib_ready is False:
            chaejib_ready_count += 1
            if chaejib_ready_count > 10:
                chaejib_ready = True

            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\search_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(890, 70, 930, 110, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\bomool_box.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(785, 80, 940, 110, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\search_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(890, 105, 930, 135, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(850, 120, cla)
                        time.sleep(0.3)
                    else:
                        chaejib_ready = True
                else:
                    click_pos_2(850, 95, cla)

                    time.sleep(0.3)

                mouse_move_cpp(545, 445, cla)

                for i in range(160):
                    if i % 20 == 0:
                        se_ = i / 10
                        data = "채집하는 중 : " + str(se_) + "초"
                        print(data)
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\chaejib_ing_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(555, 500, 610, 560, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("채집중 1")
                        break
                    full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\chaejib_ing_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(555, 500, 610, 560, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("채집중 2")
                        break
                    time.sleep(0.1)
                time.sleep(3.5)

            else:
                chaejib_ready = True




    except Exception as e:
        print(e)
        return 0


def go_hangsun_map(cla, where):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_ares import out_check, clean_screen
    try:
        print("chaejib : go_hangsun_map")

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
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    if where_split[1] == "edan":
                        spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\edan_map_title.PNG"
                    elif where_split[1] == "elia":
                        spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\elia_map_title.PNG"
                    elif where_split[1] == "loona":
                        spot_pic = "c:\\my_games\\ares\\data_ares\\imgs\\jadong\\loona_map_title.PNG"
                    full_path = spot_pic
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 200, 100, cla, img, 0.7)
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
                                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
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
                        imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
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
        print("chaejib : go_spot_in")

        where_split = where.split("/")

        quest_complete = True

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
            full_path = spot_pic
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 200, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                for i in range(20):
                    full_path = spot_pic
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 200, 100, cla, img, 0.7)
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
                imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
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
                    for i in range(20):
                        full_path = spot_pic
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 200, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\ares\\data_ares\\imgs\\chaejib\\not_complete_quest.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(365, 80, 635, 160, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("퀘스트 미완료")
                                spot_in = True
                                quest_complete = False
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
        return quest_complete
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
        print("chaejib : go_spot_click")

        where_split = where.split("/")

        # 사냥터
        dir_path = "C:\\my_games\\ares\\data_ares"
        if where_split[1] == "edan":
            file_path = dir_path + "\\jadong\\ares_edan.txt"
        if where_split[1] == "elia":
            file_path = dir_path + "\\jadong\\ares_elia.txt"
        if where_split[1] == "loona":
            file_path = dir_path + "\\jadong\\ares_loona.txt"

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

            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 200, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                drag_pos(200, 200, 800, 800, cla)
                time.sleep(0.5)
                for i in range(3):
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
    from action_ares import clean_screen
    try:
        print("chaejib : jadong_arrive")

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
                    imgs_ = imgs_set_(10, 10, 120, 100, cla, img, 0.7)
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

        if isloading == False and moving_ == False:
            # 가까운곳 이동했을 경우...
            print("가까운곳 이동했을 경우... : 채집하기")
            chaejib_go(cla)
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
                        print("moving_ == True : 채집하기")
                        chaejib_go(cla)
                    time.sleep(1)
        if walking == True:
            print("walking : 채집하기")
            chaejib_go(cla)

    except Exception as e:
        print(e)
        return 0


def spot_moglog(cla, where):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    try:
        print("chaejib : spot_moglog")
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