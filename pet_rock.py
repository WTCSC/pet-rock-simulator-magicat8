import sys

def clamp(value, minimum=0, maximum=10):
    return max(minimum, min(maximum, value))

def print_stats(name, stats):
    print(f"--- Your Pet Rock, {name} ---")
    print(f"Happiness: {stats['happiness']}/10")
    print(f"Hunger: {stats['hunger']}/10")
    if 'energy' in stats:
        print(f"Energy: {stats['energy']}/10")

def game_over_reason(stats):
    if stats.get('health', 1) <= 0:
        return "Your pet rock disinigrated."
    if stats['hunger'] >= 10:
        return "Your pet rock got too hungry and its stomach imploded."
    if stats['happiness'] <= 0:
        return "Your pet rock got too sad and ran away."
    if stats.get('energy', 1) <= 0:
        return "Your pet rock ran out of energy and couldn't stay awake."
    return "The game has ended."

def main():
    name = input("What will you name your pet rock? ").strip()
    if not name:
        name = "Rocky"
    stats = {
        'happiness': 5,
        'hunger': 5,
        'energy': 5,
        'health': 10,
    }
    turn = 0
    while True:
        print()
        print_stats(name, stats)
        print()
        print("What do you want to do?")
        print("  1. Feed the rock")
        print("  2. Play with the rock")
        print("  3. Do nothing")
        print("  4. Quit")
        choice = input("Your choice: ").strip()
        action_desc = ""
        if choice == '1':
            stats['hunger'] -= 2
            stats['happiness'] -= 1
            stats['energy'] += 1
            action_desc = "You fed your rock."
        elif choice == '2':
            if stats['energy'] <= 1:
                action_desc = "Your rock is too tired to play."
                stats['happiness'] -= 1
            else:
                stats['happiness'] += 2
                stats['hunger'] += 1
                stats['energy'] -= 2
                action_desc = "You played with your rock. It seemed pleased."
        elif choice == '3':
            stats['happiness'] -= 1
            stats['hunger'] += 1
            stats['energy'] += 1
            action_desc = "You did nothing. Time passes..."
        elif choice == '4' or choice.lower() in ('q', 'quit'):
            print()
            print("You chose to stop caring for your rock.")
            break
        else:
            action_desc = "Your rock looks confused by that choice."
        stats['happiness'] = clamp(stats['happiness'])
        stats['hunger'] = clamp(stats['hunger'])
        stats['energy'] = clamp(stats['energy'])
        stats['health'] = clamp(stats['health'], 0, 999)
        print()
        print(action_desc)
        stats['hunger'] += 1 
        stats['happiness'] -= 1 
        if stats['hunger'] >= 8:
            stats['health'] -= 2
        if stats['happiness'] <= 2:
            stats['health'] -= 1
        stats['happiness'] = clamp(stats['happiness'])
        stats['hunger'] = clamp(stats['hunger'])
        stats['energy'] = clamp(stats['energy'])
        stats['health'] = clamp(stats['health'], 0, 999)
        turn += 1
        if stats['hunger'] >= 10 or stats['happiness'] <= 0 or stats.get('health', 1) <= 0 or stats.get('energy', 1) <= 0:
            print()
            print(game_over_reason(stats))
            print("GAME OVER")
            break
    if choice == '4':
        print("Thanks for playing. Your rock rests peacefully.")


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        print("Goodbye!")
        sys.exit(0)
