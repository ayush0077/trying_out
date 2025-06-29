** start of main.py **

def hanoi_solver(n):
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []

    moves = []

    # record starting state
    moves.append(f"{source} {auxiliary} {target}")

    def move(num, src, dst, aux):
        if num == 0:
            return
        
        move(num - 1, src, aux, dst)

        # move top disk
        dst.append(src.pop())

        # record state
        moves.append(f"{source} {auxiliary} {target}")

        move(num - 1, aux, dst, src)

    move(n, source, target, auxiliary)

    return "\n".join(moves)


** end of main.py **

