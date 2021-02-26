#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <fcntl.h>

int main()
{
	int d;
	d = open("foo.txt", O_RDWR | O_CREAT);
	write(d, "Hello World!\n", 13);
	close(d);
	return 0;
}
