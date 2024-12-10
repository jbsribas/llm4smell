import os
import csv

file_name = ''
folder = ''



def main():
    # file_name = 'MLCQCodeSmellSamples - Página2.csv'
    file_name = 'MLCQCodeSmellSamples.csv'
    folder = 'smells_label'


    print("this is a main")
    with open(file_name, mode='r') as file:
        count = 0
        reader = csv.reader(file)
        linhas_validas = []
        for row in reader:
            if row:
                 # pegar a url
                url = row[13] # col N

                # tratar a url
                url = url.replace('github',"raw.githubusercontent")
                url = url.replace('/blob/',"/")
                url = url.rsplit('/', 1)[0]

                file_name = url.split("/")[-1]
                # ------------------------------------------------------
                id = row[0] # col A
                reviewer_id = row[1] # col B
                sample_id = row[2] # col C
                smell = row[3] # col D
                severity = row[4] # col E 
                typeSmell = row[6] # col G
                commit_hash = row[9] # col J
                start_line = row[11] # col L
                end_line = row[12] # col M
                is_from_industry_relevant_project = row[14] # col O

                file_name_labeled = "" + id + "_" + reviewer_id + "_" + sample_id + "_" + smell + "_" + severity + "_" + typeSmell + "_" + commit_hash + "_" + start_line + "_" + end_line + "_" + is_from_industry_relevant_project + "_" + file_name
                # print(file_name_labeled)
                caminho_completo = os.path.join(folder, file_name_labeled)
                if os.path.isfile(caminho_completo):
                    # print()
                    # print(caminho_completo)
                    # print()
                    # count += 1
                    # print(count)
                    linhas_validas.append(row)  # Adicionar a linha à lista de válidos
                # else:
                    # print("nao foi")
        with open("smells_filtered.csv", mode='w', newline='', encoding='utf-8') as novo_csv:
            escritor_csv = csv.writer(novo_csv)
            escritor_csv.writerows(linhas_validas)  # Escrever as linhas válidas

if __name__ == "__main__":
    main()