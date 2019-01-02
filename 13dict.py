BloodGroup ={"Vidit":"O+","Neha":"B+","Niraj":"B+"}
print(BloodGroup.keys())
print(BloodGroup.values())
BloodGroup["Tiwari"]="B+"
print(BloodGroup)
print(BloodGroup.keys())
del BloodGroup['Neha']
print(BloodGroup)
BloodGroup["Vidit"] = "O-"
print(BloodGroup)