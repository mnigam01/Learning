#include <bits/stdc++.h>
using namespace std;

int main(){
    int a = 24567892;
    int b = 100000000;
    b = -b;
    int c;
    while (a){
        c = a^b;
        a = (a&b)<<1;
        b = c;
    }
    cout<<b<<endl;
    return 0;
}