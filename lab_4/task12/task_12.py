from utils import File
import typing as tp

class Soldier:
    def __init__(self, num: int):
        self.num = num
        self.left = None
        self.right = None

def formation_commands(n: int, m: int, commands: tp.List[str]) -> tp.List[str]:
    soldiers = [Soldier(i) for i in range(n + 1)]
    in_formation = [False] * (n + 1)
    # Начальное состояние: только солдат 1 в строю
    in_formation[1] = True
    answers = []
    for cmd in commands:
        parts = cmd.split()
        action = parts[0]
        if action == "left":
            i, j = int(parts[1]), int(parts[2])
            if not in_formation[i] and in_formation[j]:
                current = soldiers[j]
                new_soldier = soldiers[i]
                new_soldier.right = current
                new_soldier.left = current.left
                if current.left:
                    current.left.right = new_soldier
                current.left = new_soldier
                in_formation[i] = True

        elif action == "right":
            i, j = int(parts[1]), int(parts[2])
            if not in_formation[i] and in_formation[j]:
                current = soldiers[j]
                new_soldier = soldiers[i]
                new_soldier.left = current
                new_soldier.right = current.right
                if current.right:
                    current.right.left = new_soldier

                current.right = new_soldier
                in_formation[i] = True
        elif action == "leave":
            i = int(parts[1])
            if in_formation[i]:
                soldier = soldiers[i]
                if soldier.left:
                    soldier.left.right = soldier.right
                if soldier.right:
                    soldier.right.left = soldier.left
                soldier.left = None
                soldier.right = None
                in_formation[i] = False
        elif action == "name":
            i = int(parts[1])
            soldier = soldiers[i]
            left_neighbor = soldier.left.num if soldier.left else 0
            right_neighbor = soldier.right.num if soldier.right else 0
            answers.append(f"{left_neighbor} {right_neighbor}")
    return answers

def limit(n: int, m: int, commands: tp.List[str]) -> bool:
    if (1 <= n <= 75000) and (1 <= m <= 75000) and (len(commands) == m):
        for cmd in commands:
            parts = cmd.split()
            if len(parts) < 2:
                return False
            action = parts[0]
            if action in ["left", "right"]:
                if len(parts) != 3:
                    return False
                i, j = int(parts[1]), int(parts[2])
                if not (1 <= i <= n) or not (1 <= j <= n):
                    return False
            elif action in ["leave", "name"]:
                if len(parts) != 2:
                    return False
                i = int(parts[1])
                if not (1 <= i <= n):
                    return False
            else:
                return False
        return True
    else:
        return False

def format_txt():
    f = File(__file__)
    data = f.read()
    n, m = map(int, data[0].split())
    commands = data[1:m + 1]

    if limit(n, m, commands):
        res = formation_commands(n, m, commands)
        answer = "\n".join(res)
        f.write(answer)

if __name__ == "__main__":
    format_txt()