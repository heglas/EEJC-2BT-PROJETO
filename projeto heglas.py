import pandas as pd

def cadastro_de_livros(df):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano de publicação: "))
    capitulos = int(input("Digite o número de capítulos: "))
    
    novo_livro = pd.DataFrame({
        'Nome': [nome],
        'Autor': [autor],
        'Ano': [ano],
        'Capitulos': [capitulos]
    })
    
    df = pd.concat([df, novo_livro], ignore_index=True)
    print("Livro cadastrado com sucesso.")
    return df
    
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


