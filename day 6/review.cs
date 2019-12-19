using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        int n;
        n = Convert.ToInt32(Console.ReadLine());

        for (int i = 0; i < n; i++){
            string input;
            input = Console.ReadLine();
            string even = "";
            string odd = "";
            for (int j = 0; j < input.Length; j++)
            {
                if (j%2==1){
                    odd+=input[j];
                } else {
                    even+=input[j];
                }
            }
            Console.WriteLine(even+" "+odd);
        }
    }
}


