import sys

def parse_input(idx, inputy):
    jobs = []
    numjobs = int(inputy[idx])
    idx += 1
    for _ in range(numjobs):
        i, j = inputy[idx].split()
        jobs.append([int(i), int(j)])
        idx += 1
    sorted_jobs = sorted(jobs, key=lambda pair: pair[1])
    return idx, sorted_jobs

def finish_first(jobs):
    scheduled = 0
    latest = -float("inf")
    for s, f in jobs:
        if s >= latest:
            scheduled += 1
            latest = f
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
        print(_)

if __name__ == "__main__":
    main()


