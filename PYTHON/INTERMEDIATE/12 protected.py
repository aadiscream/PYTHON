class papa:
    def __init__(self):
        self._name="anuj"
        print(f"papa is {self._name}")
class beta(papa):
    def show(self):
        self._sname="adi"
        print(f"father is {self._name}\nand son is {self._sname}")

a=beta()
a.show()
