#include <stdio.h>

int main()
{
    int bala[100],N,i,j,c,K;
    scanf("%d",&N);
    for(i=0;i<N;++i)
    {
        scanf("%d",&bala[i]);
    }
    
    {
        for(j=0;j<N-1;++j)
        {
            if(bala[j]>bala[j+1])
            {
                c=bala[j];
                bala[j]=bala[j+1];
                bala[j+1]=c;
           
                
            }
             
            
        }
    }
    for(i=0;i<N;++i)
    printf("%d ",bala[i]);
}
