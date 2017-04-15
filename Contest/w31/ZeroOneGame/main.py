
# Link : https://www.hackerrank.com/contests/w31/challenges/zero-one-game

import sys
# 
# sys.stdin = open('test1.in','r')
# sys.stdout = open('test1.out','w')



def main():
    k = int(sys.stdin.readline().rstrip())
    for i in range(k):
        n = int(sys.stdin.readline().rstrip())
        arr = [int(m) for m in sys.stdin.readline().rstrip().split(' ')]
        turn = 0 # Alice
        j=0
        while j < n-2:
            if(arr[j] == 0 and arr[j+2]==0):
                del arr[j+1]
                n -= 1
                j -= 1
                if j<0:
                    j = 0
                if(turn == 1):
                    turn = 0
                else:
                    turn = 1
            else:
                j += 1

        if turn == 0:
            sys.stdout.write('Bob')
        else:
            sys.stdout.write('Alice')
        if(i < k-1):
            sys.stdout.write('\n')





main()
