#include <stdio.h>
#include <string.h>
 
int main()
{
    int smallest, s2;
    int array[100], n, i;
    scanf("%d", &n);
    for (i = 0 ; i <n; i++)
        scanf("%d", &array[i]);
    if (array[0] < array[1]) {
        smallest = array[0];
        s2 = array[1];
    }
    else {
      smallest = array[1];
      s2 = array[0];
    }
    for (i = 2; i < n; i++) {
        if (array[i] < smallest) {
        s2 = smallest;
        smallest = array[i];
        }
        else if (array[i] < s2) {
            s2 = array[i];
        }
    }
    printf("%d", s2);
}
