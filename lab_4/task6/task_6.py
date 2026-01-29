from utils import File
import typing as tp
import collections

def queue_act(act: tp.List[str]) -> tp.List[int]:
    queue = collections.deque()
    minim = collections.deque()
    answers = []
    for a in act:
        if a == "?":
            answers.append(minim[0])
        elif a == "-":
            deleted_elem = queue.popleft()
            if deleted_elem == minim[0]:
                minim.popleft()
        else:
            elem = int(a[2:])
            queue.append(elem)

            while minim and minim[-1] > elem:
                minim.pop()
            minim.append(elem)
    return answers

def limit(commands_count: int, commands: tp.List[str]) -> bool:
    if ((1 <= commands_count <= 10**6) and (len(commands) == commands_count) and
            all(abs(int(x[2:])) <= 10**9 for x in commands if len(x) > 2)):
        return True
    else:
        return False

def queue_act_txt():
    f = File(__file__)
    data = f.read()
    commands_count = int(data[0])
    commands = data[1:]
    res = '\n'.join(map(str, queue_act(commands)))
    if limit(commands_count, commands):
        f.write(res)

if __name__ == "__main__":
    queue_act_txt()