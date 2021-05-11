//
//  Mochio.hpp
//  Mochio
//
//  Created by mochi on 5/5/21.
//

#ifndef Mochio_hpp
#define Mochio_hpp

#include <stdio.h>

class Mochio {
    //
    
public:
    static int random(int min = 0, int max = 100);
    static int* randoms(int length, int min = 0, int max = 100);
};

#endif /* Mochio_hpp */
