import random
import time
card = ('阿卡丽','德莱文','阿木木','牛头','德玛西亚')
package = {}
weight_list = [5,10,20,50,100]
weight_compare = [5,15,35,85,185]
while 1:
    
    print('请输入指令:\n1.抽卡\n2.查看背包\n3.离开')
    a = int(input())
    if a == 1:
        print('请输入抽卡次数:')
        b = int(input())
        for i in range(0,b):
            n = random.randint(1,weight_compare[-1])
            i = 0
            while n > weight_compare[i]:
                i += 1
            c = card[i]
            if package.__contains__(c):
                package[c] += 1
            else:
                package[c] = 1
            time.sleep(0.3)
            print('你抽到了:'+ c)
    if a == 2:
        print(package)
    if a == 3:
        break
