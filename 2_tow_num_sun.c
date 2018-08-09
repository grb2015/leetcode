#include <stdio.h>
#include <malloc.h>

struct ListNode {
      int val;
      struct ListNode *next;
};

#define bool long int
#define TRUE 1
#define FALSE 0


void print_link(struct ListNode*head)
{
	if(head != NULL){
		struct ListNode*tmp = head;
		while(tmp != NULL){
			printf("%d --> ",tmp->val);
			tmp = tmp->next;
		}
	}
	printf("\n");
}
/*
	intput  :  init_mode, the node of head
	returns : listNode*, if init_node  is NUll ,then return NULL.
*/
struct ListNode* creat_link(struct ListNode*init_node)
{
	struct ListNode* head = init_node;
	return head;
}


/*
	intput  :  listNode* head, the head addr 
			   ListNode*new_node  , the addr struct of node to be added 
	returns :  NULL if head is NULL
			   struct ListNode*    ,list head ,added new_node
*/
struct ListNode*  add_node(struct ListNode*head,struct ListNode*new_node)
{
	if(head == NULL){
		printf("head is NULL, you must creat_link first\n");
		return NULL;
	}
	struct ListNode*tmp = head;
	while(tmp->next != NULL){
		tmp = tmp->next;
	}
	tmp->next = new_node;
	return head;
}

long int get_link_len(struct ListNode*head)
{
	long int len  = 0;
	struct ListNode*tmp = head;

	if(head == NULL)
		return -1;
	while(tmp != NULL){
		len++;
		tmp = tmp->next;
	}
	return len;
	
}
/*
	store the values of head into array
	the array len must equal head len ;
*/
bool get_link_values(struct ListNode*head,long int *array,long int array_len)
{
	struct ListNode*tmp = head;
	long int link_len = get_link_len(head);
	if(link_len > array_len){
		printf("[%S] error: link_len > array_len ",__FUNCTION__);
		return FALSE;
	}
	long int i = 0;
	while(tmp != NULL){
		array[i] = tmp->val;
		tmp = tmp->next;
		++i;
	}
	return TRUE;

}

/*
	breif: print every value of array
*/
void print_array(long int*array,long int len)
{
	long int i ;
	for(i = 0;i<len;i++){
		printf("array[%d] = %d\n",i,array[i] );
	}
	printf("len = %d\n",len);
}

/*
	breif: caculate the value from array
	example:
		array[] = {1,2,3}
		return : 3*100+2*10+1*1 = 300+20+1 = 321
*/
long long int struct_num_from_array(long int *array,long int len)
{
	long int i ;
	long long int result_num = 0;
	printf("$$$ len =%ld\n",len);
	for (i = len-1;i>=0; i--){
		result_num = result_num*10 + array[i];
		printf("$$$ array[i] = %ld ",array[i]);
		printf("$$$ result_num= %ld \n",result_num);
	}
	printf("final: $$$ result_num= %ld \n",result_num);
	return result_num;
}

/*
	brief: struct a link  from num
	example:
		num = 807
		the link is : 7->0->8
*/
struct ListNode* struct_link_from_num(long long int num)
{	
	static struct ListNode*head = NULL;
	long long int y = num%10;	// y is remainder,   7 
	num = num/10;
	//printf("---before while ,y = %d\n",y );
	//printf("---before while ,num = %d\n",num );
	// 在leetcode上这里不能用static struct ListNode init_node ,不然会报free错，可能它本身要free链表，所以必须Malloc
	struct ListNode *init_node = (struct ListNode*)malloc(sizeof(struct ListNode));
	init_node->val = y;
	init_node->next = NULL;
	head = creat_link(init_node);
	
	while(num != 0){
		y = num%10;	// get 7 , 0, 8
		num = num/10;
		//printf("---before while ,y = %d\n",y );
		//printf("---before while ,num = %d\n",num );
		struct ListNode *new_node = (struct ListNode*)malloc(sizeof(struct ListNode));  // nei cun xie lou 
		new_node->val = y;
		new_node->next = NULL;
		add_node(head,new_node);
	}
	//print_link(head);
	return head;

}
/*
	returns: 
			NULL: if error eccured 
			struct ListNode* , the add of link  fo l1 and l2 vaules 
*/
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) 
{
    if(l1 == NULL) {
    	return l2;
    }
    if(l2 == NULL){
    	return l1;
    }
    long int len_l1 = get_link_len(l1);
    long int len_l2 = get_link_len(l2);

    //printf("len_l1  = %d ",len_l1 );
    //printf("len_l2  = %d ",len_l2);
    long int *array1 = (long int*)malloc(sizeof(long int)*len_l1);
    long int *array2 = (long int*)malloc(sizeof(long int)*len_l2);
    if(array1 == NULL || array2 == NULL){
    	printf("[[%s] error: malloc error \n",__FUNCTION__ );
    	return NULL;
    }
    if( FALSE == get_link_values(l1,array1,len_l1)
    	|| FALSE == get_link_values(l2,array2,len_l2)){

    	printf("[%s] error: get link return FALSE. \n",__FUNCTION__ );
    	return NULL;
    }
    //print_array(array1,len_l1);
    //printf("##########debug num2 array begin ####################");
    print_array(array2,len_l2);
    //printf("##########debug num2 array end ####################");
    long long int num1  = struct_num_from_array(array1,len_l1);
    printf("num1 = %ld\n",num1 );
    printf("########## debug num2 num begin ####################");
    long long int num2  = struct_num_from_array(array2,len_l2);
    printf("num2 = %ld\n",num2 );
    printf("########## debug num2 num end ####################");
    long long int sum_num = num1 + num2;
    printf("sum_num = %ld\n",sum_num );
    struct ListNode*sum_link_head =  struct_link_from_num(sum_num);
    //print_link(sum_link_head);
   	return sum_link_head;
}

long int main(long int argc, char const *argv[])
{
	struct ListNode new_node[] = {{9,NULL}};
	long int i ;
	struct ListNode*head1 = creat_link(&new_node[0]);
	
	for(i = 1;i<1;i++){
		add_node(head1,&new_node[i]);
	}
	print_link(head1);
	printf("---------------\n");
	struct ListNode new_node2[] = {{1,NULL},{9,NULL},{9,NULL},{9,NULL},{9,NULL},{9,NULL},{9,NULL},{9,NULL},{9,NULL},{9,NULL}};
	struct ListNode*head2 = creat_link(&new_node2[0]);
	for(i = 1;i<10;i++){
		add_node(head2,&new_node2[i]);
	}
	print_link(head2);

	#if 0
	struct ListNode new_node[] = {{2,NULL},{4,NULL},{3,NULL}};
	long int i ;
	struct ListNode*head1 = creat_link(&new_node[0]);
	
	for(i = 1;i<3;i++){
		add_node(head1,&new_node[i]);
	}
	print_link(head1);
	printf("---------------\n");
	struct ListNode new_node2[] = {{5,NULL},{6,NULL},{4,NULL}};
	struct ListNode*head2 = creat_link(&new_node2[0]);
	for(i = 1;i<3;i++){
		add_node(head2,&new_node2[i]);
	}
	print_link(head2);

	
	printf("test struct_link_from_num");
	//struct ListNode*sum_link_head =  struct_link_from_num(807);
    
    //long int y = 1;
    //struct ListNode init_new_node ={y,NULL};
	//struct ListNode*sum_link_head = creat_link(&init_new_node);
	//print_link(sum_link_head);
	#endif
	printf("----------------addTwoNumbers---------- \n");
	struct ListNode*sum_link_head  = addTwoNumbers(head1,head2);
	print_link(sum_link_head);

	return 0;
}