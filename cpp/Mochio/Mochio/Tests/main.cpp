//
//  main.cpp
//  Mochio
//
//  Created by mochi on 5/5/21.
//

#include <iostream>
#include "../Mochio.hpp"

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    
    int *randoms = Mochio::randoms(10);
    for (int i=0; i<10; i++) {
        cout << randoms[i] << " " ;
    }
    cout << endl;
    
    cout << Mochio::random() << endl;
    
    return 0;
}
