#include <stdio.h>
#include <stdbool.h>
void main()
{
    int n,a,p;
    a = 2;
    p = true;
    
    printf("Enter Your Number: ");
    scanf("%d",&n);
    
    while (n>a)
    {
        if (n%a==0)
        {
        p = false;
        break;
        }
        
    a++;
    }
    
    if(p==true)
    printf("%d is Prime",n);
    else
    printf("%d is Not-Prime",n);
}