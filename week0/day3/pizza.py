from time import time
from datetime import datetime
import os


def main():
    command = ""
    orders = {}
    order_files = {}
    list_called = False
    orders_saved = True
    discard_command = ""
    while(command != "finish" or discard_command != "finish"):
        command = input("Enter command>")
        if(command.startswith("take")):
            order_info = command.split(" ")
            if(order_info[1] in orders):
                orders[order_info[1]] += float(order_info[2])
            else:
                orders[order_info[1]] = float(order_info[2])
            print("Taking order from %s for %0.2f" %
            (order_info[1], float(order_info[2])))
            orders_saved = False
        elif(command == "status"):
            for client in orders:
                print("%s - %0.2f" % (client, orders[client]))
        elif(command == "save"):
            ts = time()
            stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
            file = open("orders_%s" % stamp, "w")
            for client in orders:
                file.write("%s - %0.2f" % (client, orders[client]) + "\n")
            file.close()
            print("Saved the current order to orders_%s" % stamp)
            orders_saved = True
        elif(command == "list"):
            counter = 0
            for filename in os.listdir('.'):
                if(filename.startswith("orders_")):
                    counter += 1
                    order_files[counter] = filename
            for file in order_files:
                print("[%d] - %s" % (file, order_files[file]))
            list_called = True
        elif(command.startswith("load")):
            if(list_called is False):
                print("Use list command before loading")
            elif(orders_saved is False and discard_command != command):
                print("You have not saved the current order." + "\n"
                "If you wish to discard it, type load <number> again.")
                discard_command = command
            else:
                file = open(order_files[int(command.split(" ")[1])], "r")
                orders = {}
                for line in file:
                    order_entry = line.strip("\n").split(" - ")
                    orders[order_entry[0]] = float(order_entry[1])
                orders_saved = True
                file.close()
        elif (command == "finish"):
            if(discard_command == command):
                print("Finishing order. Goodbye!")
                return
            if(orders_saved is False):
                print("You have not saved your order.\nIf you wish to continue, "
                "type finish again.\nIf you want to save your order, type save")
                command = ""
                discard_command = "finish"
            else:
                print("Finishing order. Goodbye!")
        else:
            print("Unknown command!\nTry one of the following:\n"
            "take <name> <price>\nstatus\nsave\nlist\nload <number>\nfinish")

if __name__ == '__main__':
    main()