#include <iostream>
using namespace std;

string alphabet = "abcdefghijklmnopqrstuvwxyz ";
string match = "tommy";
string best = "";
int maxScore = -1;

void makeString() 
{
    string s = "";
    int score = 0;
    for (int i = 0; i < match.length(); i++) {
        int r = rand() % 27;
        s += alphabet.substr(r,1);
        if (match.substr(i,1) == alphabet.substr(r,1)) {
            score++;
        }
    }
    if (score > maxScore) {
        maxScore = score;
        best = s;
    }
}

int main() 
{
    int i = 1;
    while (best != match) {
        makeString();
        if (i%1000 == 0) {
            cout << i << " " << best << " (" << maxScore << ")\n";
        }
        i++;
    }
    cout << i << " " << best << "\n";
    cout << "DONE!";
    return 0;
}
