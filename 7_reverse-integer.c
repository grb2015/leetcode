#include <stdio.h>
int reverse(int x) {
	int rt_value = 0;
	int r;
	long  int x1;
    if(x >2147483647 || x <  -2147483648)
    	return 0;
	while(x != 0){
		r = x%10;	// y is remainder
		printf("r = %d,x = %d ",r,x );
		x = x/10;
		x1 = (long int )rt_value*10 + r;  //// if x =1534236469, x is not limit ,but reserver_x is 
		printf("x1 =%ld\n",x1 );
		if(x1 >2147483647 || x1 <  -2147483648){
			printf(" beyond int limit\n");
			return 0;
		}
		rt_value =  rt_value*10 + r;
	}
	return rt_value;
}

int main(int argc, char const *argv[])
{
	int x = 1534236469;   // if x =1534236469, x is not limit ,but reserver_x is 
	printf("%d\n",reverse(x) );
	return 0;
}