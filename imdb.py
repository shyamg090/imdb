def display(a,b):
        print('------------')
        print(a,b)
        print('------------')
def ratem():
    global movie,rate,n
    print('how many movies??')
    n=int(input())
    if n==0:
        print('please enter a number')
    else:    
        for i in range(0,n):
            print('enter the movie name')
            movie=input()
            print('enter the rating')
            rate=input()
        
    display(movie,rate)

    
print('hello user!!')
print('if new user! type 1 else 2')
new=int(input())
if new==1:
    print("enter your name")
    name=input()
    print('sucessfully registerd')
    ratem()
else:
    ratem()



