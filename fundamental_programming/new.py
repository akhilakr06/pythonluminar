employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id":1001,"e_name":"ravi","salary":22000,"department":"ba","exp":1},
    {"e_id":1002,"e_name":"raj","salary":20000,"department":"mrkt","exp":1},
    {"e_id":1003,"e_name":"nikil","salary":26000,"department":"developer","exp":1},
    {"e_id":1004,"e_name":"nivi","salary":28000,"department":"developer","exp":2},

]
# for employee in employees:
#     print(employee["e_name"])
# #uppercase
# for employee in employees:
#     print(employee["e_name"].upper())
#print employee as developer
# for employee in employees:
#     if (employee["department"]=="developer"):
#         print("developer",employee["e_name"])

# total sal
total=0
for employee in employees:
    total+=employee["salary"]
print(total)
# 1 case map
# 2 filter
# 3 reduce
# print employee start with 'a'

# print highest salary reduce
# print lowest salary reduce
# add bonus for all employee map




