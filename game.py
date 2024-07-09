import random
def hangman():
    word_list = ["cat","dog","bear","lion","seal"]
    random_number = random.randint(0,4)
    word = word_list[random_number]
    wrong = 0
    stages = ["\n",
              "___________     ",
              "|               ",
              "|          |    ",
              "|          O    ",
              "|         /|L   ",
              "|         /  L  ",
              "|               "
              ]
    rletters = list(word)
    board = ["_"]*len(word)
    print("ハングマンへようこそ")
    win = False
    while wrong < len(stages)-1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
            e = wrong
        print(" ".join(board))
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ちです\n{}".format(word))
            win = True
            break

    if not win:
        print("あなたの負けです\n正解は{}".format(word))
    
        
