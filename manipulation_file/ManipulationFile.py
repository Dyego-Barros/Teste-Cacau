import requests
import pandas as pd
import os
from datetime import datetime
import socket

class ManupulationFile:

    def DownloadFile(self,url) -> dict:
        try:
            #Faz a requisição para url, para baixar o arquivo
            response = requests.get(url=url)
            filename = ""
            if response.status_code ==200:
                file = response.content
                #Pega o filename do arquivo baixado caso esteja presente no header da requesição
                content_disposition = response.headers.get('Content-Disposition','')
                if 'filename=' in content_disposition:
                    filename= content_disposition.split('filename=')[1].strip('\"')
                else:
                    #Seta um nome base usando a url caso falhe
                    filename = os.path.basename(url)                   
                
                #Verifica se o diretorio existe e salva o arquivo no diretorio
                if os.path.exists("processed_files"):
                    new_name = f'{datetime.now().strftime("%Y-%m-%d")}-{filename}'
                    end_path = os.path.join('processed_files', new_name)                    
                    with open(end_path, 'wb') as f:
                        f.write(file)
                    print(f"Download do arquivo : {filename} realizado.")
                    return {"Authorized": True, "File": new_name}
                else:
                    #Caso o diretorio não exista ele cria o diretorio
                    os.makedirs("processed_files")
                    new_name = f'{datetime.now().strftime("%Y-%m-%d")}-{filename}'
                    end_path = os.path.join('processed_files', new_name)                    
                    with open(end_path, 'wb') as f:
                        f.write(file)
                    print(f"Download do arquivo : {filename} realizado.")
                    return {"Authorized": True, "File": new_name}
        except Exception as err:
            self.Logs(f'Falha ao realizar download do arquivo {err}')
            print(f"Falha ao realizar download do arquivo!")
            return {"Authorized": False, "Error": err}
  
    def ExtractFile(self,file: str):
        try:
           data = pd.read_excel(f'./processed_files/{file}', engine='openpyxl')
           if len(data)> 0:
               return data
           else:
               data ={}
               return data
        except Exception as err:
          self.Logs(f'Ocorreu um error ao tentar ler o arquivo {err}')
          print('Ocorreu um error ao tentar ler o arquivo: %s', file)
          print("Error:%s", err)
          data= {}
          return data
      
    def ConnectioVerify(self):
        try:
            socket.create_connection(("www.google.com", 80), timeout=5)
            print("Máquina conectada a internet")
            return True
        except(socket.timeout, socket.gaierror):
            self.Logs(f'Ocorreu um error ao verificar conexão coma internet {socket.gaierror}')
            print("Sem conexão com a Internet")
            return False
    
    def Logs(self,msg: str):
        try:
          with open('logs.txt','a') as f:
              f.write(f'\n {datetime.now().strftime("%Y-%m-%d")}  {msg}')
          return True
        except Exception as err:
           with open('logs.txt','a') as f:
              f.write(f'\n {datetime.now().strftime("%Y-%m-%d")}  {err}')
           return False