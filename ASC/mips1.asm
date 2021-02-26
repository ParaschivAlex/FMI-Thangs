.data
	v: .word 1, 2, 4, 5
	n: .word 4
	x: .word 2
	t: .word 16

.text

main:
	lw $t0, t
	lw $t1, x
	lw $t2, n
	la $t3, v
	li $t4, 0 # suma totala
	li $t5, 0 # i-ul
	
	subu $sp, $sp, 4
	sw $t0, 0($sp)
	subu $sp, $sp, 4
	sw $t1, 0($sp)
	subu $sp, $sp, 4
	sw $t2, 0($sp)
	subu $sp, $sp, 4
	sw $t3, 0($sp)
	subu $sp, $sp, 4
	sw $t4, 0($sp)
	subu $sp, $sp, 4
	sw $t5, 0($sp)
	
	# $sp: (i)(s)(v)(n)(x)(t)
	
	jal eval
	
	addu $sp, $sp, 24
	move $a0, $v1
	li $v0, 1
	syscall
	li $v0, 10
	syscall
	
eval:
	subu $sp, $sp, 4
	sw $fp, 0($sp)
	addu $fp, $sp, 12
	subu $sp, $sp, 4
	sw $ra, 0($sp)
	
	# $sp: ($ra)($fpv)(i)(s)fp:(v)(n)(x)(t)
	
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
	
	# $sp: (s6v)(s5v)(s4v)(s3v)(s2v)(s1v)(s0v)(ra)(fpv)(i)(s)fp:(v)(n)(x)(t)
	
	lw $s0, 0($fp) # v
	lw $s1, 4($fp) # n
	lw $s2, 8($fp) # x
	lw $s3, 12($fp) # t
	lw $s4, -4($fp) # suma totala
	lw $s5, -8($fp) # i-ul curent
	li $s6, 0 # elem. curent
	
calculeaza_suma:
	beq $s1, $s5, oprire
	subu $sp, $sp, 4
	
	lw $s6, 0($s0)

	sw $s6, 0($sp)
	
	subu $sp, $sp, 4
	sw $s3, 0($sp)
	
	jal este_putere
	
	addu $sp, $sp, 8 # (s7v)(s6v)(s5v)(s4v)(s3v)(s2v)(s1v)(s0v)(ra)(fpv)(i)(s)fp:(v)(n)(x)(t)
	
	beq $v0, 1, altfel
	lw $s6, 0($s0)
	mul $s6, $s6, $s2
	addu $s6, $s6, 1
	addu $s4, $s4, $s6 # cresc suma
	addu $s5, $s5, 1 # cresc i-ul
	addu $s0, $s0, 4 # urmatorul element din vector
	j calculeaza_suma
	

altfel:
	addu $s5, $s5, 1
	addu $s0, $s0, 4
	j calculeaza_suma
	
oprire:
	lw $s7, -48($fp)
	lw $s6, -44($fp)
	lw $s5, -40($fp)
	lw $s4, -36($fp)
	lw $s3, -32($fp)
	lw $s2, -28($fp)
	lw $s1, -24($fp)
	lw $s0, -20($fp)
	lw $ra, -16($fp)
	lw $fp, -12($fp)
	jr $ra

este_putere:
	subu $sp, $sp, 4
	sw $fp, 0($sp)
	addu $fp, $sp, 64
	subu $sp, $sp, 4
	sw $ra, 0($sp) # (rav2)(fpv2)fp2:(v)(t)(s7v)(s6v)(s5v)(s4v)(s3v)(s2v)(s1v)(s0v)(ra)(fpv)(i)(s)fp:(v)(n)(x)(t)
	
	subu $sp, $sp, 4
	sw $s0, 0($sp)
	subu $sp, $sp, 4
	sw $s1, 0($sp)
	
	lw $s0, 0($fp)
	lw $s1, 4($fp)
	
	move $a0, $s0
	li $v0, 1
	syscall
	move $a0, $s1
	li $v0, 1
	syscall
	li $v0, 10
	syscall
