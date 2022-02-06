class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
def createnewlist():
    oldlist = SLinkedList()
    oldlist.headval = Node("1")
    e2 = Node("2")
    e3 = Node("3")
    e4 = Node("4")
    e5 = Node("5")

    # Link first Node to second node
    oldlist.headval.nextval = e2

    # Link second Node to third node
    e2.nextval = e3
    e3.nextval = e4
    e4.nextval = e5

    oldlist.listprint()
    newlist = SLinkedList()

    newlist.headval = oldlist.headval.nextval
    newlist.headval.nextval= oldlist.headval.

    newlist.listprint()

createnewlist()


