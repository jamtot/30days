using System.Collections.Generic;
using System.Text.RegularExpressions;
using System;

class Solution {

    static void Main(string[] args) {
        int N = Convert.ToInt32(Console.ReadLine());

        Regex nameRgx = new Regex("^[a-z]{0,20}$");
        Regex emailRgx = new Regex(@"^[a-z](\.?[a-z]){0,50}@gmail\.com$");
        List<string> nameList = new List<string>();

        for (int NItr = 0; NItr < N; NItr++) {
            string[] firstNameEmailID = Console.ReadLine().Split(' ');

            string firstName = firstNameEmailID[0];

            string emailID = firstNameEmailID[1];

            if (nameRgx.IsMatch(firstName) && emailRgx.IsMatch(emailID))
            {
                nameList.Add(firstName);
            }
        }
        nameList.Sort();
        foreach (string name in nameList){
            Console.WriteLine(name);
        }
    }
}
