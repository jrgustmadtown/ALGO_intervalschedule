import sys

def parse_input(idx, inputy):
    jobs = []

    for _ in range(inputy[idx]):
        idx += 1
        i, j = inputy[idx].split()
        jobs.append([i, j])

    sorted_jobs = sorted(jobs, key=lambda pair: pair[1])

    return idx, sorted_jobs

def finish_first(jobs):
    scheduled = 0
    for _ in jobs:
        scheduled += 1
        s, f = _.split()
        for _ in jobs:
            i, j = _.split()
            if f <= j and i < f:
                jobs.remove(_)
    return scheduled

def main():
    inputy = sys.stdin.read().splitlines()
    outputy = []
    insts = int(inputy[0])
    idx = 1
    for _ in range(insts):
        idx, sorted_jobs = parse_input(idx, inputy)
        outputy.append(finish_first(sorted_jobs))
    for _ in outputy:
        print(_ + "\n")



