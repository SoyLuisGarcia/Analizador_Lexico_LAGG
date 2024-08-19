#mi primer analizador lexico que solo me reconocer 
# numeros enteros, identificadores, operadores
# librerias: lexico, re

import re

#crear tokens
token_patterns = [
    ('NUMERO', r'\d+'),                      # Número entero
    ('IDENTIFICADOR', r'[A-Za-z]\w*'),       # Identificador
    ('SUMA', r'\+'),                         # Operador de suma
    ('RESTA', r'-'),                         # Operador de resta
    ('MULTIPLICACION', r'\*'),               # Operador de multiplicación
    ('DIVISION', r'/'),                      # Operador de división
    ('PARENTESIS_IZQ', r'\('),               # Paréntesis izquierdo
    ('PARENTESIS_DER', r'\)'),               # Paréntesis derecho
    ('ESPACIO', r'\s+'),                     # Espacios
    ('SIMBOLO', r'.'),                       # Otros caracteres
    ('FUNCION', r'function'),               #FUNCION
    ('RETORNO', r'return'),                   #Retono
    ('SI', r'if'),                            # SI
    ('SINO', r'else'),                        #SINO
    ('MIENTRAS', r'while'),                   #MIENTRAS
    ('PARA', r'for'),                         #PARA 
    ('FIN_DE_LINEA', r';'),                   #FIN DE LINEA
    ('COMENTARIO', r'//.*'),                  #COMENTARIO
    ('COMENTARIO_MULTILINEA', r'/\*[\s\S]*?\*/'), #COMENTARIO MULTILINEA
    ('CADENA', r'"[^"]*"'),                    #CADENA
    ('CARACTER', r"'[^']*'"),                  #CARACTER
    ('BOOLEANO', r'(true|false)'),             #BOOLEANO
    ('NULO', r'null'),                         #NULO
    ('ARROBA', r'@') ,                         #ARROBA
    ('DOS_PUNTOS', r':') ,                     #DOS PUNTOS
    ('PUNTO_Y_COMA', r';') ,                   #PUNTO Y COMA
    ('CORCHETE_IZQ', r'\[') ,                  #CORCHETE IZQ
    ('CORCHETE_DER', r'\]')  ,                 #CORCHETE DER
    ('%', r'%')    ,                           #MODULO
    ('IGUALDAD', r'=='),                       #IGUALDAD
    ('DIFERENTE', r'!=') ,                     #DIFERENTE
    ('MAYOR', r'>') ,                          #MAYOR QUE
    ('MENOR', r'<') ,                          #MENOR QUE
    ('MAYOR_IGUAL', r'>=') ,                   #MAYOR O IGUAL
    ('MENOR_IGUAL', r'<=') ,                   #MENOR O IGUAL
    ('ASIGNACION', r'=')  ,                    #ASIGNACION
 
]

# token expresiones regulares patrones
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns)
get_token = re.compile(token_regex).match

def tokenize(code):
    line_number = 1
    line_start = 0
    position = 0
    tokens = []

    while position < len(code):
        match = get_token(code, position)
        if not match:
            raise RuntimeError(f'Error de Analisis en posicion {position}')
        
        for name, value in match.groupdict().items():
            if value:
                if name != 'ESPACIO':
                    tokens.append((name, value))
                break
        position = match.end()

    return tokens  # Mover el return fuera del bucle while



code = "x = 2 + 4 * (2 - 8)"
tokens = tokenize(code)
for token in tokens:
    print(token)