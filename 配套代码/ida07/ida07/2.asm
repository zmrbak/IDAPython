; Listing generated by Microsoft (R) Optimizing Compiler Version 19.32.31328.0 

	TITLE	c:\users\lib\source\repos\ida07\ida07\release\ida07.obj
	.686P
	.XMM
	include listing.inc
	.model	flat

INCLUDELIB OLDNAMES

PUBLIC	??_C@_0BC@OHAFMDGK@This?5is?5fun_3?5?$CFd?6@	; `string'
PUBLIC	??_C@_0BC@CMFJBAMP@This?5is?5fun_2?5?$CFd?6@	; `string'
PUBLIC	??_C@_0BC@KKMNGCGB@This?5is?5fun_1?5?$CFd?6@	; `string'
PUBLIC	??_C@_0O@NFOCKKMG@Hello?5World?$CB?6@		; `string'
EXTRN	__imp____stdio_common_vfprintf:PROC
EXTRN	__imp____acrt_iob_func:PROC
EXTRN	@__security_check_cookie@4:PROC
;	COMDAT ??_C@_0O@NFOCKKMG@Hello?5World?$CB?6@
CONST	SEGMENT
??_C@_0O@NFOCKKMG@Hello?5World?$CB?6@ DB 'Hello World!', 0aH, 00H ; `string'
CONST	ENDS
;	COMDAT ??_C@_0BC@KKMNGCGB@This?5is?5fun_1?5?$CFd?6@
CONST	SEGMENT
??_C@_0BC@KKMNGCGB@This?5is?5fun_1?5?$CFd?6@ DB 'This is fun_1 %d', 0aH, 00H ; `string'
CONST	ENDS
;	COMDAT ??_C@_0BC@CMFJBAMP@This?5is?5fun_2?5?$CFd?6@
CONST	SEGMENT
??_C@_0BC@CMFJBAMP@This?5is?5fun_2?5?$CFd?6@ DB 'This is fun_2 %d', 0aH, 00H ; `string'
CONST	ENDS
;	COMDAT ??_C@_0BC@OHAFMDGK@This?5is?5fun_3?5?$CFd?6@
CONST	SEGMENT
??_C@_0BC@OHAFMDGK@This?5is?5fun_3?5?$CFd?6@ DB 'This is fun_3 %d', 0aH, 00H ; `string'
CONST	ENDS
PUBLIC	_main
PUBLIC	?fun_1@@YAHH@Z					; fun_1
PUBLIC	?fun_2@@YAHH@Z					; fun_2
PUBLIC	?fun_3@@YAHH@Z					; fun_3
PUBLIC	_printf
PUBLIC	__vfprintf_l
PUBLIC	___local_stdio_printf_options
PUBLIC	?_OptionsStorage@?1??__local_stdio_printf_options@@9@4_KA ; `__local_stdio_printf_options'::`2'::_OptionsStorage
;	COMDAT ?_OptionsStorage@?1??__local_stdio_printf_options@@9@4_KA
_BSS	SEGMENT
?_OptionsStorage@?1??__local_stdio_printf_options@@9@4_KA DQ 01H DUP (?) ; `__local_stdio_printf_options'::`2'::_OptionsStorage
_BSS	ENDS
; Function compile flags: /Ogtp
;	COMDAT ___local_stdio_printf_options
_TEXT	SEGMENT
___local_stdio_printf_options PROC			; COMDAT
; File C:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\ucrt\corecrt_stdio_config.h
; Line 92
	mov	eax, OFFSET ?_OptionsStorage@?1??__local_stdio_printf_options@@9@4_KA ; `__local_stdio_printf_options'::`2'::_OptionsStorage
; Line 93
	ret	0
___local_stdio_printf_options ENDP
_TEXT	ENDS
; Function compile flags: /Ogtp
;	COMDAT __vfprintf_l
_TEXT	SEGMENT
__Locale$dead$ = 8					; size = 4
__ArgList$ = 12						; size = 4
__vfprintf_l PROC					; COMDAT
; __Stream$ = ecx
; __Format$ = edx
; File C:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\ucrt\stdio.h
; Line 644
	push	ebp
	mov	ebp, esp
; Line 645
	push	DWORD PTR __ArgList$[ebp]
	push	0
	push	edx
	push	ecx
	call	___local_stdio_printf_options
	push	DWORD PTR [eax+4]
	push	DWORD PTR [eax]
	call	DWORD PTR __imp____stdio_common_vfprintf
	add	esp, 24					; 00000018H
; Line 646
	pop	ebp
	ret	0
