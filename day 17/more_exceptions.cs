using System;

public class NegativeException : Exception
{
    public NegativeException() : base("n and p should be non-negative"){}
}

class Calculator{
    public int power(int n, int p)
    {        
        return IntPow(n, p);
    }

    private int IntPow(int x, int pow)
    {
        if (x < 0 || pow < 0){
            throw new NegativeException();
        }
        else if (pow == 0) return 1;
        else if (pow == 1) return x;
        
        int powered = 1;
        for (int i = 0; i < pow; i++){
            powered*=x; 
        }
        return powered;
    }
}

class Solution{
    static void Main(String[] args){
        Calculator myCalculator=new  Calculator();
        int T=Int32.Parse(Console.ReadLine());
        while(T-->0){
            string[] num = Console.ReadLine().Split();
            int n = int.Parse(num[0]);
            int p = int.Parse(num[1]); 
            try{
                int ans=myCalculator.power(n,p);
                Console.WriteLine(ans);
            }
            catch(Exception e){
               Console.WriteLine(e.Message);

            }
        }
    }
}
