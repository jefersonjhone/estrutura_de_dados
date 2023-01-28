#include <stdlib.h>
#include <stdio.h>

char *s;
int *r;
main()
{
s = (char *) malloc(2000);
if (s == NULL){
    printf("\nErro de alocação de memoria!");
    exit(1);
}
r = (int *) malloc(40*sizeof(int));
if (r == NULL){
    printf("\nErro na alocação de memoria!");
    exit(1);
}
else
{
printf("alocaçoes bem sucedidas!!\n");
};
free(s);
free(r);
return 1;
};
