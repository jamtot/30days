#include <iostream>
#include <vector>

using namespace std;


class Person{
	protected:
		string firstName;
		string lastName;
		int id;
	public:
		Person(string firstName, string lastName, int identification){
			this->firstName = firstName;
			this->lastName = lastName;
			this->id = identification;
		}
		void printPerson(){
			cout<< "Name: "<< lastName << ", "<< firstName <<"\nID: "<< id << "\n"; 
		}
	
};

class Student :  public Person{
	private:
		vector<int> testScores;  
	public:
        Student(string firstName, string lastName, int identification, vector<int> scores) : Person(firstName, lastName, identification){
            this->testScores = scores;
        }

        char calculate()
        {
            int sum = 0;
            int count = 0;
            vector<int>::iterator iter = testScores.begin();
            for (; iter != testScores.end(); ++iter)
            {
                count++;
                sum += *iter;
            }
            int average = sum/count;
            char grade;
            switch(average){
                case 90 ... 100:
                    grade = 'O';
                    break;
                case 80 ... 89:
                    grade = 'E';
                    break;
                case 70 ... 79:
                    grade = 'A';
                    break;
                case 55 ... 69:
                    grade = 'P';
                    break;
                case 40 ... 54:
                    grade = 'D';
                    break;
                case 0 ... 39:
                    grade = 'T';
                    break;
            }
            return grade;
        }
};

int main() {
	string firstName;
  	string lastName;
	int id;
  	int numScores;
	cin >> firstName >> lastName >> id >> numScores;
  	vector<int> scores;
  	for(int i = 0; i < numScores; i++){
	  	int tmpScore;
	  	cin >> tmpScore;
		scores.push_back(tmpScore);
	}
	Student* s = new Student(firstName, lastName, id, scores);
	s->printPerson();
	cout << "Grade: " << s->calculate() << "\n";
	return 0;
}
