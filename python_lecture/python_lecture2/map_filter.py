int_numbers = range(-5, 6)
f = filter(lambda x: x<0, int_numbers)
m = map(lambda x: x<0, int_numbers)

print("f= ", list(f)) # logic이 True인 것의 결과를 반환
print("m= ", list(m)) # logic이 True인지 아닌지 반환

f = filter(lambda x: x * 2, int_numbers)
m = map(lambda x: x * 2, int_numbers)

print("f= ", list(f)) # logic이 True인 것을 반환 
print("m= ", list(m)) # logic을 적용해서 반환

## filter -> 걸러내서 보여줘
## map -> 적용해서 보여줘

