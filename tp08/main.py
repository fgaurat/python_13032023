import json 

def main  ():
    with open("tp08\data.csv") as source_file:
        data_to_write = []
        all_data = source_file.readlines()
        
        header = all_data[0].strip().split(';')
        
        # les_autres_lignes = all_data[1:]
        les_autres_lignes = [d.strip() for d in all_data[1:]]
        
        for d in all_data[1:]:
            les_autres_lignes.append(d.strip())
        
        for line in les_autres_lignes:
            value = line.strip().split(';')
            print(dict(zip(header,value)))
            data_to_write.append(dict(zip(header,value)))

    with open('tp08\data_02.json',"w") as f:
        json.dump(data_to_write, f)
            
            
    
def main_for():
    with open("tp08\data.csv") as source_file:
        data_to_write = []
        for num_line,line in enumerate(source_file):
            clean_line = line.strip()
            if num_line == 0: # lecture des clefs
                header = clean_line.split(";")
            else:# lecture des valeurs
                value = clean_line.split(";")
                print(dict(zip(header,value)))
                data_to_write.append(dict(zip(header,value)))

        with open('tp08\data_01.json',"w") as f:
            json.dump(data_to_write, f)
            
            

def main_write_csv():
    with open("tp08\data.json") as source_file:
        list_of_all_data = json.load(source_file)
    
    
    with open("tp08\data.csv","w") as destination_file:
        print(*list_of_all_data[0].keys(),sep=";",file=destination_file)
        for d in list_of_all_data:
            print(*d.values(),sep=";",file=destination_file)
        



if __name__=='__main__':
    main()

