from utils import File
import typing as tp

def queue_act(a: list[str]) -> tp.List[str]:
    queue = []
    head = 0
    deleted_elements = []
    for i in a:
        if i == "-":
            deleted_elements += [queue[head]]
            head += 1
        else:
            elem = i[2:]
            queue += [elem]
    return deleted_elements

def limit(act_count: int, act: tp.List[str]) -> bool:
    if (1 <= act_count <= 10**6) and (len(act) == act_count):
        return True
    else:
        return False

def queue_act_txt():
    f = File(__file__)
    arguments = f.read()
    act_count = int(arguments[0])
    actions = arguments[1:]
    if limit(act_count, actions):
        res = queue_act(actions)
        f.write('\n'.join(res))

if __name__ == "__main__":
    queue_act_txt()