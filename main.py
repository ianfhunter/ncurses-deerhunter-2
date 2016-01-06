# coding: utf-8
import curses,time,random

def draw_ascii(window,ascii_art,x,y,attr):
    for line_idx, line in enumerate(ascii_art.splitlines()):
        window.addstr(line_idx + y, x, line,attr)

def getRuleforNumber(num):
    rules = [
        ["Red, Odd, Lower, Prime","!Blue, Odd, Lower, Prime"],
        ["!Red, Even, Upper, Prime","!Blue, Even, Upper, Prime","Green, Even, Upper, Prime"],
        ["Red, Odd, Upper, Prime, Right","!Green, Odd, Upper, Prime, Right"],
        ["Red. Even, Lower, !Prime","!Blue. Even, Lower, !Prime","!Green. Even, Lower, !Prime"],
        ["Red,Odd, Upper, Prime, Left","!Green, Odd, Upper, Prime, Left"],
        ["Blue, Even, Upper,!Prime","!Green, Even, Upper,!Prime"],
        ["!Red, Odd, Lower, Prime","Green, Odd, Lower,Prime"],
        ["!Blue, Even, Upper, !Prime","Green, Even, Upper, !Prime"],
        ["!Red, Odd, Lower, !Prime","Blue, Odd, Lower,!Prime"],
    ]
    subset = rules[num -1]
    return subset[random.randint(0, len(subset) -1)]

def kbhit(window,char,no):
    ch = window.getch();
    if ch == -1:
        return 0

    nch = int(str(chr(ch)))

    if (nch == char or nch in no):
        if (nch == char):
            curses.ungetch(ch)
            return 1
        else:
            return 2
    else:
        return 0

def fn(curWin,mainWin):  
    desired = random.randint(1, 9)
    rule = getRuleforNumber(desired)
    undesired = [1,2,3,4,5,6,7,8,9]
    undesired.remove(desired)
    while(True):
        curWin.clear()
        curWin.border(0)
        curWin.addstr(1, 1,rule)  
#        curWin.addstr(3, 1,str(undesired))  
        curWin.addstr(8, 1,"Enter Select (Num):")   
        curWin.refresh()
        time.sleep(0.3)
        pressed = kbhit(mainWin,desired,undesired)
        if pressed == 1:
            return True
        if pressed == 2:
            return False

body = '''
                ,/  \.
               |(    )|
          \`-._:,\  /.;_,-'/
           `.\_`\')(`/'_/,'
               )/`.,'\(
               |.    ,|
   \           :6)  (6;           /
    \           \`\ /`/          /
     \       /   \._';   \      /
 \    \ ______________________ /    /
  \    /                      \    /
   \  /                        \  /
    \/                          \/
    /                            \ 
    |                            |
    |                            |
    |                            |
    |                            |
    |                            |
    |                            |
    |                            |
    |                            |
    |                            |
    |                            |
    |                            |
    |                            | 
    |                            |
    |                            |
    |                            | 
    |                            |
    |                            | 
    |                            |
    |                            |
   /\                           /\ 
  /  \                         /  \  
 /   /\                       /\   \ 
    /  \_____________________/  \ 
'''

spleen = '''
    ||
   /  \_
  /   1 \ 
 /       \ 
 \___/\__/
'''
heart = '''
,d88b.d88b,
8         8
`Y   3   Y'
  `Y   Y'  
    `Y'  
'''

thing = '''
   \ | /
 '-.;;;.-'
-==; 2 ;==-
 .-';;;'-.
   / | \ 
'''

mon = '''
    __
 .'`  _\ 
/    / 
|   |
| 4 |
\    \_
 '.____\  
'''
sta = '''
    .
 __.'.__
'-. 5 .-'
  /.'.\ 
  '   '
'''

new = '''
   _
 \/ \/ 
 / 6 \ 
 \   / 
 /\_/\ 
'''

worm = '''
                    /)
 .-""--.....__...,-'/
( 7("""`----......--'
 `. `._
   `-. `-._
      `.///`-._ 
        "`--.__)
'''

other = '''
  ,
  )\ 
 /  \ 
|  8 |
\___/ 
'''

other2 = '''
     __
    /  \ 
    \  /
 .--.\/.--.
|     9    |
 '--'/\\'--'
    /  \ 
    \__/
'''

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)
stdscr.keypad(1)

curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)


stdscr.border(0)
stdscr.refresh()

dWidth = 40
dHeight = 40

#lines, columns,  beginX, beginY
dwin = curses.newwin(dHeight, dWidth, 1,1)
hintwin = curses.newwin(dWidth,40, 1,dWidth + 1)

dwin.clear()
dwin.border(0)
draw_ascii(dwin,body,1,0,curses.color_pair(1)) #border of 1
draw_ascii(dwin,spleen,23,24,curses.color_pair(1)) 
draw_ascii(dwin,heart,20,11,curses.color_pair(1)) 
draw_ascii(dwin,thing,8,11,curses.color_pair(4)) 
draw_ascii(dwin,mon,7,28,curses.color_pair(1))
draw_ascii(dwin,sta,7,16,curses.color_pair(1))
draw_ascii(dwin,new,18,16,curses.color_pair(3))
draw_ascii(dwin,worm,6,21,curses.color_pair(4))
draw_ascii(dwin,other,27,15,curses.color_pair(4))
draw_ascii(dwin,other2,16,28,curses.color_pair(3))
dwin.refresh()

# Power Bars
hintwin.border(0)
hintwin.refresh()


stdscr.nodelay(1)
res = fn(hintwin,stdscr)

dwin.addstr(1, 1,"Result is" + str(res))   
dwin.refresh()
time.sleep(3)



curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()