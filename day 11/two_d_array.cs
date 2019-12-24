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

    static int getHourGlassSum(int[][] arr, int startX, int startY)
    {
        int size = 3;
        int sum = 0;
        for (int i = 0; i < size; i++){
            for (int j = 0; j < size; j++){
                
                if (j == 1){
                    if (i == 1)
                    {
                        sum += arr[j+startY][i+startX];
                    }
                }
                else{
                    sum += arr[j+startY][i+startX];
                }
            }
        }
        return sum;
    }

    static void Main(string[] args) {
        int[][] arr = new int[6][];

        for (int i = 0; i < 6; i++) {
            arr[i] = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp));
        }

        int max = Int32.MinValue;
        const int LIMIT = 4;
        for (int i = 0; i < LIMIT; i++)
        {
            for (int j =0; j < LIMIT; j++)
            {
                int cur = getHourGlassSum(arr, i, j);
                if (cur > max){
                    max = cur;
                }
            }
        }

        Console.WriteLine(max);
    }
}
