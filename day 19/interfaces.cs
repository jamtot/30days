using System;
public interface AdvancedArithmetic{
    int divisorSum(int n);
}

public class Calculator : AdvancedArithmetic
{
    public int divisorSum(int n)
    {
        int sum = 0;
        for (int i = 1; i <= Math.Sqrt(n); i++){
            if (n%i == 0){
                if (n/i == i)
                    sum+=i;
                else
                    sum+=i+n/i;
            }
        }
        return sum;
    }
}

class Solution{
    static void Main(string[] args){
        int n = Int32.Parse(Console.ReadLine());
      	AdvancedArithmetic myCalculator = new Calculator();
        int sum = myCalculator.divisorSum(n);
        Console.WriteLine("I implemented: AdvancedArithmetic\n" + sum); 
    }
}
