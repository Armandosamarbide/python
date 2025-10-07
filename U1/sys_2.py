import sys

## Nombre del archivo
print(sys.argv[0]) 

## Argumento 1
print(sys.argv[1]) 

## Argumento 2
print(sys.argv[2]) 

## Argumento 3
print(sys.argv[3]) 

print(sys.argv)

print(type(sys.argv))
print(len(sys.argv))
print(type(sys.argv[1:]))

## El comando de ejecución es py sys_2.py A B C, donde A, B y C son los argumentos