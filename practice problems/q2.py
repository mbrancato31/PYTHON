num = int(input())
ans = 1
for i in range(1, num + 1):
    ans *= i

print(ans)

# def fact(x):
# #     if x == 0:
# #         return 1
# #     return x * fact(x - 1)
# #
# # x=int(raw_input())
# # print fact(x)