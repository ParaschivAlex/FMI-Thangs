#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>
#include <sys/types.h>

int main(int argc, char *argv[])
{
	pid_t child;
	int n, v[101];

	for(int i=1;i<argc;i++)
		v[i]=atoi(argv[i]);

	printf("Starting parent %d\n",getpid());


	for(int i=1;i<=argc;i++)
	{
		child = fork();
		n = v[i];
		if(child == -1)
			return errno;

		if(child == 0)
		{
			printf("%d: %d ",n,n);
			while(n > 1)
			{
				if(n%2==0)
					n=n/2;
				else
					n=3*n+1;
				printf("%d ",n);
			}
			printf("\n");
			printf("Done Parent %d Me %d\n",getppid(),getpid());
			return 0;
		}
	}

	for(int i=1; i<=argc; i++)///procesul parinte
        wait(NULL);

	printf("Done Parent %d Me %d\n",getppid(),getpid());

	return 0;
}
