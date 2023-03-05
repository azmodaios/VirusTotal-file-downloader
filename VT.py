import requests
import plyer
import os
import datetime

logo = """\ _    ___                    ______      __        __   ____                      __                __
| |  / (_)______  _______   /_  __/___  / /_____ _/ /  / __ \____ _      ______  / /___  ____ _____/ /__  _____
| | / / / ___/ / / / ___/    / / / __ \/ __/ __ `/ /  / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / _ \/ ___/
| |/ / / /  / /_/ (__  )    / / / /_/ / /_/ /_/ / /  / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ /  __/ /
|___/_/_/   \__,_/____/    /_/  \____/\__/\__,_/_/  /_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/\___/_/
 V1.0.1                                                                                      by L_Ryuzaki                                                                                                         
                                                                                                          """
print(logo)
print(datetime.datetime.now())

def create_folder():
    mkdir= 'mkdir Results'
    if not os.path.exists('Results'):
        return os.system(mkdir)

def get_api_key():
    return str(input("\033[0;34m Enter API Key: \033[0m"))#enter your API from VT

def get_file_path():
   return  plyer.filechooser.open_file(multiple=True) #select the txt file who contains the hashes

def get_file_format():
    return str(input("\033[0;34m Enter file format: \033[0m"))#select the output format of the file

def download_file(hash, api, file_format, index):
    url = f"https://www.virustotal.com/api/v3/files/{hash}/download"
    r = requests.get(url, headers={'x-apikey': api})
    data = r.content
    with open(f"./Results/{hash}{index}.{file_format}", mode='wb') as f:    # requires a folder called 'Results'
        f.write(data)

def main():
    create_folder()
    api_key = get_api_key()
    file_format = get_file_format()
    ask = int(input("\033[0;34m Enter hash to Download press:[1] \n"
                    " Select file press:[2] \033[0m"))
    if ask == 1:
        hash = str(input("\033[0;34m Enter Hash: \033[0m"))
        i = hash
        download_file(hash,api_key,file_format,i)
        print("\033[0;34m Successfully downloaded!\033[0m")
    else:
        file_path = get_file_path()
        if file_path is not None:
            for file_path in file_path:
                with open(file_path) as f:
                    hashes = f.readlines()
                    for i, hash in enumerate(hashes):
                        hash = hash.strip()
                        download_file(hash, api_key, file_format, i)
                        print("\033[0;34m Successfully downloaded \033[0m")

if __name__ == "__main__":
    main()


