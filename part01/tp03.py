def fib(n: int) -> None:    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(max=1000):    # write Fibonacci series up to n
    """Return a Fibonacci series up to n."""
    a, b = 0, 1
    the_list = []
    while a < max:
        the_list.append(a)
        a, b = b, a+b

    return the_list


the_global_var = 1000


def test_scope():
    the_var = 2
    the_global_var = 12
    print("the_global_var"+str(the_global_var))
    print("local the_global_var"+str(the_global_var))


fib(1000)
result = fib2(10)  # [0,1,1,2,3,5,8]
print(result)
test_scope()
print("after the_global_var"+str(the_global_var))


a = fib2(10)
print(a)
a = fib2(max=12)
print(a)


print(50*'-')


def add(*values):
    print(values)
    r = 0
    for i in values:
        # r=r+i
        r += i
    return r


values = [1, 2, 3, 4]
r = add(*values)  # 10
r = add(1, 2, 3, 4)  # 10
r = add(*[1, 2, 3, 4])  # 10
# r = add(1,2,3) # 10
# r = add(1,2,3,45,87) # 10
print("titi", "tutu", "truc", sep=";")


values = [1, 2, 3, 4]

[a, b, *d] = values
print(a, b, d)
a, b, *v = values
print(v)


def hello(name, first_name, /):
    # def hello(**kwargs):
    # print(kwargs)
    # print("Hello",kwargs['name'],kwargs['first_name'])
    print("Hello", name, first_name)

# hello("GAURAT",'Fred')
# hello(first_name='Fred',name="GAURAT",age="46",height="1,70m")


print(50*'-')


def mult2(v):
    return v*2


the_list = [1, 2, 3, 4]


the_list2 = map(lambda v: v*2, the_list)

the_list = list(the_list2)
print("loop")
print(the_list)
for i in the_list:
    print(i)
