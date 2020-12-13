from ctypes import WinDLL, Structure, sizeof, byref
from ctypes.wintypes import SHORT, WCHAR, UINT, ULONG, DWORD
import random
kernel32_dll = WinDLL("kernel32.dll")
LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11
class COORD(Structure):
    _fields_ = [
        ("X", SHORT),
        ("Y", SHORT),
    ]
class CONSOLE_FONT_INFOEX(Structure):
    _fields_ = [
        ("cbSize", ULONG),
        ("nFont", DWORD),
        ("dwFontSize", COORD),
        ("FontFamily", UINT),
        ("FontWeight", UINT),
        ("FaceName", WCHAR * LF_FACESIZE)
    ]
get_std_handle_func = kernel32_dll.GetStdHandle
get_current_console_font_ex_func = kernel32_dll.GetCurrentConsoleFontEx
set_current_console_font_ex_func = kernel32_dll.SetCurrentConsoleFontEx
font = CONSOLE_FONT_INFOEX()
font.cbSize = sizeof(CONSOLE_FONT_INFOEX)
stdout = get_std_handle_func(STD_OUTPUT_HANDLE)
font.dwFontSize.X = 30
font.dwFontSize.Y = 60
set_current_console_font_ex_func(stdout, False, byref(font))

allpcs = [61,62,63,64,65,66,67,68,11,12,13,14,15,16,17,18,72,77,2,7,73,76,3,6,71,78,1,8,74,4,75,5]
wpieces = [61,62,63,64,65,66,67,68,72,77,73,76,71,78,74,75]
wpawn = [61,62,63,64,65,66,67,68]
bpawn = [11,12,13,14,15,16,17,18]
wknight = [72,77]
bknight = [2,7]
wbischop = [73,76]
bbischop = [3,6]
wrook = [71,78]
brook = [1,8]
wqueen = [74]
bqueen = [4]
wking = [75]
bking = [5]

board = []
schaakalgorithm = [9,10,11,1,-11,-10,-9,-1]
forbiddennmbrs = [9,10,19,20,29,30,39,40,49,50,59,60,69,70,79]

wpawncmv = [9,11]
bpawncmv = [-9,-11]
knightmv = [8,12,19,21,-8,-12,-19,-21]
bischopmv = [11,22,33,44,55,66,77,-11,-22,-33,-44,-55,-66,-77,9,18,27,36,45,54,63,-9,-18,-27,-36,-45,-54,-63]
rookmv = [10,20,30,40,50,60,70,-10,-20,-30,-40,-50,-60,-70,1,2,3,4,5,6,7,-1,-2,-3,-4,-5,-6,-7]
kingmv = [1,-1,9,10,11,-9,-10,-11]
wcastlingmv = [73,77]
bcastlingmv = [3,7]

pcsbox = 0
y = 0
x = 0
x2 = 0
cnt = 0
brd = 0
turn = 0
inp2 = 0
impmv = 0
bot = 0

mem = []

select = input("bot of 1v1?")
if select == "bot":
    bot = 1
def wcheck():
    if inp2 in bpawn:
        bpawn.remove(inp2)
    if inp2 in brook:
        brook.remove(inp2)
    if inp2 in bbischop:
        bbischop.remove(inp2)
    if inp2 in bknight:
        bknight.remove(inp2)
    if inp2 in bqueen:
        bqueen.remove(inp2)
    if inp2 in bking:
        bking.remove(inp2)
def bcheck():
    if inp2 in wpawn:
        wpawn.remove(inp2)
    if inp2 in wrook:
        wrook.remove(inp2)
    if inp2 in wbischop:
        wbischop.remove(inp2)
    if inp2 in wknight:
        wknight.remove(inp2)
    if inp2 in wqueen:
        wqueen.remove(inp2)
    if inp2 in wking:
        wking.remove(inp2)
