 #include <stdio.h>
 #include <errno.h>
 #include <netinet/in.h> 

 #define DATA_BUFFER 5000

 int main () {
     struct sockaddr_in saddr, new_addr;
     int fd, ret_val;
     char buf[DATA_BUFFER];
     socklen_t addrlen; 

     /* Step1: open a UDP socket */
     fd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP); 
     if (fd == -1) {
         fprintf(stderr, "socket failed [%s]\n", strerror(errno));
         return -1;
     }
     printf("Created a socket with fd: %d\n", fd);

     /* Initialize the socket address structure */
     saddr.sin_family = AF_INET;         
     saddr.sin_port = htons(7000);     
     saddr.sin_addr.s_addr = INADDR_ANY; 

     /* Step2: bind the socket */
     ret_val = bind(fd, (struct sockaddr *)&saddr, sizeof(struct sockaddr_in));
     if (ret_val != 0) {
         fprintf(stderr, "bind failed [%s]\n", strerror(errno));
         close(fd);
         return -1;
     }
while(1){
     /* Step3: Start receiving data. */
     printf("Let us wait for a remote client to send some data\n");
     ret_val = recvfrom(fd, buf, DATA_BUFFER, 0,
                 (struct sockaddr *)&new_addr, &addrlen);
     if (ret_val != -1) {
         printf("Received data (len %d bytes): %s\n", ret_val, buf);
     } else {
         printf("recvfrom() failed [%s]\n", strerror(errno));
     }
 }
     /* Last step: close the socket */
     close(fd);
     return 0;
 }