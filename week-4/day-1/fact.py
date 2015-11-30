def fact(n):
    if n ==2:
        fact_sum = n * (n-1)
        return fact_sum
    else:
        return fact(n-1) * n

print(fact(6))

# fact(6)
#     fac(5) * 6  =
#         fact(4) *5
#             fact(3) *4
#                  fact(2) = 2
                    
