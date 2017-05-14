#include<stdio.h>
int main(int argc, char const *argv[]) {
	int i, j, n, in, t;
	scanf("%d %d", &n, &j);
	for(i=0;i<j;i++){
		for (in = 0, t=1; in < i; in++) {
			t = t * n;
		}
		printf("%d\n", t);
	}
	return 0;
}
