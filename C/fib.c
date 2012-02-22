/*
   Fibonacci-Zahlen
   in C
   Wolfgang.Urban@schule.at
*/

#include <stdio.h> /* Ein-Ausgabe */

int fib1(int);
int fib1a(int);
int fib3(int);
int fib4(int,int,int);


/* Hauptprogramm */

int main() {
        printf("Alg. 1 : %d\n",fib1(10));
        printf("Alg. 4 : %d\n",fib4(10,1,1));
}

/* Algorithmus 1 */

int fib1(int n) {
        if (n<=2) return 1;
        else return fib1(n-1)+fib1(n-2);
}

/* Algorithmus 1a */

int fib1a(int n) {
        if (n<=2) return 1;
        return fib1a(n-1)+fib1a(n-2);
}

/* Algorithmus 3 */

int fib3(int n) {
        int a,b,neu;
        int zaehler;

        if (n<=2) return 1;
        a = 1;
        b = 1;
        for (zaehler=3; zaehler<=n; zaehler++)
        {
                neu = a+b;
                a = b;
                b = neu;
        }
        return neu;
}

/* Algorithmus 4 */

int fib4(int n, int a, int b) {
        if (n==1) return a;
        if (n==2) return b;
        return fib4(n-1,b,a+b);
}

