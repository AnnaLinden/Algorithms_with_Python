# Write a function that recursively solves the Tower of Hanoi game
def tower_of_hanoi(count, stacks=None, source=0, auxiliary=1, destination=2, moves=0):
    if not stacks:
        stacks = [['ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i] for i in range(count-1, -1, -1)], [], []]
        moves = 1
        print(stacks)
    # COMPLETE FROM HERE
    if count == 1:
        stacks[destination].append(stacks[source].pop())  # Move the disk
        print(stacks)
        return moves + 1  # Return the number of moves, incremented by this move
    else:
        # Move n-1 disks from source to auxiliary
        moves = tower_of_hanoi(count - 1, stacks, source, destination, auxiliary, moves)
        # Move the nth disk from source to destination
        stacks[destination].append(stacks[source].pop())
        print(stacks)
        moves += 1
        # Move n-1 disks from auxiliary to destination
        moves = tower_of_hanoi(count - 1, stacks, auxiliary, source, destination, moves)
        return moves


# Example usage:
# print(tower_of_hanoi(3))