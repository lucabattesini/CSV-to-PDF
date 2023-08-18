import pandas as pd

df = pd.read_csv("./files/input/data.csv")

file_name = "text.md"

colunas = df.columns
with open(file_name, 'w') as txt_file:
    txt_file.write("")

def write_title(title) :
    with open(file_name, 'a') as txt_file:
            txt_file.write(f'# {title}\n')

def write_subtitle(subtitle) :
    with open(file_name, 'a') as txt_file:
        txt_file.write(f'### {subtitle}\n')

def div() :
    with open(file_name, 'a') as txt_file:
            txt_file.write('\n----\n')

def write_h3(title, value) :
     with open(file_name, 'a') as txt_file:
        txt_file.write(f'### {title}: \n        {value}\n\n')


for i, linha in df.iterrows():
    for nome_coluna in colunas:
        valor = df.loc[i, nome_coluna]
        if nome_coluna == "name":
            write_title(valor)

        elif nome_coluna == "phone":
             write_subtitle(valor)

        elif nome_coluna == "email":
             write_subtitle(valor)

        elif nome_coluna == "list":
             write_h3("Brand", valor)

        elif nome_coluna == "url":
             write_h3("Perfil link", valor)
        else:
            with open(file_name, 'a') as txt_file:
                txt_file.write(f'### Description:\n')
            with open(file_name, 'a') as txt_file:
                txt_file.write(f'> {valor}\n\n\n')
    div()