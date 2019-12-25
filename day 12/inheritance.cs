using System;
using System.Linq;

class Person{
	protected string firstName;
	protected string lastName;
	protected int id;
	
	public Person(){}
	public Person(string firstName, string lastName, int identification){
			this.firstName = firstName;
			this.lastName = lastName;
			this.id = identification;
	}
	public void printPerson(){
		Console.WriteLine("Name: " + lastName + ", " + firstName + "\nID: " + id); 
	}
}

class Student : Person{
    private int[] testScores;  
  
    public Student(string firstName, string lastName, 
        int identification, int[] scores) : 
    base(firstName, lastName, identification) {
        this.testScores = scores;
    }

    public char Calculate()
        {
            int sum = 0;
            int count = 0;
            foreach (int num in testScores)
            {
                count++;
                sum += num;
            }
            int average = sum/count;
            char grade = 'T';
            if (average >= 90)
                    grade = 'O';
            else if (average >= 80)
                    grade = 'E';
            else if (average >= 70)
                    grade = 'A';
            else if (average >= 55)
                    grade = 'P';
            else if (average >= 40)
                    grade = 'D';

            return grade;
        }
}

class Solution {
	static void Main() {
		string[] inputs = Console.ReadLine().Split();
		string firstName = inputs[0];
	  	string lastName = inputs[1];
		int id = Convert.ToInt32(inputs[2]);
		int numScores = Convert.ToInt32(Console.ReadLine());
		inputs = Console.ReadLine().Split();
	  	int[] scores = new int[numScores];
		for(int i = 0; i < numScores; i++){
			scores[i]= Convert.ToInt32(inputs[i]);
		} 
	  	
		Student s = new Student(firstName, lastName, id, scores);
		s.printPerson();
		Console.WriteLine("Grade: " + s.Calculate() + "\n");
	}
}
