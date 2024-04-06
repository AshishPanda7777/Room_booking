def single_ton(func):
    L=[]
    def inner(*args,**kwargs):
        if len(L)==0:
            L.append(func())
        return L[0]
    return inner
@single_ton   
class xyz:
    def __init__(self):
        self.room=100
    def booking(self):
        room=int(input('Enter howmany rooms you required ? :'))
        if(self.room>=room):
            self.room-=room
            print('Your Room Booked Succesfully')
            print(f'Available rooms are={self.room}')
        else:
            print(f'Available rooms are ={self.room}')
@single_ton 
class mno:
    def __init__(self):
        self.room=100
    def booking(self):
        room=int(input('Enter howmany rooms you required ? :'))
        if(self.room>=room):
            self.room-=room
            print('Your Room Booked Succesfully')
        else:
            print(f'Available rooms are ={self.room}')
@single_ton 
class abc:
    def __init__(self):
        self.room=100
    def booking(self):
        room=int(input('Enter howmany rooms you required ? :'))
        if(self.room>=room):
            self.room-=room
            print('Your Room Booked Succesfully')
        else:
            print(f'Available rooms are ={self.room}')
@single_ton 
class pqr:
    def __init__(self):
        self.room=100
    def booking(self):
        room=int(input('Enter howmany rooms you required ? :'))
        if(self.room>=room):
            self.room-=room
            print('Your Room Booked Succesfully')
        else:
            print(f'Available rooms are ={self.room}')
def room_book():
      print('Choose Which hotel You required ')
      print('1.xyz\n2.mno\n3.abc\n4.pqr')
      book=int(input('Choose Hotel :'))
      if book==1:
          x1=xyz()
          x1.booking()
      elif(book==2):
          m1=mno()
          m1.booking()
      elif(book==3):
          a1=abc()
          a1.booking()
      elif(book==4):
          p1=pqr()
          p1.booking()
      else:
          print('This Hotel is not available.....')  
          
while(True):
    room_book()
    print('**********************************************\n*********************************************')
       

          
          
        