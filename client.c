#include <stdio.h>
 #include <errno.h>
 #include <string.h>
 #include <netinet/in.h> 
 #include <netdb.h> 

 #define DATA_BUFFER "Mona Lisa was painted by Leonardo da Vinci"

 int main () {
     struct sockaddr_in saddr;
     int fd, ret_val;
     struct hostent *host; /* need netdb.h for this  */

     /* Step1: open a UDP socket */
     fd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP); 
     if (fd == -1) {
         fprintf(stderr, "socket failed [%s]\n", strerror(errno));
         return -1;
     }
     printf("Created a socket with fd: %d\n", fd);

     /* Next, initialize the server address */
     saddr.sin_family = AF_INET;         
     saddr.sin_port = htons(7000);     
     host = gethostbyname("127.0.0.1");
     saddr.sin_addr = *((struct in_addr *)host->h_addr);

     /* Step2: send some data */
     ret_val = sendto(fd,DATA_BUFFER, strlen(DATA_BUFFER) + 1, 0, 
         (struct sockaddr *)&saddr, sizeof(struct sockaddr_in));
     if (ret_val != -1) {
         printf("Successfully sent data (len %d bytes): %s\n", ret_val, DATA_BUFFER);
     } else {
         printf("sendto() failed [%s]\n", strerror(errno));
     }

     /* Last step: close the socket */
     close(fd);
     return 0;
 }