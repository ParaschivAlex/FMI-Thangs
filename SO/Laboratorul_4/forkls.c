#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>

int main()
{
	pid_t child = fork();
	if (child == -1)
		return errno;
	if(child != 0)
		{
			printf("My PID = %d, Child = %d\n", getpid(), child);
			wait(NULL);///parintele isi suspenda activitatea pt a astepta terminarea executiei fiului; daca sunt mai multi fii, wait asteapta doar unul
			printf("Child \t%d \t\n", child);
		}
	else
		{
			char *argv[] = {"ls", NULL};
			char *envp[] = {NULL};
			execve ("/bin/ls", argv, envp);///executa un alt program existent si suprascrie complet procesul apelant cu un nou proces conform programului gasit la calea indicata
		}

	return 0;
}
