days=int(input("number of days"))
wpd=int(input("enter wage per day"))
basic= days * wpd
HRA= basic *0.1
DA = basic * 0.05
PF = basic * 0.12
print(f"netsalary is {basic + HRA + DA -PF}")
print(f"HRA is {HRA}")
print(f"DA is {DA}")
print(f"PF is {PF}")