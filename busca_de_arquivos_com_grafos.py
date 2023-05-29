import os
def procurar(file_name:str):
    fila : list = os.listdir('.')
    arquivos_pesquisados : int = 0
    diretorios_pesquisados : int = 0
    while fila:
        dire = fila.pop(0)
        if os.path.isfile(dire):
            arquivos_pesquisados += 1
            if '/' in dire:
                arquivo = dire[dire.rfind('/')+1:]
            else:
                arquivo = dire
            if file_name in arquivo:
                print(f'\n \n achei --->>> {dire}\n \n')
        elif os.path.isdir(dire):
            diretorios_pesquisados += 1
            for path in map(lambda x : f"{dire}/{x}", os.listdir(dire)):
                fila.append(path)
    print(arquivos_pesquisados,diretorios_pesquisados)

procurar('senhas')
procurar('busca')
