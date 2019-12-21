using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        int n;
        n = Int32.Parse(Console.ReadLine());

        Dictionary<string, string> phoneBook = new Dictionary<string, string>();
        for (int i = 0; i < n; i++){
            string name_number = Console.ReadLine();

            string[] seperated = name_number.Split(' ');

            phoneBook.Add(seperated[0], seperated[1]);
        }

        List<string> names = new List<string>();
        string line;
        while ((line = Console.ReadLine()) != null) {
            names.Add(line);
        }   

        foreach (string name in names) // Loop through List with foreach
        {
            if (phoneBook.ContainsKey(name))
                Console.WriteLine(name+"="+phoneBook[name]);
            else
                Console.WriteLine("Not found");

        }
    }
}
