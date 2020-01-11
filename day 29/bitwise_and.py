if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        # if k-1 is even, k-1 & k will equate to k-1
        # otherwise it'll be k-2
        print(k-1 if ((k-1) | k) <= n else k-2)

        """ #not fast enough
        maxUnderK = 0
        breakOut = False
        for i in range(1,n):
            for j in range(i+1, n+1):
                if (i < j):
                    i_and_j = i & j
                    if maxUnderK == k-1:
                        breakOut = True
                        break
                    elif maxUnderK < i_and_j < k:
                        maxUnderK = i_and_j      
            if breakOut:
                break
        print(maxUnderK)"""
