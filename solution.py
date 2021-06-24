ch = '.|.'
ca = 'welcome'
row, col = input().split()

sum = int(int(row) / 2) + 1
i = 0
while i < int(row):
    if i + 1 != int(sum):
        print(((ch * i) + ch + (ch * i)).center(int(col), '-'))
    else:
        print(ca.center(int(col), '-'))
        for j in range(i + 1, int(row)):
            k = i - 1
            while k >= 0:
                print(((ch * k) + ch + (ch * k)).center(int(col), '-'))
                k -= 1
            break
        break

    i += 1


