int fib(int N)
{
    if (N == 0) {
        return 0;
    }

    int fibo[3];
    fibo[0] = 0;
    fibo[1] = 1;
    fibo[2] = 1;
    
    for (int i = 2; i < N; i++) {
        fibo[0] = fibo[1];
        fibo[1] = fibo[2];
        fibo[2] = fibo[0] + fibo[1];
    }
    return fibo[2];
}