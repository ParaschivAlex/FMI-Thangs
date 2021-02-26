#include <stdio.h>
#include <unistd.h>///read,write
#include <fcntl.h>///open
#include <errno.h>
#include <sys/stat.h>///stat

int main(int argc, char *argv[])
{
    int f, g, size, n, err;
    struct stat sb;
    char buff[size];

    if(argc != 3)
    {
        perror("Trebuie sa avem: <comanda> <sursa> <destinatie>\n");
        return -1;
    }

    f = open(argv[1], O_RDONLY);
    g = open(argv[2], O_WRONLY | O_CREAT, 0644);

    if(!f)
    {
        perror("Nu s-a putut deschide fisierul sursa!");
        return errno;
    }
    if(!g)
    {
        perror("Nu s-a putut deschide fisierul destinatie!");
        return errno;
    }

    if(stat(argv[1],&sb))///stat intoarce informatii despre fisier
    {
        perror(NULL);
        return errno;
    }
    printf("Fisierul sursa ocupa %jd biti pe disk.\n", sb.st_size);
    size=sb.st_size;///marimea fisierului sursa(biti)
    read(f, buff, size);///citesc intreg continutul fisierului sursa in buff
    write(g, buff, size);///scriu in fisierul destinatie din buff

    close(f);
    close(g);

    return 0;
}
