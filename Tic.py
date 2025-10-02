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
# pau.hotkey('alt', 'tab')
# img = pau.screenshot(region=(750,150,1350,1280)).save("tic.png")
# img = pau.screenshot(allScreens=True).save("tic_tac.png")


# # # # img = pau.locateCenterOnScreen('image.png')

# pau.hold = 5
time.sleep(5)

# pau.dragTo(930,380)
# # print(pau.position())

# # topLeft, topRight, bottomLeft, bottomeRight :(750,150), (2100,150),(750, 1430), (2100,1430)







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









# # color1 = pau.pixel(930,380)
# # print(color1)

firstSpot_X = 930
firstSpot_Y = 380
secondSpot_X = 1040

game = []  # 2D array
location = {}

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

# Print the full board
print("Final Board:")
for r in game:
    print(r)
print(location)


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

# Print the assistant's reply
print(response.choices[0].message.content)









# import pyautogui as pau
# import time

# firstSpot_X = 930
# firstSpot_Y = 380

# for y in range(3):  # 3 rows
#     currentY = firstSpot_Y + 385 * y
#     for x in range(3):  # 3 columns
#         currentX = firstSpot_X + 395 * x 

#         # first pixel
#         fx = currentX + 395
#         fy = currentY
#         pau.moveTo(fx, fy, duration=0.2)   # move mouse
#         first = pau.pixel(fx, fy)

#         # second pixel
#         sx = currentX + 395 * 2
#         sy = currentY
#         pau.moveTo(sx, sy, duration=0.2)   # move mouse
#         second = pau.pixel(sx, sy)

#         # print result with coordinates
#         print(f"y={y+1}, x={x+1} ->", check_sign(first, second))

#         time.sleep(0.2)  # small pause so you can see the movement












##############chech the postion of the mouse continuously

# import pyautogui, sys
# import keyboard
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
#         if keyboard.is_pressed ('ctrl+shift') :
#             break
# except KeyboardInterrupt:
#     print('\n')

























##################################  AI made 
# import pyautogui as pau
# import time

# print("Move your mouse to the TOP-LEFT of the FIRST square (row=1,col=1), then press Enter...")
# input()
# firstSpot_X, firstSpot_Y = pau.position()
# print("Recorded first spot:", firstSpot_X, firstSpot_Y)

# print("\nMove your mouse to the TOP-LEFT of the NEXT square to the right (row=1,col=2), then press Enter...")
# input()
# secondX, secondY = pau.position()
# stepX = secondX - firstSpot_X
# print("Recorded X step:", stepX)

# print("\nMove your mouse to the TOP-LEFT of the NEXT square below (row=2,col=1), then press Enter...")
# input()
# thirdX, thirdY = pau.position()
# stepY = thirdY - firstSpot_Y
# print("Recorded Y step:", stepY)

# print("\n✅ Calibration done!")
# print(f"firstSpot_X={firstSpot_X}, firstSpot_Y={firstSpot_Y}, stepX={stepX}, stepY={stepY}")

# # === Now scan the full 3x3 grid ===
# for y in range(3):  # rows
#     for x in range(3):  # cols
#         posX = firstSpot_X + stepX * x
#         posY = firstSpot_Y + stepY * y

#         pau.moveTo(posX, posY, duration=0.2)   # show scanning
#         px = pau.pixel(posX, posY)
#         print(f"Row={y+1}, Col={x+1}, Pixel={px}")

#         time.sleep(0.2)




