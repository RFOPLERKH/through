import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = {}

    def add_item(self, item, quantity=1):
        if item.name in self.inventory:
            self.inventory[item.name] += quantity
        else:
            self.inventory[item.name] = quantity

    def remove_item(self, item, quantity=1):
        if item.name in self.inventory:
            if self.inventory[item.name] >= quantity:
                self.inventory[item.name] -= quantity
                return True
            else:
                return False
        else:
            return False

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_inventory(player):
    print("\n你的背包：")
    for item_name, quantity in player.inventory.items():
        print(f"{item_name}: {quantity}个")

def choose_action():
    print("\n你可以做以下操作：")
    print("1. 查看角色状态")
    print("2. 查看背包")
    print("3. 探险")
    print("4. 完成任务")
    print("5. 与他人交流")
    print("6. 退出游戏")
    while True:
        try:
            choice = int(input("请输入你的选择（1/2/3/4/5/6）："))
            if 1 <= choice <= 6:
                return choice
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def show_character_status(player):
    print(f"\n{name}生命值：{player.health}")

def explore(player):
    delay_print("\n你穿越到了秦朝的时空，周围是陌生的环境。")
    encounter = random.choice(["task", "item", "danger", "nothing"])
    
    if encounter == "task":
        complete_task(player)
    elif encounter == "item":
        collect_item(player)
    elif encounter == "danger":
        danger_encounter(player)
    else:
        delay_print("这片区域看起来平静无事。")

def complete_task(player):
    delay_print("\n你遇到了一个有求于你的人。")
    delay_print("陌生人：我有一个任务需要完成，你能帮我吗？")
    while True:
        choice = input("你愿意帮助他吗？(是/否)：").lower()
        if choice == "是":
            delay_print("陌生人：太感谢了！任务就是...")
            # 在这里添加具体的任务内容，根据玩家的选择和任务进展进行对话和交互
            break
        elif choice == "否":
            delay_print("陌生人：好吧，算了。")
            break
        else:
            delay_print("无效的选择，请重新输入。")

def collect_item(player):
    item = random.choice(item_list)
    quantity = random.randint(1, 5)
    player.add_item(item, quantity)
    delay_print(f"你发现了{item.name} x {quantity}。")

def danger_encounter(player):
    delay_print("突然，你遭遇了敌对势力的袭击！")
    # 在这里添加具体的危险事件，根据玩家的选择和决策进行对话和交互
    pass

def interact_with_others(player):
    # 在这里添加与其他角色的对话和交流功能
    pass

def play_game():
    player_name = input("请输入你的名字：")
    player = Player(player_name)
    
    item_list = [
        Item("水", "清澈的泉水"),
        Item("食物", "补充生命值的食物"),
        Item("草药", "可以治疗的草药"),
        Item("藏宝图", "寻找宝藏的地图")
    ]

    delay_print(f"欢迎来到《穿越秦朝的对话生存游戏》，{player_name}！")
    delay_print("你将在这片陌生的秦朝时空中冒险。")

    while True:
        show_character_status(player)
        action = choose_action()

        if action == 1:
            show_character_status(player)
        elif action == 2:
            show_inventory(player)
        elif action == 3:
            explore(player)
        elif action == 4:
            complete_task(player)
        elif action == 5:
            interact_with_others(player)
        elif action == 6:
            delay_print("谢谢你玩《穿越秦朝的对话生存游戏》，再见！")
            exit()

if __name__ == "__main__":
    play_game()
