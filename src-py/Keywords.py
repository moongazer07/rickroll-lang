from sys import stdout

# Keywords
KW_print        = 'showme'
KW_if           = 'if'

KW_let          = 'lint'
KW_assign       = 'mario'
KW_import1      = 'bring'
KW_import2      = "bring2"
KW_def          = 'egg'
KW_return1      = 'comeback'
KW_return2      = 'comeback2'
KW_try          = 'attempt'
KW_except       = 'xcept'
KW_main         = 'protagonist'
KW_end          = 'terminate'

KW_break        = 'rake'
KW_continue     = 'keepgoing'
KW_endless_loop = 'runforever'
KW_while_loop   = 'whilerun'

KW_L_OP = 'isinferiorthan'
KW_G_OP = 'issuperiorthan'
KW_GOE_OP = 'issuperiorthanorequalto'
KW_LOE_OP = 'isinferiorthanorequalto'
KW_is_not_OP = 'aint'
KW_E_OP = 'is'

KW_PY = "py:"

keywords = [
    KW_print,
    KW_if,
    KW_let,
    KW_assign,
    KW_import1,
    KW_import2,
    KW_def,
    KW_return1,
    KW_return2,
    KW_try,
    KW_except,
    KW_main,
    KW_end,
    KW_break,
    KW_continue,
    KW_endless_loop,
    KW_while_loop,
    KW_L_OP,
    KW_G_OP,
    KW_GOE_OP,
    KW_LOE_OP,
    KW_is_not_OP,
    KW_E_OP,

    KW_PY
]

INDENT_KW = [
KW_if, KW_def, KW_try, KW_except, KW_while_loop, KW_endless_loop
]


# Tokens that the interpreter will totally ignore
ignore_tokens = {'~', "'"}

# Characters in numbers
digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}

# Separators are used in tokenization
separators = {
    '(', ')', '[', ']', '{', '}', ',', '\n', ' ', '+', '-', '*', '/', '%', '^', '='
}

# Operators
operators = {
    '+', '-', '*', '/', '%', '^', '=',
    '[', ']', '(', ')', '{', '}', ',',
    '>', '<', '<=', '>=', '!=', 'is', 'aint'
}
OP_build_in_functions = {'to_string', 'to_int', 'to_float', 'length'}

def join_list(l):
    return ''.join(map(str, l))
