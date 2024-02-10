#multilevel
class A:
  def methode_a(self):
    print("methode")
class B(A):
  def methode_b(self):
    print("methode2")
class C(B):
  def methode_c(self):
    print("ajsdhasjdas")
obj_c=C()
obj_c.methode_a()
obj_c.methode_b()
obj_c.methode_c()
