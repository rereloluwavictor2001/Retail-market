import time
class Retail_market():
    def __init__ (self):
        self.stock = {
           "Sugar":{"Available Quantity":152, "Price per quantity(N)":50},
           "Bread(sliced)":{"Available Quantity":311, "Price per quantity(N)":200},
           "Bread(unsliced)":{"Available Quantity":229, "Price per quantity(N)":150},
           "Egg":{"Available Quantity":545, "Price per quantity(N)":50},
           "Three crown(tin)":{"Available Quantity":201, "Price per quantity(N)":150},
           "Peak milk(tin)":{"Available Quantity":230, "Price per quantity(N)":120},
           "Peak milk(satchet)":{"Available Quantity":791, "Price per quantity(N)":50},
           "Bournvita(satchet)":{"Available Quantity":611, "Price per quantity(N)":50},
           "Milo(tin)":{"Available Quantity":367, "Price per quantity(N)":500},
           "Peak milk(Large Satchet)":{"Available Quantity":889, "Price per quantity(N)":700},
           "Milo(Large Satchet)":{"Available Quantity":934, "Price per quantity(N)":700},
           "Bournvita(Large Satchet)":{"Available Quantity":758, "Price per quantity(N)":100},
           "Custard(Small satchet)":{"Available Quantity":383, "Price per quantity(N)":200},
           "Corn flakes(small satchet)":{"Available Quantity":647, "Price per quantity(N)":150},
           "Golden morn(small satchet)":{"Available Quantity":121, "Price per quantity(N)":100},
           "Detergent(small Wawu)":{"Available Quantity":198, "Price per quantity(N)":120},
           "Detergent(small Aerial)":{"Available Quantity":354, "Price per quantity(N)":115},
           "Detergent(big Wawu)":{"Available Quantity":323, "Price per quantity(N)":200},
           "Detergent(Big Aerial)":{"Available Quantity":222, "Price per quantity(N)":250},
           "Corn flakes(big satchet":{"Available Quantity":341, "Price per quantity(N)":750},
           "Golden Morn(Large satchet)":{"Available Quantity":458, "Price per quantity(N)":650},
           "Sprite(small)":{"Available Quantity":134, "Price per quantity(N)":80},
           "Pepsi(small)":{"Available Quantity":674, "Price per quantity(N)":80},
           "Fanta(small)":{"Available Quantity":757, "Price per quantity(N)":80},
           "Lacasera(small)":{"Available Quantity":127, "Price per quantity(N)":80},
           "Sprite(big)":{"Available Quantity":956, "Price per quantity(N)":150},
           "Pepsi(big)":{"Available Quantity":374, "Price per quantity(N)":150},
           "Fanta(big)":{"Available Quantity":374, "Price per quantity(N)":150},
           "Lacasera(big)":{"Available Quantity":374, "Price per quantity(N)":150},
           "Coke(big)":{"Available Quantity":374, "Price per quantity(N)":150}
        }

    def change_price_of_items(self, name, new_price):
        self.stock[name]["Price per quantity(N)"] = new_price
        

    def add_more_items(self, name, available_Quantity, price_per_quantity):
        self.stock.update({name:{"Available Quantity": available_Quantity, "Price per quantity(N)": price_per_quantity}})

    
    def total_gain_per_day(self):
        return
    
my_stock = Retail_market()

my_stock.change_price_of_items("Sugar",60)
my_stock.add_more_items("Spaghetti(Dangote)",70,90)

def communicate_with_users():
        print("These are the available items in our store\n")
        for keys, values in my_stock.stock.items():
            print(keys)
        time.sleep(2)

        print("\nThe price for the available goods in our store in (N) are stated below:\n")
        for keys, values in my_stock.stock.items():
            print(keys + ':' + str(values["Price per quantity(N)"]))
        time.sleep(2)

        def buy_goods():
            print("\nFill the form below to take in your order\n")
            global items_needed
            items_needed = {}
            global number_of_items
            number_of_items = int(input("How many items do you want to purchase from our shop: "))
            for i in range(number_of_items):
                data = input ('Enter the name & quantity of goods separated by ":" : ')
                temp = data.split(':')
                items_needed[temp[0]] = int(temp[1])
            global total_payment
            total_payment = 0
            global price_list
            price_list = []
            global valList
            valList = []
            for key,value in items_needed.items():
                total_payment += my_stock.stock[key]['Price per quantity(N)'] * value
                time.sleep(2)
                if value > 10:
                    price_list.append(my_stock.stock[key]["Price per quantity(N)"])
                valList.append(value)
                

                def update_stock():
                    quantity_left = my_stock.stock[key]["Available Quantity"] - value
                    my_stock.stock[key]["Available Quantity"] = quantity_left
                update_stock()
        buy_goods()
        def receipt():
            print("\n==============================================")
            print("\t MAL ADAMU IFE RETAIL MARKET", "\n\t\tCash Receipt")
            global total_payment
            global number_of_items
            quantity = 0
            for quantity in valList:
                if quantity < 5:
                    VAT = total_payment * 0.2
                    total_payment += VAT

                elif quantity > 10:
                    VAT = total_payment * 0.3
                    total_payment += VAT
                    if min(price_list) >= 100:
                        global Discount
                        Discount = 800
                        total_payment = total_payment - Discount
            for key, value in items_needed.items():
                
                cost_per_items = my_stock.stock[key]["Price per quantity(N)"]
                total_cost_for_these_items = my_stock.stock[key]['Price per quantity(N)'] * value
                print(f'Name of goods:{key}')
                print(f"Quantity purchased:{value}")
                print(f"Cost per quantity:N{cost_per_items}")
                print(f'Total price for this quantity:N{total_cost_for_these_items}\n')
            print(f"VAT:N{VAT}")
            print("Total cost of the goods purchased : N{}".format(total_payment))
            print("===============================================")
        receipt()
communicate_with_users()
