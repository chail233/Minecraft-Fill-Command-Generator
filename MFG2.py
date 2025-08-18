import json
class Config():
    def __init__(self):
        self.preset = {}
        self.axis_lock = {"x":{"lock":False,"value":None},"y":{"lock":False,"value":None},"z":{"lock":False,"value":None}}
    def init(self):
        self.preset = {}
        self.axis_lock = {"x": {"lock": False, "value": None}, "y": {"lock": False, "value": None},
                          "z": {"lock": False, "value": None}}
    def write(self):
        config_name = input("配置文件名:")
        config_dict = {"preset":self.preset, "axis_lock":self.axis_lock}
        with open(f"{config_name}.json", "w") as file:
            json.dump(config_dict, file, indent=4)
    def read(self):
        config_name = input("配置文件名:")
        with open(f"{config_name}.json", "r") as file:
            dict = json.load(file)
            self.preset = dict["preset"]
            self.axis_lock = dict["axis_lock"]

config = Config()
class Fill():
    def __init__(self):
        self.start = {"x":None,"y":None,"z":None}
        self.end = {"x":None,"y":None,"z":None}
    def result(self):
        print(f"/fill {self.start['x']} {self.start['y']} {self.start['z']} {self.end['x']} {self.end['y']} {self.end['z']} {block_id}")
    def coordinate_get(self):
        for i in ("x","y","z"):
            if config.axis_lock[i]["lock"]:
                self.start[i] = config.axis_lock[i]["value"]
                self.end[i] = config.axis_lock[i]["value"]
            else:
                self.start[i] = start_coordinate.pop(0)
                self.end[i] = end_coordinate.pop(0)
def menu_1():
    print('1.增加填充方块预设')
    print("2.删除填充方块预设")
    print("3.查看填充方块预设")
    choice = choice_fun()
    if choice == "1":
        name = input("方块名(可随意设置方便使用,不能以“lock”作为方块名，会出bug！)")
        id = input("方块id(不可随意设置，必须使用游戏中有效的id)")
        config.preset[name] = id
        print(f"添加完成！{name}:{id}")
    elif choice == "2":
        name = input("需要删除的方块名")
        if name not in config.preset:
            print("该方块名不在预设中！")
        else:
            del config.preset[name]
            print(f"删除成功！{name}")
    elif choice == "3":
        print(config.preset)
    else:
        print("无效选择！")

def menu_2():
    print("1.通过id锁定")
    print("2.通过预设方块名锁定")
    choice = choice_fun()
    if choice == "1":
        id = input("请输入物品id:")
        config.preset["__lock__"] = id
        print("锁定完毕！")
    elif choice == "2":
        name = input("请输入预设的方块名:")
        if name not in config.preset:
            print("该方块名不存在！")
        else:
            config.preset["__lock__"] = config.preset[name]
    else:
        print("无效选择！")

def menu_3():
    if config.preset["__lock__"] is not None:
        del config.preset["__lock__"]
        print("已解除锁定！")
    else:
        print("当前填充方块没有锁定！")

def menu_4():
    axis = input("请输入要锁定的轴(x/y/z)(锁定后的轴请不要输入坐标，以免出现错误)")
    if axis == "x" or axis == "y" or axis == "z":
        config.axis_lock[axis]["lock"] = True
        config.axis_lock[axis]["value"] = input("坐标值")
        print(f"{axis}轴已锁定坐标{config.axis_lock[axis]['value']}")
    else:
        print("无效的坐标轴")

def menu_5():
    axis = input("请输入需要解除锁定的轴(x/y/z)")
    if config.axis_lock[axis]["lock"]:
        config.axis_lock[axis]["lock"] = False
        print(f"{axis}轴已解除锁定！")
    else:
        print(f"错误，{axis}轴没有被锁定！")

def menu_6():
    config.write()
    print("保存完成！")

def menu_7():
    config.read()

def menu_8():
    config.init()

menu_dict = {"1":menu_1,"2":menu_2,"3":menu_3,"4":menu_4,"5":menu_5,"6":menu_6,"7":menu_7,"8":menu_8}

def choice_fun():
    c = input("请选择:")
    return c
def menu():
    global choice_fun
    print("1.管理方块预设")
    print("2.锁定填充方块")
    print("3.解除填充方块锁定")
    print("4.锁定坐标轴")
    print("5.解除坐标轴锁定")
    print("6.保存配置文件")
    print("7.加载配置文件")
    print("8.创建新配置")
    choice = choice_fun()
    if choice == "1":
        menu_dict["1"]()
    elif choice == "2":
        menu_dict["2"]()
    elif choice == "3":
        menu_dict["3"]()
    elif choice == "4":
        menu_dict["4"]()
    elif choice == "5":
        menu_dict["5"]()
    elif choice == "6":
        menu_dict["6"]()
    elif choice == "7":
        menu_dict["7"]()
    elif choice == "8":
        menu_dict["8"]()

while True:
    start_coordinate = input("起始坐标(直接按回车可进入菜单)")
    if start_coordinate == "":
        menu()
    else:
        end_coordinate = input("终点坐标").split()
        start_coordinate = start_coordinate.split()
        num = 3
        for i in ("x","y","z"):
            if config.axis_lock[i]["lock"]:
                num -= 1
        if len(start_coordinate) != num:
            print(f"起始坐标数错误，应为{num},而输入了{len(start_coordinate)}个")
            continue
        if len(end_coordinate) != num:
            print(f"终点坐标数错误,应为{num},而输入了{len(end_coordinate)}个")
            continue
        if "__lock__" in config.preset:
            block_id = config.preset["__lock__"]
        else:
            block = input("填充方块(预设的方块名/ID)")
            if block in config.preset:
                block_id = config.preset[block]
            else:
                block_id = block
        command = Fill()
        command.coordinate_get()
        command.result()
