import csv
import requests
import os

def download_and_save(url,folder,folder_label,file_name, file_name_labeled):
    headers = {
    'Authorization': 'token <token>'
    }
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            file_path = os.path.join(folder, file_name)
            file_path_labeled =  os.path.join(folder_label, file_name_labeled)

            with open(file_path, 'wb') as f:
                f.write(response.content)
            print("nome escrito  com sucesso")
            with open(file_path_labeled, 'wb') as f:
                f.write(response.content)
        else:
            print(f"Falha ao baixar o arquivo {url}, Status code: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar baixar o arquivo {url}: {e}")








def main():
    csv_file = 'MLCQCodeSmellSamples copy.csv'
    folder = './smells'
    folder_label = './smells_label'

    #abrir o arquivo
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        count = 0
        for row in reader:
            count +=1
            if row:
                # pegar a url
                url = row[13]

                # tratar a url
                url = url.replace('github',"raw.githubusercontent")
                url = url.replace('/blob/',"/")
                url = url.rsplit('/', 1)[0]

                file_name = url.split("/")[-1]
                # ------------------------------------------------------
                id = row[0]
                reviewer_id = row[1]
                sample_id = row[2]
                smell = row[3]
                severity = row[4]
                typeSmell = row[6]
                commit_hash = row[9]
                start_line = row[11]
                end_line = row[12]
                is_from_industry_relevant_project = row[14]

                file_name_labeled = "" + id + "_" + reviewer_id + "_" + sample_id + "_" + smell + "_" + severity + "_" + typeSmell + "_" + commit_hash + "_" + start_line + "_" + end_line + "_" + is_from_industry_relevant_project + "_" + file_name

                # print("file name is ")
                # print(file_name)
                # print(file_name_labeled)
                print(count)
                download_and_save(url,folder,folder_label,file_name, file_name_labeled)








                
    # criar nome
    #criar nome labeled

    #salvar nas pastas









if __name__ == "__main__":
    main()