__vfprintf_l ENDP
_TEXT	ENDS
; Function compile flags: /Ogtp
;	COMDAT _printf
_TEXT	SEGMENT
__Format$ = 8						; size = 4
_printf	PROC						; COMDAT
; File C:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\ucrt\stdio.h
; Line 956
	push	ebp
	mov	ebp, esp
	push	esi
; Line 960
	mov	esi, DWORD PTR __Format$[ebp]
	push	1
	call	DWORD PTR __imp____acrt_iob_func
	add	esp, 4
; Line 645
	lea	ecx, DWORD PTR __Format$[ebp+4]
	push	ecx
	push	0
	push	esi
	push	eax
	call	___local_stdio_printf_options
	push	DWORD PTR [eax+4]
	push	DWORD PTR [eax]
	call	DWORD PTR __imp____stdio_common_vfprintf
	add	esp, 24					; 00000018H
; Line 962
	pop	esi
; Line 963
	pop	ebp
	ret	0
_printf	ENDP
_TEXT	ENDS
; Function compile flags: /Ogtp
;	COMDAT ?fun_3@@YAHH@Z
_TEXT	SEGMENT
?fun_3@@YAHH@Z PROC					; fun_3, COMDAT
; _i$dead$ = ecx
; File C:\Users\lib\source\repos\ida07\ida07\ida07.cpp
; Line 5
	push	4
	push	OFFSET ??_C@_0BC@OHAFMDGK@This?5is?5fun_3?5?$CFd?6@
	call	_printf
	add	esp, 8
; Line 6
	mov	eax, 1
; Line 7
	ret	0
?fun_3@@YAHH@Z ENDP					; fun_3
_TEXT	ENDS
; Function compile flags: /Ogtp
;	COMDAT ?fun_2@@YAHH@Z
_TEXT	SEGMENT
?fun_2@@YAHH@Z PROC					; fun_2, COMDAT
; _i$dead$ = ecx
; File C:\Users\lib\source\repos\ida07\ida07\ida07.cpp
; Line 11
	push	3
	push	OFFSET ??_C@_0BC@CMFJBAMP@This?5is?5fun_2?5?$CFd?6@
	call	_printf
; Line 5
	push	4
	push	OFFSET ??_C@_0BC@OHAFMDGK@This?5is?5fun_3?5?$CFd?6@
	call	_printf
	add	esp, 16					; 00000010H
; Line 12
	mov	eax, 1
; Line 13
	ret	0
?fun_2@@YAHH@Z ENDP					; fun_2
_TEXT	ENDS
; Function compile flags: /Ogtp
;	COMDAT ?fun_1@@YAHH@Z
_TEXT	SEGMENT
?fun_1@@YAHH@Z PROC					; fun_1, COMDAT
; _i$dead$ = ecx
; File C:\Users\lib\source\repos\ida07\ida07\ida07.cpp
; Line 17
	push	2
	push	OFFSET ??_C@_0BC@KKMNGCGB@This?5is?5fun_1?5?$CFd?6@
	call	_printf
; Line 11
	push	3
	push	OFFSET ??_C@_0BC@CMFJBAMP@This?5is?5fun_2?5?$CFd?6@
	call	_printf
; Line 5
	push	4
	push	OFFSET ??_C@_0BC@OHAFMDGK@This?5is?5fun_3?5?$CFd?6@
	call	_printf
	add	esp, 24					; 00000018H
; Line 18
	mov	eax, 1
; Line 19
	ret	0
?fun_1@@YAHH@Z ENDP					; fun_1
_TEXT	ENDS
; Function compile flags: /Ogtp
;	COMDAT _main
_TEXT	SEGMENT
_main	PROC						; COMDAT
; File C:\Users\lib\source\repos\ida07\ida07\ida07.cpp
; Line 24
	push	OFFSET ??_C@_0O@NFOCKKMG@Hello?5World?$CB?6@
	call	_printf
; Line 17
	push	2
	push	OFFSET ??_C@_0BC@KKMNGCGB@This?5is?5fun_1?5?$CFd?6@
	call	_printf
; Line 11
	push	3
	push	OFFSET ??_C@_0BC@CMFJBAMP@This?5is?5fun_2?5?$CFd?6@
	call	_printf
; Line 5
	push	4
	push	OFFSET ??_C@_0BC@OHAFMDGK@This?5is?5fun_3?5?$CFd?6@
	call	_printf
	add	esp, 28					; 0000001cH
; Line 26
	xor	eax, eax
	ret	0
_main	ENDP
_TEXT	ENDS
END
