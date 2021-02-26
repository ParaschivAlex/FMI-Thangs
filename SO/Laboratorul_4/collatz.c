#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>

int main(int argc, char *argv[])
{
    pid_t child = fork();
    if (child == -1)
        return errno;
    if(child == 0)
    {
        int n=atoi(argv[1]);
        printf("%d: %d ",n,n);
        while(n!=1)
        {
            if(n%2==0)
                n=n/2;
            else
                n=n*3+1;
            printf("%d ", n);
        }
        printf("\n");
    }
    else
    {
        wait(NULL);
        printf("Child \t%d\n",child);
    }

    return 0;
}
