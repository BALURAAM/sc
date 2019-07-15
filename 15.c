#include<stdio.h>
int main()
{
    int hrs,mts,b;
    scanf("%d",&mts);
    hrs=mts/60;
    if(hrs>0)
        mts=mts-(hrs*60);
    printf("%d %d",hrs,mts);
}
