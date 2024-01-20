# importing the modules created
import districtmodule
import periodmodule

# Creating register function
# The function register a students for Learning Python benninger program
def register(name, address, dis, day):
    day = periodmodule.days(day)
    dis = districtmodule.districts_lima(dis)
    shc = periodmodule.schedules["20"]
    ins = periodmodule.program["instructor"]
    pro = periodmodule.program["program"]

    return "The student " + name + " with address " + address + " - " + dis + " registre the program " + pro + " - Instructor: " + ins + " the days " + day + " in the schedule "+shc

# Calling the register function
student = register("Cesar Paredes", "Street detroit", 10, 2)
print(student)