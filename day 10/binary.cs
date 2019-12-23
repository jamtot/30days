using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Solution {

    static string get_binary(int n)
    {
        string binary = "";
        while (n > 0)
        {
            binary = (n%2).ToString()+binary;
            n = n / 2;
        }    
        return binary;
    }

    static int get_consec(string binary)
    {

        int max_consec = 0;
        int cur_count = 0;
        for (int i = 0; i < binary.Length; i++)
        {
            if (binary[i] == '1'){
                cur_count += 1;
                if (max_consec < cur_count)
                    max_consec = cur_count;
            }
            else
                cur_count = 0;
        }

        return max_consec;
    }

    static void Main(string[] args) {
        int n = Convert.ToInt32(Console.ReadLine());
        string bin = get_binary(n);
        int max_consec = get_consec(bin);
        Console.WriteLine(max_consec);
    }
}
