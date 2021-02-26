.data
	v: .word 1, 2, 4, 5
	n: .word 4
	x: .word 2
	t: .word 16
	
.text

main:
	la $t0, v
	lw $t1, n
	lw $t2, x
	lw $t3, t
	
	subu $sp, $sp, 4
	sw $t3, 0($sp)
	subu $sp, $sp, 4
	sw $t2, 0($sp)
	subu $sp, $sp, 4
	sw $t1, 0($sp)
	subu $sp, $sp, 4
	sw $t0, 0($sp)
	
	jal eval
	
	addu $sp, $sp, 16
	
	move $a0, $v1
	li $v0, 1
	syscall
	
	li $v0, 10
	syscall
	
eval:
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
	# $sp: (s7v)(s6v)(s5v)(s4v)(s3v)(s2v)(s1v)(s0v)(rav)(fpv)fp:(v)(n)(x)(t)
	
	lw $s0, 0($fp) # v
	lw $s1, 4($fp) # n
	lw $s2, 8($fp) # x
	lw $s3, 12($fp) # t
	li $s4, 0 # suma totala
	li $s5, 0 # i-ul curent
	li $s6, 0 # termen curent
	lw $s7, 0($s0) # primul element din vector
	
loop:
	beq $s5, $s1, iesiAfara
	
	subu $sp, $sp, 4
	sw $s7, 0($sp)
	subu $sp, $sp, 4
	sw $s3, 0($sp)
	
	jal este_putere
	
	addu $sp, $sp, 8
	
	beq $v0, 1, nuAdaugaLaSuma
	
	mul $s6, $s7, $s2
	addu $s6, $s6, 1
	addu $s4, $s4, $s6
	
	addu $s0, $s0, 4
	addu $s5, $s5, 1
	lw $s7, 0($s0)
	
	j loop
	
nuAdaugaLaSuma:
	addu $s0, $s0, 4
	addu $s5, $s5, 1
	lw $s7, 0($s0)
	j loop

iesiAfara:
	move $v1, $s4
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
	
este_putere:
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

	# $sp: (s3v)(s2v)(s1v)(s0v)(rav)(fpv)fp:(t)(v[i])
	
	lw $s0, 0($fp) # t
	lw $s1, 4($fp) # v[i]
	rem $s3, $s0, $s1 # s3 = v[i] % t
	
	beq $s1, 1, iesiAfara2
loop2:
	bgt $s3, 0, verifica
	div $s0, $s0, $s1
	rem $s3, $s0, $s1
	j loop2

verifica:
	bgt $s0, 1, nuEstePutere
	li $v0, 1
	j iesiAfara2
	
nuEstePutere:
	li $v0, 0
	
iesiAfara2:
	lw $s3, -24($fp)
	lw $s2, -20($fp)
	lw $s1, -16($fp)
	lw $s0, -12($fp)
	lw $ra, -8($fp)
	lw $fp, -4($fp)
	jr $ra
	
	