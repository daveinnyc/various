# PURPOSE: Exit and return a status code to the kernel

# INPUT: none

# OUTPUT: a status code, to view type: echo $? 

# VARIABLES: 
#      %eax holds the system call number
#      %ebx holds the return status

.section .data
.global _start
_start:
movl $1, %eax   # kernel sys call to exit
# movl $0, %ebx   # return status passed to  sys call
movl $4, %ebx   # return status passed to  sys call
int $0x80       # kernel execute command
