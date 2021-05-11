//
//  Mochio.cpp
//  Mochio
//
//  Created by mochi on 5/5/21.
//
#include <random>
#include "Mochio.hpp"

void seed() {
    static bool need_to_seed = true;
    if (need_to_seed) {
        srand( (unsigned int)time(NULL) ); // seed the generator
        need_to_seed = false;
    }
}

int Mochio::random(int min, int max) {
    seed();
    return rand() % (max-min + 1) + min; // generate
}

int* Mochio::randoms(int length, int min, int max) {
    seed();
    int * nums = new int[length];
    for (int i=0; i<length; i++) {
        nums[i] = random(min, max);
    }
    return nums;
}
