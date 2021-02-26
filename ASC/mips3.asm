.data
	v: .word 1, 2, 3, 4
	n: .word 4
	a: .word 10
	c: .word 3
	t: .word 4
	
.text

main:
	la $t0, v
	lw $t1, n
	lw $t2, a
	lw $t3, c
	lw $t4, t
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
	beq $t5, $t1, intoarceMain
	lw $t6, 0($t0)
	move $a0, $t6
	li $v0, 1
	syscall
	addu $t5, $t5, 1
	addu $t0, $t0, 4
	j afisare
	
	
intoarceMain:
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
	
	# $sp: (s6v)(s5v)(s4v)(s3v)(s2v)(s1v)(s0v)(rav)(fpv)fp:(v)(n)(a)(c)(t)
	
	lw $s0, 0($fp) # v
	lw $s1, 4($fp) # n
	lw $s2, 8($fp) # a
	lw $s3, 12($fp) # c
	lw $s4, 16($fp) # t
	lw $s5, 0($s0) # primul element din vector
	li $s6, 0 # i-ul
	
loop:
	beq $s6, $s1, iesiAfara
	
	bge $s5, $s4, nuModifica
	subu $sp, $sp, 4
	sw $s5, 0($sp)
	subu $sp, $sp, 4
	sw $s3, 0($sp)
	subu $sp, $sp, 4
	sw $s2, 0($sp)
	
	jal f
	
	addu $sp, $sp, 12
	
	sw $v0, 0($s0)
	
	addu $s6, $s6, 1
	addu $s0, $s0, 4
	lw $s5, 0($s0)
	j loop
	
nuModifica:
	addu $s6, $s6, 1
	addu $s0, $s0, 4
	lw $s5, 0($s0)
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
	# $sp: (s4v)(s3v)(s2v)(s1v)(s0v)(rav)(fpv)fp:...
	
	lw $s0, 0($fp) # a
	lw $s1, 4($fp) # c
	lw $s2, 8($fp) # v[i]
	mul $s3, $s0, $s2
	rem $s4, $s3, $s1

	move $v0, $s4
	
	lw $s4, -28($fp)
	lw $s3, -24($fp)
	lw $s2, -20($fp)
	lw $s1, -16($fp)
	lw $s0, -12($fp)
	lw $ra, -8($fp)
	lw $fp, -4($fp)
	jr $ra