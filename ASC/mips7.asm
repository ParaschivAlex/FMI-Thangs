.data
	v: .word 1, 2, 3, 4
	n: .word 4
	a: .word 10
	sp: .asciiz " "
	
.text

main:
	la $t0, v
	lw $t1, n
	lw $t2, a
	li $t3, 0
	li $t4, 0
	
	subu $sp, $sp, 4
	sw $t2, 0($sp)
	subu $sp, $sp, 4
	sw $t1, 0($sp)
	subu $sp, $sp, 4
	sw $t0, 0($sp)
	
	jal modif
	
	addu $sp, $sp, 12
	
	jal afisare
	
	li $v0, 10
	syscall
	
afisare:
	beq $t4, $t1, revenireMain
	lw $t3, 0($t0)
	move $a0, $t3
	li $v0, 1
	syscall
	la $a0, sp
	li $v0, 4
	syscall
	addu $t4, $t4, 1
	addu $t0, $t0, 4
	j afisare

revenireMain:
	jr $ra
	
modif:
	subu $sp, $sp, 4
	sw $fp, 0($sp)
	addu $fp, $sp, 4
	subu $sp, $sp, 4
	sw $ra, 0($sp)
	
	subu $sp, $sp, 4
	sw $s0, 0($sp)
	subu $sp, $sp, 4
	sw $s1, 0($sp)
	subu $sp, $sp, 4
	sw $s2, 0($sp)
	subu $sp, $sp, 4
	sw $s3, 0($sp)
	subu $sp, $sp, 4
	sw $s4, 0($sp)
	subu $sp, $sp, 4
	sw $s5, 0($sp)
	subu $sp, $sp, 4
	sw $s6, 0($sp)
	
	lw $s0, 0($fp) # v
	lw $s1, 4($fp) # n
	lw $s2, 8($fp) # a
	lw $s3, 0($s0) # primul element din v
	li $s5, 0 # i-ul

loop:
	beq $s5, $s1, iesiAfara
	addu $s6, $s3, $s2
	
	subu $sp, $sp, 4
	sw $s3, 0($sp)
	
	jal f
	
	addu $sp, $sp, 4
	
	rem $s6, $v0, 2
	
	bgt $s6, 0, nuModifica
	
	addu $v0, $v0, $s2
	sw $v0, 0($s0)
	
	addu $s0, $s0, 4
	addu $s5, $s5, 1
	lw $s3, 0($s0)
	
	j loop
	
nuModifica:
	addu $s0, $s0, 4
	addu $s5, $s5, 1
	lw $s3, 0($s0)
	j loop
	
iesiAfara:
	lw $s6, -36($fp)
	lw $s5, -32($fp)
	lw $s4, -28($fp)
	lw $s3, -24($fp)
	lw $s2, -20($fp)
	lw $s1, -16($fp)
	lw $s0, -12($fp)
	lw $ra, -8($fp)
	lw $fp, -4($fp)
	jr $ra
	
f:
	subu $sp, $sp, 4
	sw $fp, 0($sp)
	addu $fp, $sp, 4
	subu $sp, $sp, 4
	sw $ra, 0($sp)
	
	subu $sp, $sp, 4
	sw $s0, 0($sp)
	subu $sp, $sp, 4
	sw $s1, 0($sp)
	subu $sp, $sp, 4
	sw $s2, 0($sp)
	subu $sp, $sp, 4
	sw $s3, 0($sp)
	subu $sp, $sp, 4
	sw $s4, 0($sp)
	
	lw $s0, 0($fp) # v[i]
	li $s1, 0 # numarul de iterarii
	
	beq $s0, 1, returneaza1
	
loop2:
	beq $s0, 1, iesiAfara2
	rem $s4, $s0, 2
	beqz $s4, x_e_par
	
x_e_impar:
	mul $s0, $s0, 3
	addu $s0, $s0, 1
	addu $s1, $s1, 1
	j loop2
	
x_e_par:
	div $s0, $s0, 2
	addu $s1, $s1, 1
	j loop2

returneaza1:
	addu $s1, $s1, 1

iesiAfara2:
	move $v0, $s1
	lw $s4, -28($fp)
	lw $s3, -24($fp)
	lw $s2, -20($fp)
	lw $s1, -16($fp)
	lw $s0, -12($fp)
	lw $ra, -8($fp)
	lw $fp, -4($fp)
	jr $ra