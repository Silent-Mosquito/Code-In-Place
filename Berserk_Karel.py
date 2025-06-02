from karel.stanfordkarel import *

def main():
    while front_is_clear():
        while front_is_clear():
            if random(0.5):
                if no_beepers_present():
                    put_beeper()
            move()
            if random(0.5):
                if beepers_present():
                    pick_beeper()
            if random(0.5):
                turn_left()
                if random(0.5):
                    turn_left()
                    if random(0.5):
                        turn_left()
                        if random(0.5):
                            turn_left()
        turn_left()
        turn_left()

if __name__ == '__main__':
    main()
