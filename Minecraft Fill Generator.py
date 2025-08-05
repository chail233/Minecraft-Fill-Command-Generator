preset = {}
axis_lock = {"x":False,"y":False,"z":False}
class Fill():
    def __init__(self):
        self.start = {"x":None,"y":None,"z":None}
        self.end = {"x":None,"y":None,"z":None}
    def result(self):
        print(f"/fill {self.start['x']} {self.start['y']} {self.start['z']} {self.end['x']} {self.end['y']} {self.end['z']} {block_id}")
    def coordinate_get(self):
        for i in ("x","y","z"):
            if axis_lock[i]:
                self.start[i] = axis_lock[f"{i}_coordinate"]
                self.end[i] = axis_lock[f"{i}_coordinate"]
            else:
                self.start[i] = start_coordinate.pop(0)
                self.end[i] = end_coordinate.pop(0)

def choice_fun():
    c = input("请选择:")
    return c
def menu():
    global choice_fun,preset,axis_lock
    print("1.管理方块预设")
    print("2.锁定填充方块")
    print("3.解除填充方块锁定")
    print("4.锁定坐标轴")
    print("5.解除坐标轴锁定")
    choice = choice_fun()
    if choice == "1":
        print('1.增加填充方块预设')
        print("2.删除填充方块预设")
        print("3.查看填充方块预设")
        choice = choice_fun()
        if choice == "1":
            name = input("方块名(可随意设置方便使用,不能以“lock”作为方块名，会出bug！)")
            id = input("方块id(不可随意设置，必须使用游戏中有效的id)")
            preset[name] = id
            print(f"添加完成！{name}:{id}")
        elif choice == "2":
            name = input("需要删除的方块名")
            if name not in preset:
                print("该方块名不在预设中！")
            else:
                del preset[name]
                print(f"删除成功！{name}")
        elif choice == "3":
            print(preset)
        else:
            print("无效选择！")
    elif choice == "2":
        print("1.通过id锁定")
        print("2.通过预设方块名锁定")
        choice = choice_fun()
        if choice == "1":
            id = input("请输入物品id:")
            preset["lock"] = id
            print("锁定完毕！")
        elif choice == "2":
            name = input("请输入预设的方块名:")
            if name not in preset:
                print("该方块名不存在！")
            else:
                preset["lock"] = preset[name]
        else:
            print("无效选择！")
    elif choice == "3":
        if preset["lock"] is not None:
            del preset["lock"]
            print("已解除锁定！")
        else:
            print("当前填充方块没有锁定！")
    elif choice == "4":
        axis = input("请输入要锁定的轴(x/y/z)(锁定后的轴请不要输入坐标，以免出现错误)")
        if axis == "x":
            axis_lock["x"] = True
            axis_lock["x_coordinate"] = input("坐标值")
            print(f"x轴已锁定坐标{axis_lock['x_coordinate']}")
        elif axis == "y":
            axis_lock["y"] = True
            axis_lock["y_coordinate"] = input("坐标值")
            print(f"y轴已锁定坐标{axis_lock['y_coordinate']}")
        elif axis == "z":
            axis_lock["z"] = True
            axis_lock["z_coordinate"] = input("坐标值")
            print(f"z轴已锁定坐标{axis_lock['z_coordinate']}")
    elif choice == "5":
        axis = input("请输入需要解除锁定的轴(x/y/z)")
        if axis_lock[axis]:
            axis_lock[axis] = False
            print(f"{axis}轴已解除锁定！")
        else:
            print(f"错误，{axis}轴没有被锁定！")
while True:
    start_coordinate = input("起始坐标(直接按回车可进入菜单)")
    if start_coordinate == "":
        menu()
    else:
        end_coordinate = input("终点坐标").split()
        start_coordinate = start_coordinate.split()
        if "lock" in preset:
            block_id = preset["lock"]
        else:
            block = input("填充方块(预设的方块名/ID)")
            if block in preset:
                block_id = preset[block]
            else:
                block_id = block
        command = Fill()
        command.coordinate_get()
        command.result()