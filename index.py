from methods.incremental import incremental_rename, incremental_with_extra
from methods.get_path import get_path
from methods.get_prefix_suffix import get_text

print(":: Welcome ::")
print(":: Author: Anubixo ::")
print(":: Bulk Renamer Script ::")

src = get_path("Source Directory")
# print(src)
des = get_path("Destination Directory")
# print(des)

while True:
    print(":: Please select your operation or type exit to quit ::")
    print("==================================")
    print("1: Incremental Rename")
    print("2: Incremental With Prefix")
    print("3: Incremental With Suffix")
    print("4: Timestamp With Prefix")
    print("5: Timestamp With Suffix")
    print("6: Select New Source And Destination")
    print("==================================")
    operation = input("Type Operation Number: ")
    if operation.lower() == "exit":
        print(":: Thank you for using my script ::")
        print(":: Exiting ::")
        quit()
    elif operation == "1":
        res = incremental_rename(src, des)
        print(res)
    elif operation == "2":
        word = get_text("prefix")
        res = incremental_with_extra(src, des, word, 1)
        print(res)
    elif operation == "3":
        word = get_text("suffix")
        res = incremental_with_extra(src, des, word, 0)
        print(res)
    # elif operation == "4":
    #     word = get_text("prefix")
    #     print(operation)
    # elif operation == "5":
    #     word = get_text("suffix")
    #     print(operation)
    elif operation == "6":
        src = get_path("Source Directory")
        des = get_path("Destination Directory")

