.data
	v: .word 1, 4, 6
	n: .word 3
	x: .word 2
	y: .word 1
	z: .word 3

.text

main:
	la $t0, v
	lw $t1, n
	lw $t2, x
	lw $t3, y
	lw $t4, z
	
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
	jal eval
	addu $sp, $sp, 20
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
	# $sp: ($rav)($fpv)fp:(v)(n)(x)(y)(z)
	
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
	# $sp: (s7v)(s6v)(s5v)(s4v)(s3v)(s2v)(s1v)(s0v)(rav)(fpv)fp:(v)(n)(x)(y)(z)
	
	li $s0, 0 # i-ul
	lw $s1, 0($fp) # v
	lw $s2, 4($fp) # n
	lw $s3, 8($fp) # x
	lw $s4, 12($fp) # y
	lw $s5, 16($fp) # z
	li $s7, 0 # suma totala
	
loop:
	beq $s0, $s2, iesiAfara
	lw $s6, 0($s1) # prim element din vector
	addu $s6, $s6, $s4 # v[i] + y, arg. 2 pentru a doua functie
	
	subu $sp, $sp, 4
	sw $s6, 0($sp)
	subu $sp, $sp, 4
	sw $s3, 0($sp)
	
	jal exactXDivizori
	
	addu $sp, $sp, 8
	
	beq $v0, 1, nuAdaugaLaSuma
	
	lw $s6, 0($s1)
	subu $s6, $s6, $s5
	addu $s7, $s7, $s6
	addu $s1, $s1, 4 # urm. element din vector
	addu $s0, $s0, 1 # creste i
	
	j loop
	
nuAdaugaLaSuma:
	addu $s1, $s1, 4
	addu $s0, $s0, 1
	j loop
	
iesiAfara:
	move $v1, $s7
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

exactXDivizori:
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
	sw $s4, 0($sp) # $sp: (s4v)(s3v)(s2v)(s1v)(s0v)(rav)(fpv)fp:...
	
	lw $s0, 0($fp) # x
	lw $s1, 4($fp) # v[i] + y
	li $s2, 1 # nr_divizori
	li $s3, 2 # divizorul
	li $s4, 0 # pentru modulo

loop2:
	bgt $s3, $s1, testeaza
	rem $s4, $s1, $s3
	beq $s4, 0, aduna
	addu $s3, $s3, 1
	j loop2
	
aduna:
	addu $s2, $s2, 1
	addu $s3, $s3, 1
	j loop2

testeaza:
	beq $s0, $s2, adevarat
	j fals
	
adevarat:
	li $v0, 1

fals:
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
	