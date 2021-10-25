#!/usr/bin/python3
""" doc """
import sys
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = eval(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)
if (N < 4):
    print('N must be at least 4')
    exit(1)
Grid = [[0]*N for _ in range(N)]
Nq = [N]
solution = []


def attack(i, j):
    """ doc """
    for k in range(N):
        if Grid[i][k] == 1 or Grid[k][j] == 1:
            return True
    for k in range(N):
        for z in range(N):
            if (k + z == i + j) or (k - z == i - j):
                if Grid[k][z] == 1:
                    return True
    return False


def Nqueens(n, x):
    """ doc """
    for i in range(x, N):
        for j in range(N):
            if (not(attack(i, j))) and (Grid[i][j] != 1):
                Grid[i][j] = 1
                Nq[0] = Nq[0] - 1
                Nqueens(n - 1, i + 1)
                if Nq[0] == 0:
                    position()
                Grid[i][j] = 0
                Nq[0] = Nq[0] + 1
    return False


def reset(N):
    """ doc """
    for k in range(N):
        for z in range(N):
            Grid[k][z] = 0


def validate(N):
    """ doc """
    suma = 0
    store = []
    for k, i in enumerate(Grid):
        if 1 in i:
            store.append([k, i.index(1)])
            suma += 1
    if suma == N:
        return store
    else:
        return []


def position():
    """ doc """
    x = validate(N)
    if len(x) == N and x not in solution:
        print(x)
        solution.append(x)


Nqueens(N, 0)
