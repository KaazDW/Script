#include <iostream>
#include <time.h>
#include <cstring>
using namespace std;

void randomchar(int n) {
	char tabrand[63] = {"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"};
	char m;
	cout << ">   ";
	for (int i = 0; i < n; i++) {
		m = rand() % 62;
		cout << tabrand[m];
	}
	cout << endl;
}

int main() {

	srand(time(NULL));
	int n;
	int N;
	bool continuer = true;

	do{
		cout << "simple PASSWORD GENERATOR by KAAZDW";
		cout << endl <<endl<<"Nombre de caracteres / Nombre de Mots de Passe  " << endl;
		cin >> n;
		cin >> N;
		for (int i = 0; i < N; i++) {
			randomchar(n);
		}
	} while (continuer = true);

	return 0;
}