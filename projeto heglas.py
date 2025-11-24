import pandas as pd

dados_livros = {
    'Nome': ['EU, ROBÔ', 'BLADE RUNNER', 'DOM CASMURRO'],
    'Autor': ['ISAAC ASIMOV', 'PHLLIP K. DICK', 'MACHADO DE ASSIS'],
    'Ano': [1950, 1968, 1899],
    'Capitulos': [9, 21, 148]
}

df_livros = pd.DataFrame(dados_livros)
def atualizar_livro(df, indice, nome=None, autor=None, ano=None, capitulos=None):
 
    if indice < 0 or indice >= len(df):
        print("Índice inválido.")
        return df
    
    if nome is not None:
        df.at[indice, 'Nome'] = nome
    if autor is not None:
        df.at[indice, 'Autor'] = autor
    if ano is not None:
        df.at[indice, 'Ano'] = ano
    if capitulos is not None:
        df.at[indice, 'Capitulos'] = capitulos
    
    print(f"Livro no índice {indice} atualizado com sucesso.")
    return df

print("\nDataFrame após atualização:")
print(df_livros)