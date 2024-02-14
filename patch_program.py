class monkey:
    def patch(self):
          print ("patch() is being called")

def monk_p(self):
    print ("monk_p() is being called")

# replacing address of "patch" with "monk_p"
monkey.patch = monk_p

obj = monkey()

obj.patch()
# monk_p() is being called

class patch:
     def patch_fun(self):
          print("patch_function is called")

def call_fun(self):
     print("call function is called")

patch.patch_fun = call_fun

obj1 = patch()
obj1.patch_fun()