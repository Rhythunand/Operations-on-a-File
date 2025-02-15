fn = open('Codingal1.txt', 'r')
fn1 = open("'Codingal.txt", 'w')

count = fn.readlines()
type(count)

for i in range(1, len(count)+1) :
  if(i % 2 != 0) :
    fn1.write(count[i-1])

  else :
    pass

fn1.close()

fn1 = open('Codingal.txt', 'r')

count1 = fn1.read()

print(count1)

fn.close()
fn1.close()