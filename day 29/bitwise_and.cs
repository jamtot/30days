using System;

class Solution {

    static void Main(string[] args) {
        int t = Convert.ToInt32(Console.ReadLine());

        for (int tItr = 0; tItr < t; tItr++) {
            string[] nk = Console.ReadLine().Split(' ');

            int n = Convert.ToInt32(nk[0]);

            int k = Convert.ToInt32(nk[1]);
            int maxUnderK = 0;
            for (int i = 1; i < n; i++){
                for (int j = i+1; j <= n; j++)
                if (i < j){
                    int and = i & j;
                    if (and == k-1){
                        maxUnderK = k-1;
                        goto End;
                    }
                    if (and > maxUnderK && and < k){
                        maxUnderK = and;
                    }
                }
            }
            End:
                Console.WriteLine(maxUnderK);
        }
    }
}
