# def div(n1,n2):
#     if n1>n2:
#         (n1,n2)=(n2,n1)
#     return n1/n2
# def sub(n1,n2):
#     if n1>n2:
#         (n1,n2)=(n2,n1)
#     return n1-n2

#Here if n1>n2: , (n1,n2)=(n2,n1) are same in both functions so we should not repeat it.
#DRY--->Do not Repeat Yourself.
#So we use decorator function write the features.
def swap_dec(fn):
    def wrapper(n1,n2): #Here if we are having more then 2 values use *arg and *karg.
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper #No need to use the brackets.

@swap_dec #Here we are adding feature using decorate function without changing the definition.
def div(n1,n2):
    return n1/n2

@swap_dec
def sub(n1,n2):
    return n1-n2

print(div(2,10))
print(sub(2,10))

