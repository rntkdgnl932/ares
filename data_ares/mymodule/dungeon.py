import sys

sys.path.append('C:/my_games/ares/data_ares/mymodule')

import variable as v_



def dungeon_start(cla, dungeon):
    try:
        print("dungeon_start")
    except Exception as e:
        print(e)
        return  0


def dungeon_in(cla, dungeon):
    from action_ares import menu_open
    try:
        print("dungeon_in")
        # 침식의시즌

        # 도전
        # 도전 : 행성파견, 성운돌파
        # 행성파견(4단계) : 군단장헥스, 갤리온기지전투, 군단장아키투스, 거신아페칸, 고대사원전투, 협곡전투
        # 성운돌파 : (?)

        # 협동
        # 협동 : 다크디멘젼, 레이드, 기간토마키아
        # 다크디멘젼 : 마수바즈라(에단), 오닉스침공저지, 마수바즈라(루나), 임펄서보호, 마수바즈라(?), 오닉스침공저지, 마수바즈라(?)
        # 레이드(3단계) : 크사이엘둥지, 레기온침공전, 아바돈연구소
        # 기간토마키아 : 카시아스, (?)

        # 경쟁
        # 경쟁 : 데이모스전장, 모리아기지, coming soon
        # 데이모스전장 : (?)
        # 모리아기지(4단계) : 죄악의요새(1), 몰락의격납고, 파괻된용광로,영광의유산(4)
    except Exception as e:
        print(e)
        return  0

