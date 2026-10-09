# 18th github Project --> Traffic Management System
print("----------Traffic Management System----------")
import time
import os
import sys


GREEN_TIME = 10
YELLOW_TIME = 3
RED_TIME = GREEN_TIME + YELLOW_TIME


class Color:
    RED    = '\033[91m'
    YELLOW = '\033[93m'
    GREEN  = '\033[92m'
    GREY   = '\033[90m'
    CYAN   = '\033[96m'
    BOLD   = '\033[1m'
    RESET  = '\033[0m'


def light_circle(color_name, active):
    if active:
        if color_name == 'red':
            return f"{Color.RED}●{Color.RESET}"
        elif color_name == 'yellow':
            return f"{Color.YELLOW}●{Color.RESET}"
        elif color_name == 'green':
            return f"{Color.GREEN}●{Color.RESET}"
    return f"{Color.GREY}○{Color.RESET}"


def draw_intersection(phase):
    ns = {'red': False, 'yellow': False, 'green': False}
    ew = {'red': False, 'yellow': False, 'green': False}

    if phase == 'NS':
        ns['green'] = True
        ew['red']   = True
    elif phase == 'NS_YELLOW':
        ns['yellow'] = True
        ew['red']    = True
    elif phase == 'EW':
        ew['green'] = True
        ns['red']   = True
    elif phase == 'EW_YELLOW':
        ew['yellow'] = True
        ns['red']    = True

    print("\n" + "=" * 46)
    print(f"{Color.BOLD}{Color.CYAN}     🚦 TRAFFIC MANAGEMENT SYSTEM 🚦{Color.RESET}")
    print("=" * 46)

    print("\n  ┌─────────────────────────┐")
    print("  │   NORTH / SOUTH  road   │")
    print("  ├─────────────────────────┤")
    print(f"  │   RED    {light_circle('red',    ns['red'])}              │")
    print(f"  │   YELLOW {light_circle('yellow', ns['yellow'])}              │")
    print(f"  │   GREEN  {light_circle('green',  ns['green'])}              │")
    print("  └─────────────────────────┘")

    print("\n  ┌─────────────────────────┐")
    print("  │   EAST / WEST  road     │")
    print("  ├─────────────────────────┤")
    print(f"  │   RED    {light_circle('red',    ew['red'])}              │")
    print(f"  │   YELLOW {light_circle('yellow', ew['yellow'])}              │")
    print(f"  │   GREEN  {light_circle('green',  ew['green'])}              │")
    print("  └─────────────────────────┘")

    if phase == 'NS':
        print(f"\n  {Color.GREEN}▶ NORTH-SOUTH is moving (GO){Color.RESET}")
        print(f"  {Color.RED}■ EAST-WEST is stopped{Color.RESET}")
    elif phase == 'NS_YELLOW':
        print(f"\n  {Color.YELLOW}⚠ NORTH-SOUTH is slowing down (CAUTION){Color.RESET}")
        print(f"  {Color.RED}■ EAST-WEST is stopped{Color.RESET}")
    elif phase == 'EW':
        print(f"\n  {Color.GREEN}▶ EAST-WEST is moving (GO){Color.RESET}")
        print(f"  {Color.RED}■ NORTH-SOUTH is stopped{Color.RESET}")
    elif phase == 'EW_YELLOW':
        print(f"\n  {Color.YELLOW}⚠ EAST-WEST is slowing down (CAUTION){Color.RESET}")
        print(f"  {Color.RED}■ NORTH-SOUTH is stopped{Color.RESET}")

    print("\n" + "=" * 46)


def countdown(phase, seconds):
    for remaining in range(seconds, 0, -1):
        print(f"\r  ⏱️  Time left in this phase: {remaining:2d}s ", end='')
        time.sleep(1)
    print("\r" + " " * 45 + "\r", end='')


def next_phase(current):
    cycle = ['NS', 'NS_YELLOW', 'EW', 'EW_YELLOW']
    idx = cycle.index(current)
    return cycle[(idx + 1) % len(cycle)]


def phase_duration(phase):
    if phase in ('NS', 'EW'):
        return GREEN_TIME
    else:
        return YELLOW_TIME


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print(f"{Color.BOLD}{Color.CYAN}")
    print("  ████████╗██████╗  █████╗ ███████╗███████╗██╗ ██████╗")
    print("  ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██║██╔════╝")
    print("     ██║   ██████╔╝███████║█████╗  █████╗  ██║██║     ")
    print("     ██║   ██╔══██╗██╔══██║██╔══╝  ██╔══╝  ██║██║     ")
    print("     ██║   ██║  ██║██║  ██║██║     ██║     ██║╚██████╗")
    print("     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝ ╚═════╝")
    print(f"{Color.RESET}")
    print(f"  {Color.YELLOW}Beginner Traffic Management System{Color.RESET}")
    print("  Lights cycle automatically: Green → Yellow → other road\n")
    print(f"  {Color.GREY}Press Ctrl+C to exit.{Color.RESET}\n")

    input("  Press ENTER to start the simulation...")

    phase = 'NS'

    try:
        while True:
            clear_screen()
            draw_intersection(phase)
            duration = phase_duration(phase)
            countdown(phase, duration)
            phase = next_phase(phase)

    except KeyboardInterrupt:
        print(f"\n\n  {Color.CYAN}Simulation stopped. Drive safely! 🚗{Color.RESET}\n")
        sys.exit(0)


if __name__ == "__main__":
    main()