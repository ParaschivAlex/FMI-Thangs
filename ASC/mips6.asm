.data
	v: .word 2, 3, 4, 5
	w: .word 4, 4, 4, 4
	n: .word 4
	x: .word 1
	y: .word 2
	sp: .asciiz " "
	
.text

main:
	la $t0, v
	la $t1, w
	lw $t2, n
	lw $t3, x
	lw $t4, y
	li $t5, 0
	li $t6, 0
	
	subu $sp, $sp, 4
	sw $t4, 0($sp)
	subu $sp, $sp, 4
	sw $t3, 0($sp)
	subu $sp, $sp, 4
	sw $t2, 0($sp)
	subu $sp, $sp, 4
	sw $t1, 0($sp)
	subu $sp, $sp, 4
	sw $t0, 0($sp)
	
	jal modif
	
	addu $sp, $sp, 20
	
	jal afisare
	
	li $v0, 10
	syscall
	
afisare:
	beq $t6, $t2, revenireMain
	lw $t5, 0($t0)
	move $a0, $t5
	li $v0, 1
	syscall
	la $a0, sp
	li $v0, 4
	syscall
	addu $t0, $t0, 4
	addu $t6, $t6, 1
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
	subu $sp, $sp, 4
	sw $s7, 0($sp)
	
	lw $s0, 0($fp) # v
	lw $s1, 4($fp) # w
	lw $s2, 8($fp) # n
	lw $s3, 12($fp) # x
	lw $s4, 16($fp) # y
	lw $s5, 0($s0) # primul element din v
	lw $s6, 0($s1) # primul element din w
	mul $s7, $s3, $s4 # xy
	
loop:
	beqz $s2, iesiAfara
	rem $s7, $s5, $s7
	bgtz $s7, nuModifica
	
	subu $sp, $sp, 4
	sw $s6, 0($sp)
	subu $sp, $sp, 4
	sw $s5, 0($sp)
	
	jal putere
	
	addu $sp, $sp, 8
	
	sw $v0, 0($s0)
	
	addu $s0, $s0, 4
	addu $s1, $s1, 4
	lw $s5, 0($s0)
	lw $s6, 0($s1)
	mul $s7, $s3, $s4 # s7 are dublu rol.
	subu $s2, $s2, 1
	j loop
	
nuModifica:
	addu $s0, $s0, 4
	addu $s1, $s1, 4
	lw $s5, 0($s0)
	lw $s6, 0($s1)
	mul $s7, $s3, $s4
	subu $s2, $s2, 1
	j loop

iesiAfara:
	lw $s7, -40($fp)
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
	
putere:
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
	
	lw $s0, 0($fp) # v[i]
	lw $s1, 4($fp) # w[i]
	li $s2, 0
	li $s3, 1
	
loop2:
	beq $s2, $s1, iesiAfara2
	mul $s3, $s3, $s0
	addu $s2, $s2, 1
	j loop2
	
iesiAfara2:
	move $v0, $s3
	lw $s3, -24($fp)
	lw $s2, -20($fp)
	lw $s1, -16($fp)
	lw $s0, -12($fp)
	lw $ra, -8($fp)
	lw $fp, -4($fp)
	jr $ra
