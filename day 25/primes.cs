using System;
using System.Collections.Generic;
using System.IO;
class Solution {

    static string simpleCheck(int n){
        if (n == 2) return "Prime";
        else if (n < 2 || n%2==0) return "Not prime";
        for (int i = 3; i*i <= n; i+=2){
            if (n%i==0) return "Not prime";
        }
        return "Prime";
}

    static void Main(String[] args) {
        int T = Convert.ToInt32(Console.ReadLine());
        for (int i = 0; i < T; i++){
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(simpleCheck(n));
        }
    }
}
