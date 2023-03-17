import traceback

class DivBy12Error(Exception):
    
    def __init__(self):
        super().__init__("Division par 12")
        

def div(a,b):
    if b == 12:
        # raise Exception("Division par 12 !")
        raise DivBy12Error()
    c = a/b
    return c

def main():
    try:
        a = 2
        b = int(input("valeur de b : "))
        # c = a/b
        c = div(a, b)
        print(c)
        
    # except ZeroDivisionError as e:
    #     traceback.print_exc()
    #     print("erreur ZeroDivision",e)    
    # except TypeError as e:
    #     traceback.print_exc()
    #     print("erreur Type",e)    
    # except DivBy12Error as e:
    #     print("DivBy12Error",e)
    except Exception as e:
        # traceback.print_exc()
        print("All erreur Type",e)    
    else:
        print("pas d'erreur")
    
    
    print("après !!")
if __name__=='__main__':
    main()

