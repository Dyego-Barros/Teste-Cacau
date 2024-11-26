from manipulation_file.ManipulationFile import ManupulationFile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


#Instância da classe ManupulationFile
obj = ManupulationFile()
#Verifica conexão com a internet
internet = obj.ConnectioVerify()
if not internet:
    print("Máquina não possui conexão com a internet!")
    ManupulationFile.Logs("Falha na conexão com a internet, automação interrompida")
    sys.exit()

# Realiza o download e extração dos dados da planilha
download_file = obj.DownloadFile("http://localhost:3000/download")
extract_data = obj.ExtractFile(download_file['File'])

# Inicia o Selenium WebDriver
driver = webdriver.Chrome()
driver.get("http://localhost:3000")


time.sleep(3)

def required_field(driver):    
    # Busca todos os campos obrigatórios na página
    required_fields = driver.find_elements_by_xpath("//*[@required]")
    fields_any = []
    
    for field in required_fields:
        value = field.get_attribute("value")
        if not value:  # Se o campo não estiver preenchido
             fields_any.append(field)
    
    if  fields_any:
        print("Campos obrigatórios não preenchidos:")
        for campo in  fields_any:
            print(campo.get_attribute("name") or campo.get_attribute("id") or "campo sem nome/id")
        return True
    return False

def slow_typing(element, text, delay=0.1):
    #Caso a digitação precise ser mais devagar, já atuei em casos em que o sistema identificava robos pelo velocidade da digitação
    for character in text:
        element.send_keys(character)
        time.sleep(delay)  # Atraso entre os caracteres

for index, row in extract_data.iterrows():
    try:
        # Encontre os campos do formulário
        nome_input = driver.find_element_by_name('Nome')  
        email_input = driver.find_element_by_name('Email')  
        idade_input = driver.find_element_by_name('Idade')  
        0

        # Preencher os campos com os dados da planilha
        nome_input.send_keys(row['Nome'])
        email_input.send_keys(row['Email'])
        idade_input.send_keys(row['Idade'])

        # Verificar se todos os campos obrigatórios foram preenchidos
        if required_field(driver):
            print(f"Erro ao preencher o formulário para a linha {index}: Campos obrigatórios não preenchidos.")
            obj.Logs(f"Erro ao preencher o formulário para a linha {index}: Campos obrigatórios não preenchidos.")
            continue  

        # Envia o formulário 
        idade_input.send_keys(Keys.RETURN)  

        # Esperar o envio (simulando o tempo para a página de envio ou recarga)
        time.sleep(3)
        
    except Exception as e:
        obj.Logs(f"Erro ao preencher o formulário {e}")
        print(f"Erro ao preencher o formulário para a linha {index}: {e}")

# Fechar o navegador depois que tudo estiver preenchido
driver.quit()
obj.Logs(f"Automação executada com sucesso!")

