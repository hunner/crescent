#pragma once

// Adapter to map crescent finger positions to zmk-helpers key labels.
//
// Crescent uses 10 keys: 4 left-hand (C R S T), 4 right-hand (A E U I),
// and 2 thumbs (Space N).
//
// Default mapping (using zmk-helpers key-label conventions):
//   Left hand top row:  C=LT4, R=LT3, S=LT2, T=LT1
//   Right hand top row: A=RT1, E=RT2, U=RT3, I=RT4
//   Left thumb:         SPACE=LH0
//   Right thumb:        N=RH0
//
// Override any position by defining CRESCENT_POS_* before including
// crescent.dtsi. For example:
//   #define CRESCENT_POS_C 0
//   #define CRESCENT_POS_R 1
//   ...

#ifndef CRESCENT_POS_C
#define CRESCENT_POS_C LT4
#endif

#ifndef CRESCENT_POS_R
#define CRESCENT_POS_R LT3
#endif

#ifndef CRESCENT_POS_S
#define CRESCENT_POS_S LT2
#endif

#ifndef CRESCENT_POS_T
#define CRESCENT_POS_T LT1
#endif

#ifndef CRESCENT_POS_SPACE
#define CRESCENT_POS_SPACE LH0
#endif

#ifndef CRESCENT_POS_N
#define CRESCENT_POS_N RH0
#endif

#ifndef CRESCENT_POS_A
#define CRESCENT_POS_A RT1
#endif

#ifndef CRESCENT_POS_E
#define CRESCENT_POS_E RT2
#endif

#ifndef CRESCENT_POS_U
#define CRESCENT_POS_U RT3
#endif

#ifndef CRESCENT_POS_I
#define CRESCENT_POS_I RT4
#endif
