using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        List<int> returned = new List<int>( 
            Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse) );
        List<int> expected = new List<int>( 
            Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse) );

        if (returned[2] > expected[2]) 
            Console.WriteLine(10000);
        else if ( (expected[0] >= returned[0] && expected[1] >= returned[1]) 
                || expected[2] > returned[2]) 
            Console.WriteLine(0);
        else if (expected[0] < returned[0] && expected[1] == returned[1])
            Console.WriteLine(15*(returned[0]-expected[0]));
        else 
            Console.WriteLine(500*(returned[1]-expected[1]));
    }
}
