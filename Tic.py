import pyautogui as pau
import keyboard
import os
from openai import OpenAI
import time 
import webbrowser

# Setup Groq client

client = OpenAI(
    api_key="your_real_api_key_here",  # or "your_real_api_key_here"
    base_url="https://api.groq.com/openai/v1"
)




#### this go to the page of the game and take a screenshot

webbrowser.open("https://playtictactoe.org/")


time.sleep(5)


game = []  # 2D array
location = {}




##### this check the sign if it is X or O
def check_sign(x,o):

    if x == 0 and o == 0 :
        return 'EMPTY'
    elif x == 0 and o == 255 :
        return 'X'
    elif x == 255 and o == 0 :
        return 'O'
    elif x == 255 and o == 255 :
        return 'INVALIDE'
    else :
        return 'ERROR'


def move():
    firstSpot_X = 930
    firstSpot_Y = 380
    secondSpot_X = 1040

    for y in range(3):  # 3 rows
        currentY = firstSpot_Y + 395 * y
        row = []  # store one row of results

        for x in range(3):  # 3 columns
            currentX1 = firstSpot_X + 395 * x 
            currentX2 = secondSpot_X + 395 * x

            pau.moveTo(currentX1, currentY)
            first = pau.pixel(currentX1, currentY)
            pau.moveTo(currentX2, currentY)
            second = pau.pixel(currentX2, currentY)

            result = check_sign(first[0], second[0])
            print(f"Row={y+1}, Column={x+1} ->", result)

            row.append(result)  ######## store the result of each square in a 2D array

            location[(y, x)] = {    ######## store the location of each square in a dictionary
                'coordinations' : ((currentX1, currentY), (currentX2, currentY))
            }

        game.append(row) 



while True :


    ###### Print the full board
    print("Final Board:")
    for r in game:
        print(r)


    ############# AI 

    # Send a single chat message
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "You are a proffessional Tic-Tac_Toe player"},
            {"role": "user", "content": f"""

            Tic Tac Toe - Rules of the Game
            1-The game is played on a 3 by 3 grid.
            2-Two players take turns. One player uses X and the other player uses O.
            3-Players take turns placing their mark (X or O) in an empty square.
            4-A square cannot be used more than once.
            5-The first player to get three of their marks in a row wins. The row can be horizontal, vertical, or diagonal.
            6-If all nine squares are filled and no player has three in a row, the game ends in a draw.
            
            you should play for the player 'X' and I will give you a
            set with every row of the tic tac toe and I want you to tell me where should I play next? 
            this is the set: {game}.
            
            you answer should only include the place of the next move
            I emphasize that you should only say the place of the next move without even saying any word,
            just a place that consist of the number of the row and the number of the column (for example:(2,1))
            """}
        ]
    )

    ###### the mouse go to the place the AI decided and click 

    reply = response.choices[0].message.content.strip()  


    row, col = map(int, reply.strip("()").split(","))
    coords = location[(row, col)]["coordinations"]

    # Print the assistant's reply
    print(coords)

    pau.click(coords, duration=1)

    time.sleep(2)

    all_full = all(cell != "Empty" for row in game for cell in row)
    if all_full:
        continue
    else:
        break

