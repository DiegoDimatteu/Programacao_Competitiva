#include <stdio.h>
 
int main(){
	int previous, count = 0, a, b, i;
	scanf("%d", &a);
	for(i = 0; i < a; i++){
		scanf("%d", &b);
		if(count == 0){
			previous = b;
			count++;
		}
		else if(b != previous){
			previous = b;
			count++;
		}
	}
	printf("%d\n", count);
}