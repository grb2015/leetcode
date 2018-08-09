#include <stdio.h>
#include <malloc.h>
int* twoSum(int* nums, int numsSize, int target){
	int i,j;
	for( i = 0;i<numsSize-1;i++){
		for( j = i+1;j<numsSize;j++){
			if(nums[i] + nums[j] == target){
				int *index = malloc(sizeof(int)*2);
				index[0] = i;
				index[1] = j;
				return index;
			}
		}
	}
    return NULL;
}
int main(void)
{
    //int nums[] = {-1, -2, -3, -4, -5};
    //int target = -8;
    //int nums[] = {0,4,3,0};
    //int target = 0;
    int nums[] = { 3, 2, 3 };
    int count = sizeof(nums) / sizeof(*nums);
    int target = 6;
    int *indexes = twoSum(nums, count, target);
    if (indexes != NULL) {
        printf("%d %d\n", indexes[0], indexes[1]);
    } else {
        printf("Not found\n");
    }

    return 0;
}
