/* The following program takes two inputs a and b
    it prints a integers with the following rule
    1. print from 1 to b
    2. then print from b-1 to 1
    3. then print from 2 to b
    keep repeating till a integers are printed
*/
#include<stdio.h>
void main(){
    int a,b,c=1,x=1;
    scanf("%d %d",&a,&b);
    while(c<=a){
        while(x<b && c<=a){
            printf("%d ",x);
            c++;
            x++;
        }
        if(x>b){
            x-=2;
            while(x>=1 && c<=a){
                printf("%d ",x);
                c++;
                x--;
            }
        }
        x+=2;
    }
    
}
