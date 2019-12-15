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

    static string weird(int n)
    {
        if (n%2==1 || (n > 5 && n < 21))
            return "Weird";
        else
            return "Not Weird";
    }

    static void Main(string[] args) {
        int N = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine(weird(N));
    }
}
