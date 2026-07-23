try:
    num = int(input("Enter a number : "))
    print(10/num)

except ZeroDivisionError:
    print("0 se divide nhi kar sakate")

except ValueError:
    print("shirf number hi ENter kar sakate hai")

# except:
#    print("Error")

finally:
    print("Program Finished")