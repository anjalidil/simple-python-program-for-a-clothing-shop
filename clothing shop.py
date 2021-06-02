#this program is about store and print bill items of a bill receipt
#customer will get 15% discount ,if he purchase cloths worth more than RS.8,000/- .

class Node:
    def __init__(self,purchaseNum,value): #creating a new node
        self.data=value
        self.purchaseNum=purchaseNum
        self.next=None
        print("-----New Item is Added to the Bill-----")

class invoice:
    def __init__(self):   #creating a new queue 
        self.front = None
        self.rear = None
        #print("-----New Bill is Created -----\n")


    #add 
    def inputItems(self,new):
        if self.front==None: 
            self.front=new
            self.rear=new
        else:
            self.rear.next=new   
            self.rear=new


     
    def printInvoice(self):
        i=1
        if self.front == None:
            print("Queue is empty")
        else:
            temp=self.front
            print("\n~~~~~~~Bill Details~~~~~~~\n")
            while temp!=None:
                print("Item {0}: {1} -->".format(i,temp.data))  #printing Item Prices
                temp=temp.next
                i+=1
            

print("\n\t\t\t~~~~~~~~~~~~~~~~~~~~~Welcome to the Nolimit~~~~~~~~~~~~~~~~~~~~~~~~~\n\n");

c=1 #bill count
clothType=20
netPrice=0
inv=invoice()

while(clothType!=0):
    print("\t\t\tItem Code Catalogue\n\t\t\t\n\t1) Addidas T-Shirt- 1500.00\t\t4) Nike T-Shirt - 2000.00\n\t\n\t\n\t2) Denim Trouser - 2500.00\t\t5) Addidas Tracking Kit - 4000.00\n\t\n\t\n\t3) Check Shirt - 2000.00\t\t6) Leather Jacket - 2500.00\t\n");
    print("\n\t0) Exit from adding new Items to the bill\n\n");
            
		
    print(" Invoice {0}\n ~~~~~~~~~~~~~~\n".format(c))
		
    x = int(input("How many Item Types: "))
    
    for i in range(x):
        clothType = int(input("Enter code: "))
    
        if clothType == 1:
            Uprice = 1500.00
        elif clothType == 2:
            Uprice = 2500.00
        elif clothType == 3:
            Uprice = 3000.00
        elif clothType == 4:
            Uprice = 2000.00
        elif clothType == 5:
            Uprice = 1000.00
        elif clothType == 0: 
            break
            exit()
        else:
            print("invalid Cloth Type")
            continue
    
        qnty = int(input("Enter quantity: "))    
        price=Uprice*qnty  #calculate the price using unit price and quantity
        netPrice = netPrice+price
        
        node= Node(c,netPrice)
        inv.inputItems(node)
    
    if netPrice>8000:
        discount=0.15
    else:
        discount = 0
    finalPrice = netPrice-(netPrice*discount)
    
    

    c+=1  
    inv.printInvoice()
    print("\nDiscount: {0}".format(netPrice*discount))
    print("Final bill Amount: {0}\n\n\n".format(finalPrice))





    		
		
		
		
		
