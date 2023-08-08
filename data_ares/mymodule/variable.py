# 현재실행중인 클라우드
now_cla = 'none'

# 현재실행중인 퀘스트(챕터)
now_chabter = 'none'

# 아두이노 관련
now_arduino = "none"

# 아레스 관련
# 협동 던전 : 다크디멘젼
dark_demen = False
# 지역퀘스트 : 전설속 몬스터 페네트라
# penetra = False
# gorgon = False
region_click = 0
# 가디언 임무 관련
gardiun_juljun_count = 0


# 버젼

dir_path = "C:\\my_games\\ares\\data_ares"
file_path = dir_path + "\\mymodule\\version.txt"
file_path2 = "C:\\my_games\\mouse\\port.txt"

with open(file_path, "r", encoding='utf-8-sig') as file:
    version_ = file.read()
    print("version???", version_)

with open(file_path2, "r", encoding='utf-8-sig') as file:
    read_port = file.read().splitlines()
    COM_ = read_port[0]
    speed_ = int(read_port[1])
    print("COM???", COM_)
    print("speed_???", speed_)

this_game = "아레스"


# 강제로 돈벌기
forcee_not_sub = False
force_sub_quest = False
onForceGold = 5000000
onForceGoldSpot = "none"
onCollection = False


# 마우스 관련
mouse_speed = 20
mouse_pm = 3