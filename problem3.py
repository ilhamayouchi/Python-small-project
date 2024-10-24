#Book Inventroy Managemnt System#
list_of_tuples=[]
def read_books(book: str) -> list :
    with open ('book.txt', 'r') as file :
        try :
           for line in file :
             book_id, title, author, price = line.strip().split(', ')
             list_of_tuples.append((book_id, title, author, float(price))) #append as a tuple with double (), Add the type of the variable price.#
        except FileNotFoundError:
            print("File Not Founded")
        except IOError :
            print("Error :could not open the file.")
        except ValueError :
            print("price is invalid.")
    return list_of_tuples
books= read_books('book.txt')
print(books)
def apply_discount(book: list ) -> list:
    discount_input=(input("Please enter the discounted price (e.g : 15 or 15%)"))
    if '%' in discount_input :
        try:
            discount_rate= float(discount_input.replace('%','').strip())
        except ValueError:
            print("The discounted price is invalid .Enter an valid rate.")
            return None
    else:
        try:
            discount_rate=float(discount_input.strip())
        except ValueError:
            print("Invalid discounted rate.Enter an valid rate.")
            return None
    discount_rate = discount_rate/100
    print(f" Well Done\n")
    print(f"All the books prices in the store will be discounted by {discount_rate} %")
    with open ('discounted_book.txt', 'a') as file : # to add content to the file #
      # # there is no need for a loop to scroll over the file cause it's empty #
           # for i,(book_id,title,auther,price) in enumerate(list_of_tuples,start=1) :
               # new_price = price - (price*discount_rate)
                #file.write(f"{book_id},{title},{auther},{new_price:.2f}\n")
              #  list_of_tuples[i-1]=(book_id,title,auther,new_price) ## Tuples are immutable, can't modify them directly. 
              return None
def write_discounted_books()->None :
    with open ('discounted_book.txt','r') as file :
        for line in file:
          existing_lines=line.readline()
          print("books dicounted","" .join(existing_lines))
# Unit test #
def test_discounted():
    discounted_rate=0.5
    excepted_price=4.5
    original_price=9
    new_price=original_price - (original_price*discounted_rate)
    assert new_price==excepted_price
 #def writing_function():#
    # To confirm that the data is written correctly to the output file #



def main():

    dicount=apply_discount(list_of_tuples)
    print(dicount)
    test=test_discounted()
    affiche=write_discounted_books()
    print(affiche)
main()



    



            

        




        


    
