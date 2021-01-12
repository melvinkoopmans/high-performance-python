#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <stdlib.h>
#include <pthread.h>

using namespace std;

#define NUM_THREADS 16

struct thread_data {
    int thread_id;
    vector<int> *a;
    vector<int> *b;
    int start;
    int end;
};

void add_normal(vector<int> &a, vector<int> &b, int start, int end)
{
    for (int i = start; i <= end; i++) {
        a[i] = a[i] + b[i];
    }
}

void *print_hello(void *threadarg) {
    struct thread_data *my_data;
    my_data = (struct thread_data *) threadarg;
    add_normal(*my_data->a, *my_data->b, my_data->start, my_data->end);
    pthread_exit(NULL);
}

int main()
{
    srand (time(NULL));
    int i;
    int N = 1000000;
    int rc;
    struct thread_data td[NUM_THREADS];
    
    vector<int> a;
    vector<int> b;

    for (i=0; i<N; i++) {
        // Add random number between 1 and 10.
        a.push_back(rand() % 10 + 1);
        b.push_back(rand() % 10 + 1);
    }

    cout << a[0] << " + " << b[0] << " = ?" << endl;
    cout << a[a.size() - 1] << " + " << b[a.size() - 1] << " = ?" << endl;

    pthread_t threads[NUM_THREADS];
    int chunk_size = N / NUM_THREADS;

    auto start = chrono::steady_clock::now();

    for (i=0; i < NUM_THREADS; ++i) {
        td[i].thread_id = i;
        td[i].start = i * chunk_size;
        td[i].end = td[i].start + chunk_size;
        td[i].a = &a;
        td[i].b = &b;

        rc = pthread_create(&threads[i], NULL, print_hello, (void *)&td[i]);
    }

    for (i=0; i < NUM_THREADS; ++i) {
        pthread_join(threads[i], NULL);
    }

//    add_normal(a, b);
    auto end = chrono::steady_clock::now();

    cout << "Elapsed time in nanoseconds: " << (end - start).count() << "\n\n";

    cout << a[0] << endl;
    cout << a[a.size() - 1] << endl;
    
    return 0;
}
