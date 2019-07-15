#include<stdio.h>
int main()
{
    int i,N,arrr[100];
    scanf("%d",&N);
    for(i=0;i<N;i++)
        scanf("%d",&arrr[i]);
    for(i=0;i<N;i++)
        printf("%d %d\n",arrr[i],i);
}
