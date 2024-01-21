#hcf finder

def compute_hcf(a,b):
    if a > b:
        small = b
    else:
        small = a
    
    for i in range(1,small+1):
        if (a % i == 0) and (b % i == 0):
            hcf = i
            print(hcf)
    return hcf

print("The hcf is",compute_hcf(54,24))