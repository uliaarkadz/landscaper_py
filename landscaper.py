winner = 1200

tools = [{'name': "teeth", "profit": 1, "price": 0, "isAvailable": True},
         {'name': "rusty scissors", "profit": 5, "price": 5, "isAvailable": False},
         {'name': "old-timey push lawnmower", "profit": 50, "price": 25, "isAvailable": False},
         {'name': "fancy battery-powered lawnmower", "profit": 100, "price": 250, "isAvailable": False},
         {'name': "hire a team of starving students", "profit": 250, "price": 500, "isAvailable": False}
         ]

player ={
  "bankAccount": 0,
  "tool": 0,
  "availableTools": [tools[0]['name']],
  "isWinner": False,
  "allToolsSet": False,
}

def use_tool():
    tool = tools[player["tool"]]
    print(f"You used ${tool['name']} for cutting grass and made ${tool['profit']} money")
    player["bankAccount"]+=tool['profit']


def buy_tools():
    if(player["tool"] + 1 < len(tools)):
        next_tool = tools[player["tool"] + 1]
        if(next_tool["price"] <= player["bankAccount"]):
            player["bankAccount"]-= next_tool["price"]
            player["tool"]+=1
            tools[player["tool"]]["isAvailable"] = True
            player["availableTools"].append(tools[player["tool"]]["name"])
        else:
            print("Not enough money to buy a new tool")
    else:
        print("No more tools available to use")

def reset_game():
    player["allToolsSet"] = False
    player["availableTools"] =[tools[0]['name']]
    player['bankAccount'] = 0
    player["isWinner"] = False
    player["tool"] = 0


def define_winner():
    if(int(player["tool"]) == int(len(tools)-1) and player["bankAccount"] >= winner):
        player["isWinner"] = True        
        print("You are the winner")

            
print("************WELCOME TO LANDSCAPER GAME**************")

answer = input("Would you like to start the game? Answer [y]es or [n]o. ")
if (answer.lower() == "y"):
    while not player["isWinner"]:
        answer = input(f"You bank account currently has $ {player["bankAccount"]} do you want [c]ut the grass or [b]uy a new tool or would you like to [r]eset the game or [q]uit? ")
        if(answer.lower() == "c"):
            use_tool()
        elif(answer.lower() == "b"):
            buy_tools()
        elif(answer.lower() == "r"):
            reset_game()
            print(player['isWinner'])
        elif(answer.lower() == "q"):
           break
        else:
            print("Wrong input")
        define_winner()
        if(player["isWinner"]):
            answer = input("Would you like to [r]eset the game?")
            if answer == "r" : reset_game()
            else:
                print("Wrong input")
else:
    print("The game is OVER")

