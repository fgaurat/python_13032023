import requests
from bs4 import BeautifulSoup
import glob
import re



def main():
    logs = glob.glob('*.log')
    cpt=0
    for log in logs:
        with open(log) as f:
            for line in f:
                line = line.strip()
                result = re.findall(r'\"\s(\d{3})\s',line)
                if '404' in result:
                    print(line)
                    cpt+=1

    print(cpt)
def main_ip():
    logs = glob.glob('*.log')
    for log in logs:
        with open(log) as f:
            for line in f:
                line = line.strip()
                # result = re.findall(r'^((\d{1,3}\.){3}\d{1,3})',line)
                # result = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',line)
                result = re.findall(r'^(.+?)\s',line)
                print(result)





def main_download():

    url="http://logs.eolem.com/"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    all_a = soup.find_all('a')
    
    log_files = []
    # log_files = [url+a['href'] for a in all_a if ".log" in a['href']]
    
    for a in all_a:
        if ".log" in a['href']:
            # print(a.get('href'))
            print(url+a['href'])
            # log_url = f"{url}{a['href']}"
            log_files.append(url+a['href'])

    for url_log_file in log_files:
        file_name = url_log_file.split("/")[-1]
        response = requests.get(url_log_file)
        with open(file_name,'w') as f:
            f.write(response.text)
if __name__=='__main__':
    main()

