# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


func = True

dici = {}

current = 0

while func:

    name = input("Type your name: \n")
    bid = int(input("Type your bid: \n"))
    if bid > current:
        current = bid

    question = input("Here are others who need to bid? 'yes' or 'no'?")

    dici[name] = bid

    print("\n" * 20)

    if question == 'no':
        func = False
        print("bye")


for key, value in dici.items():
    if value == current:
        print(f"The highest bid is: \nname: {key}\nbid: {value}")


