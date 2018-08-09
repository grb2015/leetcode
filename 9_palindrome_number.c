#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define bool int 
#define false 0
#define true 1

#define BUFFER_LEN  11  // unsigned long 0～4294967295 , in fact , BUFFER_LEN = 11 is  enough
bool isPalindrome_str(char*str)
{
	if(str == NULL)
		return false;
	int i = 0;
	int j = strlen(str)-1;
	while(i < j){
		printf("str[%d] = %c,str[%d] = %c\n",i,str[i],j,str[j] );
		if(str[i] != str[j]){
			printf("str[i]!=str[j]\n");
			return false;
		}
		i++;
		j--;
	}
	return true;
}
bool isPalindrome(int x) {
    if(x<0)
    	return false;
    char *p = (char*)malloc(sizeof(char)*BUFFER_LEN);
    if(p != NULL){
	   	sprintf(p,"%d",x); // itoa is not supported in gcc ,use sprintf instead
	    //printf("p = %s\n",p );
	    bool rt = isPalindrome_str(p);
	    free(p);
	    return rt;
    }
    else{
    	printf("[%s]: cannot juege,malloc error!\n",__FUNCTION__);
    }
   	return false;
}
int main(int argc, char const *argv[])
{
	int x[] = {-123,0,1927007291};
	int i ;
	for(i = 0;i<3;i++){
		printf("isPalindrome(%d) = %d \n",x[i],isPalindrome(x[i]) );
	}
	return 0;
}