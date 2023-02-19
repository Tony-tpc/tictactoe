def player_num(a):
    global pos_x, pos_y
    if a == 2:
        pos_x = int(input("列数:"))
        pos_y = int(input("行数:"))
    else:
        print("人机对弈")


def run(sth):
    global ctrl_round, pos_x, pos_y, control
    i = 0
    if int(ctrl_round/2) == ctrl_round/2:
        print("o行")
        player_num(sth)
        exam(pos_x, pos_y, player1, "o ")
    else:
        print("x行")
        player_num(sth)
        exam(pos_x, pos_y, player2, "x ")


def exam(a, b, c, d):
    global game_list, ctrl_round, player, control
    if a < 4 and b < 4:
        y = [a, b]
        if [a, b] in player:
            print("输入错误")
        else:
            c.append([a, b])
            ctrl_round = ctrl_round+1
            player.append([a, b])
            game_list[b][a] = d
            for f in game_list:
                print("   ".join(f))
            print(c)
            if len(c) > 2:  # 判断胜利
                for x in c:
                    if x == [a, b]:
                        pass
                    elif ((x[0]-a)**2+(x[1]-b)**2)**(1/2) <= 2**(1/2):
                        move_x = x[0]-a
                        move_y = x[1]-b
                        if len(player) == 9:
                            control = 2
                        for s in c:
                            if s[0]-move_x == x[0] and s[1]-move_y == x[1]:
                                control = 1
                        if control == 1:
                            print(f"{d}赢了")

                        if control == 2:
                            print("平局")

    else:
        print("不在范围")


game_list = [
            [".\\", "一", "二", "三", "\n"], 
            ["一", "--", "--", "--", "\n"], 
            ["二", "--", "--", "--", "\n"], 
            ["三", "--", "--", "--"]]
for i in game_list:
    print("   ".join(i))
player1 = []
player2 = []
player = []
ctrl_round = 0
control = 0
while True:
    if control==0:
        run(2)
       
    else:
        break
