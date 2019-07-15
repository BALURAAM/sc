#include <stdio.h>

int main()
{
    int bala[100],N,i,j,c,K;
    scanf("%d",&N);
    scanf("%d",&K);
    for(i=0;i<N;++i)
    {
        scanf("%d",&bala[i]);
    }
    for(i=0;i<N;++i)
    {
        for(j=0;j<N-1;++j)
        {
            if(bala[j]<bala[j+1])
            {c=bala[j];
            bala[j]=bala[j+1];
            bala[j+1]=c;
                
            }
            
        }
    }
    printf("%d",bala[K-1]);
    return 0;
}
