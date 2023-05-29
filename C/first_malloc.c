#include <stdlib.h>
#include <stdio.h>
//inclusão das bibliotecas basicas em c

char *s;
int *r;
//declaração de duas variaveis globais estaticas do tipo ponteiro
void main(){
    s = (char *) malloc(2000); //alocaçao de 2000 bytes de memoria e asssociacao com o ponteiro s
    r = (int *) malloc(40* sizeof(int)); //alocacao de 40 espaços do tipo inteiro e associação ao ponteiro r
    free(s);// libera a memoria alocada
    free(r);// libera a memoria alocada
    printf("executou");
    
};
