#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <ctype.h>
#include <math.h>
#include <signal.h>
typedef unsigned int            uint32_t;

uint32_t reverseBits(uint32_t n) {
    uint32_t temp = 0;
    for (int i = 0; i < 31; i++) {
        if (n & 1 == 1) {
            temp = temp | 1;
        }
        n = n >> 1;
        temp = temp << 1;
    }
    temp = n | temp;
    return temp;
}