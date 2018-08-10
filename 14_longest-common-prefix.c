/*
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀
*/
#include <stdio.h>
#include <malloc.h>
#include <string.h>
/*
	brief : find the shortest len string from strs,and return the index 
*/
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
/*
	算法思路：
	先找出所有输入字符串中最短的那个设为shortest_str,
	然后对shortest_str中的每个字符，在所有strs中查看是否都有
	所有是一个二层for遍历.
*/
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