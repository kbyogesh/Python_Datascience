#multiple inheritance :
class A:
  def methode_a(self):
    print("methode1")
class B:  
  def methode_b(self):
     print("methode2")
class C(A,B):
  def methode_c(self):
    print("methode3")
obj_c=C()
obj_c.methode_a()
obj_c.methode_b()
obj_c.methode_c()