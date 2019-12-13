using System;
using System.Collections.Generic;
using System.IO;

class Solution {
    static void Main(String[] args) {
        int i = 4;
        double d = 4.0;
        string s = "HackerRank ";
        
        // Declare second integer, double, and String variables.
        int i2;
        double d2;
        string s2;

        // Read and save an integer, double, and String to your variables.
        string userInput = Console.ReadLine();
        i2 = Convert.ToInt32(userInput);
        userInput = Console.ReadLine();
        d2 = Convert.ToDouble(userInput);
        s2 = Console.ReadLine();

        // Print the sum of both integer variables on a new line.
        Console.WriteLine(i+i2);

        // Print the sum of the double variables on a new line.
        string dS = string.Format("{0:N1}", d+d2);
        Console.WriteLine(dS);
        
        // Concatenate and print the String variables on a new line
        // The 's' variable above should be printed first.
        Console.WriteLine(s +  s2);
    }
}
