import requests
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog

def get_api_key():
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askstring("api", prompt="Enter API Key:") #enter your API from VT

def get_file_path():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename() #select the txt file who contains the hashes

def get_file_format():
    root = tk.Tk()
    root.withdraw()
    return simpledialog.askstring("file_format", prompt="Enter file format:") #select the output format of the file

def download_file(hash, api, file_format, index):
    url = f"https://www.virustotal.com/api/v3/files/{hash}/download"
    r = requests.get(url, headers={'x-apikey': api})
    data = r.content
    with open(f"./Result/{hash}{index}.{file_format}", mode='wb') as f:    # requires a folder called 'Result'
        f.write(data)

def main():
    api_key = get_api_key()
    file_path = get_file_path()
    file_format = get_file_format()
    with open(file_path) as f:
        hashes = f.readlines()
    for i, hash in enumerate(hashes):
        hash = hash.strip()
        download_file(hash, api_key, file_format, i)

if __name__ == "__main__":
    main()

