#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#define MAX 10000

void shell_sort(int *vetor, int tam);

int main()
{
    double tempo = 0.0;
    clock_t begin = clock();
    FILE *p;
    int i;
    int vet[MAX];

    p = fopen("o10000.txt", "r");
    if (p == NULL){
    printf("nao foi possivel abrir o arquivo");
    return 1;
    }

    for (i = 0; i < MAX; i++)
    {
        fscanf(p, "%d", &vet[i]);
        if(feof(p)){
            break;
        }
    }
    fclose(p);

    shell_sort(vet, MAX);

    printf("Valores ordenados\n");
    for (i = 0; i < MAX; i++)
    {
        printf("%d\n", vet[i]);
    }

    clock_t end = clock();
    tempo += (double)(end - begin) / CLOCKS_PER_SEC;
 
    printf("Tempo gasto: %f segundos \n", tempo);
    system("pause");
    return 0;
}

void shell_sort(int *vet, int size) {
    int i, j, value;
 
    int h = 1;
    while(h < size) {
        h = 3*h+1;
    }
    while (h > 0) {
        for(i = h; i < size; i++) {
            value = vet[i];
            j = i;
            while (j > h-1 && value <= vet[j - h]) {
                vet[j] = vet[j - h];
                j = j - h;
            }
            vet[j] = value;
        }
        h = h/3;
    }
}