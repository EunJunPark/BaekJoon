def hab(sorted_list):
    total_sum = sum(sorted_list)
    for i in range(9):
        for j in range(i+1, 9):
            if total_sum - sorted_list[i] - sorted_list[j] == 100:
                ans = [sorted_list[k] for k in range(9) if k != i and k != j]
                ans.sort()
                return ans

list = []

for i in range(9):
    num = int(input())  
    list.append(num)

sorted_list = sorted(list)
result = hab(sorted_list)

for r in result:
    print(r)