while True:
    if turn == 0:
        y = y + 1
    else:
        if y == 0:
            y = 79
        y = y - 1
    board.append(y)
    if y in wpawn:
        mem.append("○")
    elif y in bpawn:
        mem.append("•")
    elif y in wknight:
        mem.append("k")
    elif y in bknight:
        mem.append("K")
    elif y in wbischop:
        mem.append("b")
    elif y in bbischop:
        mem.append("B")
    elif y in wrook:
        mem.append("r")
    elif y in brook:
        mem.append("R")
    elif y in wqueen:
        mem.append("q")
    elif y in bqueen:
        mem.append("Q")
    elif y in wking:
        mem.append("a")
    elif y in bking:
        mem.append("A")
    elif brd == 0:
        mem.append("-")
    else:
        mem.append("=")
    if brd == 0:
        brd = 1
    else:
        brd = 0
    cnt = cnt + 1
    if cnt == 8:
        if brd == 0:
            brd = 1
        else:
            brd = 0
        if turn == 0:
            y = y + 2
        else:
            y = y - 2
        cnt = 0
        if impmv == 0 and bot == 1 or bot == 0:
            if pcsbox == 0 and turn == 0:
                print(*mem,"       1  2  3  4  5  6  7  8 ")
            elif turn == 0:
                print(*mem,"      ",*board)
            if turn == 1 and y < 9:
                print(*mem,"       8  7  6  5  4  3  2  1")
            elif turn == 1:
                print(*mem,"      ",*board)
            elif y > 70:
                print("\n")
        pcsbox = 1
        impmv = 0
        board.clear()
        mem.clear()
        if y == 80 or y == -1:
            pcsbox = 0
            y = 0

            if turn == 0:
                if bot == 0:
                    inp1 = int(input("move?"))
                    inp2 = int(input("to?"))
                else:
                    rndmv = random.choice(wpieces)
                    inp1 = rndmv
                    if inp1 in wpawn:
                        inp2 = inp1 + random.choice([-10,-20])
                    if inp1 in wknight:
                        inp2 = inp1 + random.choice([8,12,19,21,-8,-12,-19,-21])
                    if inp1 in wbischop:
                        inp2 = inp1 + random.choice([11,22,33,44,55,66,77,-11,-22,-33,-44,-55,-66,-77,9,18,27,36,45,54,63,-9,-18,-27,-36,-45,-54,-63])
                    if inp1 in wrook:
                        inp2 = inp1 + random.choice([10,20,30,40,50,60,70,-10,-20,-30,-40,-50,-60,-70,1,2,3,4,5,6,7,-1,-2,-3,-4,-5,-6,-7])
                    if inp1 in wqueen:
                        inp2 = inp1 + random.choice([10,20,30,40,50,60,70,-10,-20,-30,-40,-50,-60,-70,1,2,3,4,5,6,7,-1,-2,-3,-4,-5,-6,-7,11,22,33,44,55,66,77,-11,-22,-33,-44,-55,-66,-77,9,18,27,36,45,54,63,-9,-18,-27,-36,-45,-54,-63])
                    if inp1 in wking:
                        inp2 = inp1 + random.choice([1,-1,9,10,11,-9,-10,-11])
                    print(inp1,inp2)
                if inp2 in forbiddennmbrs or inp2 > 78 or inp2 < 1:
                    print("move is not valid because to destination is outside the chessboard")
                    impmv = 0
                else:
                    if inp1 in wpawn and inp2 not in allpcs and inp1 in [11,12,13,14,15,16,17,18] and inp1 == inp2 + 10:
                        pcschoice = int(input("choose your piece:\n(1 = knight 2 = bischop 3 = rook 4 = queen)"))
                        allpcs.remove(inp1)
                        allpcs.append(inp2)
                        wpawn.remove(inp1)
                        if pcschoice == 1:
                            wknight.append(inp2)
                        if pcschoice == 2:
                            wbischop.append(inp2)
                        if pcschoice == 3:
                            wrook.append(inp2)
                        if pcschoice == 4:
                            wqueen.append(inp2)
                    elif inp1 in wpawn and inp2 in allpcs and inp2 not in wpieces and inp1 in [11,12,13,14,15,16,17,18] and inp1 - inp2 in wpawncmv:
                        pcschoice = int(input("choose your piece:\n(1 = knight 2 = bischop 3 = rook 4 = queen)"))
                        wcheck()
                        allpcs.remove(inp1)
                        allpcs.append(inp2)
                        wpawn.remove(inp1)
                        if pcschoice == 1:
                            wknight.append(inp2)
                        if pcschoice == 2:
                            wbischop.append(inp2)
                        if pcschoice == 3:
                            wrook.append(inp2)
                        if pcschoice == 4:
                            wqueen.append(inp2)
                    elif inp1 in wpawn and inp2 in allpcs and inp2 not in wpieces and inp1 - inp2 in wpawncmv:
                        wcheck()
                        wpawn.remove(inp1)
                        wpawn.append(inp2)
                        allpcs.remove(inp1)
                        allpcs.append(inp2)
                        wpieces.remove(inp1)
                        wpieces.append(inp2)
                    elif (inp1 in wpawn and inp2 not in allpcs and inp1 == inp2 + 10 or (inp1 in [61,62,63,64,65,66,67,68] and inp1 == inp2 + 20 and inp1 - 10 not in allpcs)):
                        wpawn.remove(inp1)
                        wpawn.append(inp2)
                        allpcs.remove(inp1)
                        allpcs.append(inp2)
                        wpieces.remove(inp1)
                        wpieces.append(inp2)
                    elif inp1 in wknight and inp1 - inp2 in knightmv:
                        wcheck()
                        wknight.remove(inp1)
                        wknight.append(inp2)
                        allpcs.remove(inp1)
                        allpcs.append(inp2)
                        wpieces.remove(inp1)
                        wpieces.append(inp2)
                    elif inp1 in wbischop and inp1 - inp2 in bischopmv:
                        inp3 = inp1 - inp2
                        inp4 = inp2
                        if inp3 in [11,22,33,44,55,66,77,88]:
                            mvchk = 0
                        if inp3 in [-11,-22,-33,-44,-55,-66,-77,-88]:
                            mvchk = 1
                        if inp3 in [-9,-18,-27,-36,-45,-54,-63,-72]:
                            mvchk = 2
                        if inp3 in [9,18,27,36,45,54,63,72]:
                            mvchk = 3
                        while inp3 in bischopmv and inp1 != inp4 and pcsbox == 0:
                            if inp4 in allpcs and inp2 != inp4:
                                pcsbox = 1
                                break
                            elif inp2 in allpcs and inp2 not in wpieces:
                                wcheck()
                                wbischop.remove(inp1)
                                wbischop.append(inp2)
                                allpcs.remove(inp1)
                                allpcs.append(inp2)
                                pcsbox = 2
                            if mvchk == 0:
                                inp4 = inp4 + 11
                            if mvchk == 1:
                                inp4 = inp4 - 11
                            if mvchk == 2:
                                inp4 = inp4 - 9
                            if mvchk == 3:
                                inp4 = inp4 + 9
                        if pcsbox == 0:
                            wcheck()
                            wbischop.remove(inp1)
                            wbischop.append(inp2)
                            allpcs.remove(inp1)
                            allpcs.append(inp2)
                            wpieces.remove(inp1)
                            wpieces.append(inp2)
                        if pcsbox == 1:
                            print("a piece is blocking the path")
                            impmv = 1
                    elif inp1 in wrook and inp1 - inp2 in rookmv:
                        inp3 = inp1 - inp2
                        inp4 = inp2
                        if inp3 in [10,20,30,40,50,60,70]:
                            mvchk = 0
                        if inp3 in [-10,-20,-30,-40,-50,-60,-70]:
                            mvchk = 1
                        if inp3 in [1,2,3,4,5,6,7]:
                            mvchk = 2
                        if inp3 in [-1,-2,-3,-4,-5,-6,-7]:
                            mvchk = 3
                        while inp3 in rookmv and inp1 != inp4 and pcsbox == 0:
                            if inp4 in allpcs and inp2 != inp4:
                                pcsbox = 1
                                break
                            elif inp2 in allpcs and inp2 not in wpieces:
                                wcheck()
                                wrook.remove(inp1)
                                wrook.append(inp2)
                                allpcs.remove(inp1)
                                allpcs.append(inp2)
                                pcsbox = 2
                            if mvchk == 0:
                                inp4 = inp4 + 10
                            if mvchk == 1:
                                inp4 = inp4 - 10
                            if mvchk == 2:
                                inp4 = inp4 + 1
                            if mvchk == 3:
                                inp4 = inp4 - 1
                        if pcsbox == 0:
                            wcheck()
                            wrook.remove(inp1)
                            wrook.append(inp2)
                            allpcs.remove(inp1)
                            allpcs.append(inp2)
                            wpieces.remove(inp1)
                            wpieces.append(inp2)
                        if pcsbox == 1:
                            print("a piece is blocking the path")
                            impmv = 1
                    elif inp1 in wqueen and (inp1 - inp2 in rookmv or bischopmv):
                        inp3 = inp1 - inp2
                        inp4 = inp2
                        if inp3 in [10,20,30,40,50,60,70]:
                            mvchk = 0
                        if inp3 in [-10,-20,-30,-40,-50,-60,-70]:
                            mvchk = 1
                        if inp3 in [1,2,3,4,5,6,7]:
                            mvchk = 2
                        if inp3 in [-1,-2,-3,-4,-5,-6,-7]:
                            mvchk = 3
                        if inp3 in [11,22,33,44,55,66,77,88]:
                            mvchk = 4
                        if inp3 in [-11,-22,-33,-44,-55,-66,-77,-88]:
                            mvchk = 5
                        if inp3 in [-9,-18,-27,-36,-45,-54,-63,-72]:
                            mvchk = 6
                        if inp3 in [9,18,27,36,45,54,63,72]:
                            mvchk = 7
                        while (inp3 in rookmv or bischopmv) and inp1 != inp4 and pcsbox == 0:
                            if inp4 in allpcs and inp2 != inp4:
                                pcsbox = 1
                                break
                            elif inp2 in allpcs and inp2 not in wpieces:
                                wcheck()
                                wqueen.remove(inp1)
                                wqueen.append(inp2)
                                allpcs.remove(inp1)
                                allpcs.append(inp2)
                                pcsbox = 2
                            if mvchk == 0:
                                inp4 = inp4 + 10
                            if mvchk == 1:
                                inp4 = inp4 - 10
                            if mvchk == 2:
                                inp4 = inp4 + 1
                            if mvchk == 3:
                                inp4 = inp4 - 1
                            if mvchk == 4:
                                inp4 = inp4 + 11
                            if mvchk == 5:
                                inp4 = inp4 - 11
                            if mvchk == 6:
                                inp4 = inp4 - 9
                            if mvchk == 7:
                                inp4 = inp4 + 9
                        if pcsbox == 0:
                            wcheck()
                            wqueen.remove(inp1)
                            wqueen.append(inp2)
                            allpcs.remove(inp1)
                            allpcs.append(inp2)
                            wpieces.remove(inp1)
                            wpieces.append(inp2)
                        if pcsbox == 1:
                            print("a piece is blocking the path")
                            impmv = 1
                    elif inp1 in wking and inp1 - inp2 in kingmv or inp1 in wking and inp2 in wcastlingmv and inp1 == 75:
                        inp3 = inp2
                        chkchkmate = 1
                        if inp2 in wcastlingmv and inp1 == 75:
                            if inp2 == 72 and 72 not in allpcs and 73 not in allpcs and 74 not in allpcs:
                                wrook.remove(71)
                                wrook.append(74)
                            elif 76 not in allpcs and 77 not in allpcs:
                                wrook.remove(78)
                                wrook.append(76)
                            else:
                                chkchkmate = 0
                        while chkchkmate == 1:
                            inp3 = inp3 + 9
                            if inp3 in bbischop or inp3 in bqueen:
                                chkchkmate = 0
                            if inp3 in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 2
                        inp3 = inp2
                        while chkchkmate == 2:
                            inp3 = inp3 + 10
                            if inp3 in brook or inp3 in bqueen:
                                chkchkmate = 0
                            if inp3 in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 3
                        inp3 = inp2
                        while chkchkmate == 3:
                            inp3 = inp3 + 11
                            if inp3 in bbischop or inp3 in bqueen:
                                chkchkmate = 0
                            if inp3 in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 4
                        inp3 = inp2
                        while chkchkmate == 4:
                            inp3 = inp3 + 1
                            if inp3 in brook or inp3 in bqueen:
                                chkchkmate = 0
                            if inp3 in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 5
                        inp3 = inp2
                        while chkchkmate == 5:
                            inp3 = inp3 - 11
                            if inp3 in bbischop or inp3 in bqueen:
                                chkchkmate = 0
                            if inp3 in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 6
                        inp3 = inp2
                        while chkchkmate == 6:
                            inp3 = inp3 - 10
                            if inp3 in brook or inp3 in bqueen:
                                chkchkmate = 0
                            if inp3 in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 7
                        inp3 = inp2
                        while chkchkmate == 7:
                            inp3 = inp3 - 1
                            if inp3 in brook or inp3 in bqueen:
                                chkchkmate = 0
                            if inp3 in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 8
                        inp3 = inp2
                        while chkchkmate == 8:
                            inp3 = inp3 - 9
                            if inp3 in bbischop or inp3 in bqueen:
                                chkchkmate = 0
                            if inp3 in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 9
                        if chkchkmate == 0:
                            print("move is not valid")
                            impmv = 1
                        elif chkchkmate != 0:
                            wking.remove(inp1)
                            wking.append(inp2)
                            allpcs.remove(inp1)
                            allpcs.append(inp2)
                            if inp2 in allpcs and inp2 not in wpieces:
                                wcheck()
                        else:
                            print("move is not valid")
                            impmv = 1
                    else:
                        print("move is not valid")
                        impmv = 1
                    pcsbox = 0
                    if impmv == 0:
                        turn = 1
                    else:
                        turn = 0
                    impmv = 0
            elif turn == 1:
                inp1 = int(input("move?"))
                inp2 = int(input("to?"))
                if inp2 in forbiddennmbrs or inp2 > 78 or inp2 < 1:
                    print("move is not valid because to destination is outside the chessboard")
                    impmv = 1
                else:
                    if inp1 in bpawn and inp2 not in allpcs and inp1 in [61,62,63,64,65,66,67,68] and inp1 == inp2 - 10:
                        pcschoice = int(input("choose your piece:\n(1 = knight 2 = bischop 3 = rook 4 = queen)"))
                        allpcs.remove(inp1)
                        allpcs.append(inp2)
                        bpawn.remove(inp1)
                        if pcschoice == 1:
                            bknight.append(inp2)
                        if pcschoice == 2:
                            bbischop.append(inp2)
                        if pcschoice == 3:
                            brook.append(inp2)
                        if pcschoice == 4:
                            bqueen.append(inp2)
                    elif inp1 in bpawn and inp2 in wpieces and inp1 in [61,62,63,64,65,66,67,68] and inp1 - inp2 in bpawncmv:
                        pcschoice = int(input("choose your piece:\n(1 = knight 2 = bischop 3 = rook 4 = queen)"))
                        bcheck()
                        allpcs.remove(inp1)
                        allpcs.append(inp2)
                        bpawn.remove(inp1)
                        if pcschoice == 1:
                            bknight.append(inp2)
                        if pcschoice == 2:
                            bbischop.append(inp2)
                        if pcschoice == 3:
                            brook.append(inp2)
                        if pcschoice == 4:
                            bqueen.append(inp2)
                    elif inp1 in bpawn and inp2 in wpieces and inp1 - inp2 in bpawncmv:
                        bcheck()
                        bpawn.remove(inp1)
                        bpawn.append(inp2)
                        allpcs.remove(inp1)
                        allpcs.append(inp2)
                    elif inp1 in bpawn and inp1 in [11,12,13,14,15,16,17,18] and inp1 == inp2 - 20 and inp1 + 10 not in allpcs or inp1 in bpawn and inp1 == inp2 - 10 and inp2 not in allpcs or inp1 in bpawn and inp1 - inp2 in bpawncmv:
                        if inp2 in allpcs:
                            allpcs.remove(inp2)
                        bcheck()
                        allpcs.remove(inp1)
                        allpcs.append(inp2)
                        bpawn.remove(inp1)
                        bpawn.append(inp2)
                    elif inp1 in bknight and inp1 - inp2 in knightmv:
                        allpcs.remove(inp1)
                        allpcs.append(inp2)
                        bknight.remove(inp1)
                        bknight.append(inp2)
                    elif inp1 in bbischop and inp1 - inp2 in bischopmv:
                        inp3 = inp1 - inp2
                        inp4 = inp2
                        if inp3 in [11,22,33,44,55,66,77,88]:
                            mvchk = 0
                        if inp3 in [-11,-22,-33,-44,-55,-66,-77,-88]:
                            mvchk = 1
                        if inp3 in [-9,-18,-27,-36,-45,-54,-63,-72]:
                            mvchk = 2
                        if inp3 in [9,18,27,36,45,54,63,72]:
                            mvchk = 3
                        while inp3 in bischopmv and inp1 != inp4 and pcsbox == 0:
                            if inp4 in allpcs and inp2 != inp4:
                                pcsbox = 1
                                break
                            elif inp2 in wpieces:
                                bcheck()
                                bbischop.remove(inp1)
                                bbischop.append(inp2)
                                allpcs.remove(inp1)
                                allpcs.append(inp2)
                                pcsbox = 2
                            if mvchk == 0:
                                inp4 = inp4 + 11
                            if mvchk == 1:
                                inp4 = inp4 - 11
                            if mvchk == 2:
                                inp4 = inp4 - 9
                            if mvchk == 3:
                                inp4 = inp4 + 9
                        if pcsbox == 0:
                            bcheck()
                            bbischop.remove(inp1)
                            bbischop.append(inp2)
                            allpcs.remove(inp1)
                            allpcs.append(inp2)
                        if pcsbox == 1:
                            print("a piece is blocking the path")
                            impmv = 1
                    elif inp1 in brook and inp1 - inp2 in rookmv:
                        inp3 = inp1 - inp2
                        inp4 = inp2
                        if inp3 in [10,20,30,40,50,60,70]:
                            mvchk = 0
                        if inp3 in [-10,-20,-30,-40,-50,-60,-70]:
                            mvchk = 1
                        if inp3 in [1,2,3,4,5,6,7]:
                            mvchk = 2
                        if inp3 in [-1,-2,-3,-4,-5,-6,-7]:
                            mvchk = 3
                        while inp3 in rookmv and inp1 != inp4 and pcsbox == 0:
                            if inp4 in allpcs and inp4 != inp2:
                                pcsbox = 1
                                break
                            elif inp2 in wpieces:
                                bcheck()
                                brook.remove(inp1)
                                brook.append(inp2)
                                allpcs.remove(inp1)
                                allpcs.append(inp2)
                                pcsbox = 2
                            if mvchk == 0:
                                inp4 = inp4 + 10
                            if mvchk == 1:
                                inp4 = inp4 - 10
                            if mvchk == 2:
                                inp4 = inp4 + 1
                            if mvchk == 3:
                                inp4 = inp4 - 1
                        if pcsbox == 0:
                            bcheck()
                            brook.remove(inp1)
                            brook.append(inp2)
                            allpcs.remove(inp1)
                            allpcs.append(inp2)
                        if pcsbox == 1:
                            print("a piece is blocking the path")
                            impmv = 1
                    elif inp1 in bqueen and (inp1 - inp2 in rookmv or bischopmv):
                        inp3 = inp1 - inp2
                        inp4 = inp2
                        if inp3 in [10,20,30,40,50,60,70]:
                            mvchk = 0
                        if inp3 in [-10,-20,-30,-40,-50,-60,-70]:
                            mvchk = 1
                        if inp3 in [1,2,3,4,5,6,7]:
                            mvchk = 2
                        if inp3 in [-1,-2,-3,-4,-5,-6,-7]:
                            mvchk = 3
                        if inp3 in [11,22,33,44,55,66,77,88]:
                            mvchk = 4
                        if inp3 in [-11,-22,-33,-44,-55,-66,-77,-88]:
                            mvchk = 5
                        if inp3 in [-9,-18,-27,-36,-45,-54,-63,-72]:
                            mvchk = 6
                        if inp3 in [9,18,27,36,45,54,63,72]:
                            mvchk = 7
                        while (inp3 in rookmv or bischopmv) and inp1 != inp4 and pcsbox == 0:
                            if inp4 in allpcs and inp4 != inp2:
                                pcsbox = 1
                                break
                            elif inp2 in wpieces:
                                bcheck()
                                bqueen.remove(inp1)
                                bqueen.append(inp2)
                                allpcs.remove(inp1)
                                allpcs.append(inp2)
                                pcsbox = 2
                            if mvchk == 0:
                                inp4 = inp4 + 10
                            if mvchk == 1:
                                inp4 = inp4 - 10
                            if mvchk == 2:
                                inp4 = inp4 + 1
                            if mvchk == 3:
                                inp4 = inp4 - 1
                            if mvchk == 4:
                                inp4 = inp4 + 11
                            if mvchk == 5:
                                inp4 = inp4 - 11
                            if mvchk == 6:
                                inp4 = inp4 - 9
                            if mvchk == 7:
                                inp4 = inp4 + 9
                        if pcsbox == 0:
                            bcheck()
                            bqueen.remove(inp1)
                            bqueen.append(inp2)
                            allpcs.remove(inp1)
                            allpcs.append(inp2)
                        if pcsbox == 1:
                            print("a piece is blocking the path")
                            impmv = 1
                    elif inp1 in bking and inp1 - inp2 in kingmv or inp1 in bking and inp2 in bcastlingmv and inp1 == 5:
                        chkchkmate = 1
                        inp3 = inp2
                        if inp2 in bcastlingmv and inp1 == 5:
                            if inp2 == 2 and 2 not in allpcs and 3 not in allpcs and 4 not in allpcs:
                                brook.remove(1)
                                brook.append(4)
                            elif 6 not in allpcs and 7 not in allpcs:
                                brook.remove(8)
                                brook.append(6)
                            else:
                                chkchkmate = 0
                        while chkchkmate == 1:
                            inp3 = inp3 + 9
                            if inp3 in wbischop or inp3 in wqueen:
                                chkchkmate = 0
                            if inp3 in allpcs and inp3 not in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 2
                        inp3 = inp2
                        while chkchkmate == 2:
                            inp3 = inp3 + 10
                            if inp3 in wrook or inp3 in wqueen:
                                chkchkmate = 0
                            if inp3 in allpcs and inp3 not in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 3
                        inp3 = inp2
                        while chkchkmate == 3:
                            inp3 = inp3 + 11
                            if inp3 in wbischop or inp3 in wqueen:
                                chkchkmate = 0
                            if inp3 in allpcs and inp3 not in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 4
                        inp3 = inp2
                        while chkchkmate == 4:
                            inp3 = inp3 + 1
                            if inp3 in wrook or inp3 in wqueen:
                                chkchkmate = 0
                            if inp3 in allpcs and inp3 not in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 5
                        inp3 = inp2
                        while chkchkmate == 5:
                            inp3 = inp3 - 11
                            if inp3 in wbischop or inp3 in wqueen:
                                chkchkmate = 0
                            if inp3 in allpcs and inp3 not in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 6
                        inp3 = inp2
                        while chkchkmate == 6:
                            inp3 = inp3 - 10
                            if inp3 in wrook or inp3 in wqueen:
                                chkchkmate = 0
                            if inp3 in allpcs and inp3 not in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 7
                        inp3 = inp2
                        while chkchkmate == 7:
                            inp3 = inp3 - 1
                            if inp3 in wrook or inp3 in wqueen:
                                chkchkmate = 0
                            if inp3 in allpcs and inp3 not in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 8
                        inp3 = inp2
                        while chkchkmate == 8:
                            inp3 = inp3 - 9
                            if inp3 in wbischop or inp3 in wqueen:
                                chkchkmate = 0
                            if inp3 in allpcs and inp3 not in wpieces or inp3 < -20 or inp3 > 100 or inp3 in forbiddennmbrs:
                                chkchkmate = 9
                        if chkchkmate == 0:
                            print("deze zet is helaas niet mogelijk")
                            impmv = 1
                        elif chkchkmate != 0:
                            bking.remove(inp1)
                            bking.append(inp2)
                            allpcs.remove(inp1)
                            allpcs.append(inp2)
                            if inp2 in wpieces:
                                bcheck()
                        else:
                            print("move is not valid")
                            impmv = 1
                    else:
                        print("move is not valid")
                        impmv = 1
                    if impmv == 0:
                        turn = 0
                    else:
                        turn = 1

                    pcsbox = 0


                    

