#include <stdio.h>
#include <malloc.h>
#include <string.h>
int get_min_array_index(char** strs, int strsSize){
	int i ;
	int min_len = strlen(strs[0]);
	int min_len_index = 0;
	for(i = 1;i<strsSize;i++){
		if(min_len > strlen(strs[i])){
			min_len = strlen(strs[i]);
			min_len_index = i;
		}
	}
	return min_len_index;
}
char* longestCommonPrefix(char** strs, int strsSize){
    int i,j ;
    printf("strlen(strs[0])  = %d\n",strlen(strs[0]));
    int min_index = get_min_array_index(strs,strsSize);
    for(i = 0;i<strlen(strs[min_index]);i++){
    	char c = strs[0][i];
    	printf("c = %c\n", c);
    	for(j = 0;j<strsSize;j++){
    		printf("strs[%d][%d] = %c\n",j,i,strs[j][i]);
    		if(strs[j][i] != c){
	    		//printf("error!\n");
	    		char*p = (char*)malloc(sizeof(char)*(i+1));
	    		strncpy(p,strs[0],i);
	    		p[i] = '\0';
	    		return p;
    		}
   		}
    }
    return strs[min_index];
}
int main(int argc, char const *argv[])
{
	//char *a[] = {"flower","flow","flight"}; 
	char *a[] = {"dog","racecar","car"}; 
	//char *a[] = {"abca","abc"};
	
	char**strs = a;
	char*comm_str = longestCommonPrefix(strs,sizeof(a)/sizeof(a[0]));
	printf("%s\n",comm_str );
	return 0;
}