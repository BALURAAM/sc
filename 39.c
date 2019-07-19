#include<stdio.h>
int main()
{
    int a,i,b,c,sum=1,ans;
    scanf("%d%d%d",&a,&b,&c);
    while(b!=0)
    {
        sum=sum*a;
        b--;
    }
    //printf("%d",sum);
    ans=sum%c;
    printf("%d",ans);
}
