using namespace std;
#include <iostream>

class Person{
    public:
        int age;
        Person(int initialAge);
        void amIOld();
        void yearPasses();
    };

    Person::Person(int initialAge){
        if (initialAge < 0) {
            cout << "Age is not valid, setting age to 0." << endl;
            age = 0;
        }
        else age = initialAge;
    }

    void Person::amIOld(){
        cout << "You are ";
        if (age < 13)
            cout << "young." << endl;
        else if (age < 18)
            cout << "a teenager." << endl;
        else cout << "old." << endl;
    }

    void Person::yearPasses(){
        age++;
    }

int main(){
    int t;
	int age;
    cin >> t;
    for(int i=0; i < t; i++) {
    	cin >> age;
        Person p(age);
        p.amIOld();
        for(int j=0; j < 3; j++) {
        	p.yearPasses(); 
        }
        p.amIOld();
      
		cout << '\n';
    }

    return 0;
}
