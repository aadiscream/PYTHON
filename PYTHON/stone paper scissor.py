from random import randrange
# stone = -1 
# paper =0
# scissor=1
def fullfomr(x):
   if(x==1):
      return "scissor"
   elif(x==0):
      return 'paper'
   else:
      return 'stone'
print("ENTER\n1 FOR STONE\n2 FOR PAPER\n3 FOR SCISSOR")
point=0
game=True
while(game==True):
   computer=(randrange(-1,2))
   user=int(input("\nyour turn : "))
   if(computer==1 and user==1):#draw
      print(f'you :{fullfomr(user)}\ncomp : {fullfomr(computer)}')
      print(f"draw \nyour current point = {point}+0")
   elif(computer==1 and user==-1):#win
      print(f'you :{fullfomr(user)}\ncomp : {fullfomr(computer)}')
      print(f"you won\nyour current point = {point+1}")
   elif(computer==1 and user==0):
      print(f'you :{fullfomr(user)}\ncomp : {fullfomr(computer)}')
      print(f"you lost\nyour current point = {point}")
      game=False
   elif(computer==0 and user==1):#win
      print(f'you :{fullfomr(user)}\ncomp : {fullfomr(computer)}')
      print(f"you won\nyour current point = {point+1}")
   elif(computer==0 and user==0):#draw
      print(f'you :{fullfomr(user)}\ncomp : {fullfomr(computer)}')
      print(f"draw\nyour current point = {point}+0")
   elif(computer==0 and user==-1):
      print(f'you :{fullfomr(user)}\ncomp : {fullfomr(computer)}')
      print(f"you lost\nyour current point = {point}")
      game=False
   elif(computer==-1 and user==1):
      print(f'you :{fullfomr(user)}\ncomp : {fullfomr(computer)}')
      print(f"you lost\nyour current point = {point}")
      game=False
   elif(computer==-1 and user==0):#win
      print(f'you :{fullfomr(user)}\ncomp : {fullfomr(computer)}')
      print(f"you won\nyour current point = {point+1}")
   else:#draw
      print(f'you :{fullfomr(user)}\ncomp : {fullfomr(computer)}')
      print(f"draw\nyour current point = {point}+0")
   point+=1
    
