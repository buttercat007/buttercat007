christmastree = open('christmastree.txt', 'w')
treesize = 10

for i in range(1,treesize+1, 1):
  num = treesize
  text = ""
  #สร้าง ข้างแรกของต้น
  for i in range(treesize, 1, -1):
    christmastree.write(f'{int(num)}')
    num = num - 1
  for i in range(1, treesize+1):
    christmastree.write(f'{int(num)}')
    num = num + 1
  # print("")
  christmastree.write("\n")
  treesize = treesize - 1

christmastree.close()

christmastree = open('christmastree.txt', 'r')
tree = []
treelength = 0
for line in christmastree:
  if len(line.strip("\n")) > treelength:
    treelength = len(line.strip("\n"))
  tree.append(line.strip("\n"))

newtree = sorted(tree, key=len)

for i in newtree:
  print(f'{i:^{treelength}}')

for m in range(1,9,3):
    for i in range(m,m+1):
        print(f"{str(str(i)+str(i+1)+str(i+2)):^{treelength}}", end="")
    print()

christmastree.close()
