.data
	v: .word 10, 11, 12, 13
	w: .word 2, 3, 5, 6
	n: .word 4
	p: .word 3
	
.text

main:
	la $t0, v
	la $t1, w
	lw $t2, n
	lw $t3, p
	
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
	subu $sp, $sp 4
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
	lw $s3, 12($fp) # p
	li $s4, 0 # suma totala
	lw $s5, 0($s0) # prim element din v
	lw $s6, 0($s1) # prim element din w
	li $s7, 0 # elementul curent
	
	# $sp: (s7v)(s6v)(s5v)(s4v)(s3v)(s2v)(s1v)(s0v)(rav)(fpv)fp:(v)(w)(n)(p)
	
loop:
	beqz $s2, iesiAfara
	
	addu $s7, $s5, $s6
	
	subu $sp, $sp, 4
	sw $s3, 0($sp)
	subu $sp, $sp, 4
	sw $s7, 0($sp)
	
	jal cel_putin_p_div
	
	addu $sp, $sp, 8
	
	beqz $v0, nuAdaugaLaSuma
	
	rem $s7, $s5, $s6
	
	addu $s4, $s4, $s7
	
	addu $s0, $s0, 4
	addu $s1, $s1, 4
	lw $s5, 0($s0)
	lw $s6, 0($s1)
	subu $s2, $s2, 1
	
	j loop
	
nuAdaugaLaSuma:
	addu $s0, $s0, 4
	addu $s1, $s1, 4
	lw $s5, 0($s0)
	lw $s6, 0($s1)
	subu $s2, $s2, 1
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
	
cel_putin_p_div:
	subu $sp, $sp, 4
	sw $fp, 0($sp)
	addu $fp, $sp 4
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
	
	lw $s0, 0($fp) # v[i]+w[i]
	lw $s1, 4($fp) # p
	li $s2, 1 # i-ul
	li $s3, 0 # nr de divizori

loop2:
	bgt $s2, $s0, verifica
	
	rem $s4, $s0, $s2
	
	bgtz $s4, nuEsteDivizor
	
	addu $s3, $s3, 1
	addu $s2, $s2, 1
	
	j loop2
	
nuEsteDivizor:
	addu $s2, $s2, 1
	j loop2

verifica:
	bgt $s1, $s3, returneazaFals
	li $v0, 1
	j iesiAfara2
	
returneazaFals:
	li $v0, 0

iesiAfara2:
	lw $s4, -28($fp)
	lw $s3, -24($fp)
	lw $s2, -20($fp)
	lw $s1, -16($fp)
	lw $s0, -12($fp)
	lw $ra, -8($fp)
	lw $fp, -4($fp)
	jr $ra