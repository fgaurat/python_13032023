def main():
    age = 46
    s = f"age  : {age}" # fstring
    print(s)

    a = 3
    b = 2
    c = b/a
    print(f"{a}/{b} = {c:.2%}")
    
    name = "GAURAT"
    firstname = "Fred"
    
    print(f'{name:>10} {firstname}')    
    
    the_list = ["toto","tata","tutu"]

    print(f"{the_list[0]} ")
    s = "{0} {1} {2}".format(the_list[0],the_list[1],the_list[2])
    s = "{} {} {}".format(the_list[0],the_list[1],the_list[2])
    s = "{1} {0} {2}".format(*the_list)
    print(s)
    
    d = {"name":"GAURAT","firstname":"Frédéric","age":46}
    s = "{name} {firstname} {age}".format(name=d['name'],firstname=d["firstname"],age=d['age'])
    print(s)
    s = "{name} {firstname} {age}".format(**d)
    print(s)
    name = "GAURAT"
    firstname = "Fred"
    s = f"{name=} {firstname=:>10}"
    print(s)
    
        
if __name__=='__main__': 
    main()

