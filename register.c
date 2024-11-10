#include <stdio.h>
#include <string.h>

int main()	{
	
	char users[10000];
	char user[32];
	int reps;
	int count = 0;
	int index = 0;
	int flag = 0;
	
	scanf("%d", &reps);
	
	for (int i = 0; i < reps; i++)	{
		scanf("%s", &user);
		
		
		
		for (int j = 0; j < sizeof(users)/sizeof(users[0]); j++)	{
			if (users[j] == user)	{
				count++;
				flag = 1;
			
			}
		}
			
		if (flag == 0)	{	
			users[index] = user;
			index++;
		}
			
	  

	  
		if (count == 0) 	{
			printf("OK\n");
		}	else	{
			printf("%s%d\n", user, count);
		}
			
			
				
}
		
		
		
		
	
	


	
	return 0;
}