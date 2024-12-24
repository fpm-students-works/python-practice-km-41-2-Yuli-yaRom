import factorial.factorial 
import logarithm.logarithm
import exp_root.exponentiation
import exp_root.root
def inpcheck(txt, i, a):
    while(True):
        x = input(txt)
        try:
            if i == "int":
                x = int(x)
            if i == "float":
                x = float(x)
            if a > 0:
                if x <= 0:
                    raise TypeError
            break
        except ValueError:
            print(f"Your number is not {i}")
        except TypeError:
            print("Insert a positive number.")
    return x

def inpcheck1(txt, i, a):
    while(True):
        x = inpcheck(txt, i, a)
        if x != 1:
            break
        else:
            print("The number cant equal 1")
    return x 

def main():
    inp1 = input("What func would you like to use? We have: fact, log, lg, ln, exp2, exp3, root2, root3 ")
    if inp1 == "fact":
        a1 = inpcheck("Insert a number", "int", 5)
        print(factorial.factorial.fact(a1))
    elif inp1 == "log":
        a1 = inpcheck("Insert a number", "float", 5)
        a = inpcheck1("Insert the base", "float", 5)
        print(logarithm.logarithm.log(a, a1))
    elif inp1 == "lg":
        a1 = inpcheck("Insert a number", "float", 5)
        print(logarithm.logarithm.lg(a1))
    elif inp1 == "ln":
        a1 = inpcheck("Insert a number", "float", 5)
        print(logarithm.logarithm.ln(a1))
    elif inp1 == "exp2":
        a1 = inpcheck("Insert a number", "float", 0)
        print(exp_root.exponentiation.exp2(a1))
    elif inp1 == "exp3":
        a1 = inpcheck("Insert a number", "float", 0)
        print(exp_root.exponentiation.exp3(a1))
    elif inp1 == "root2":
        a1 = inpcheck("Insert a number", "float", 5)
        print(exp_root.root.root2(a1))
    elif inp1 == "root3":
        a1 = inpcheck("Insert a number", "float", 0)
        print(exp_root.root.root3(a1))
    else:
        print("Insert one of the things on the list.")
    
main()

if __name__ == "main.py":
    main()