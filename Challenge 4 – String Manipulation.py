a=input("Enter a Sentence:")

b=a.split()

c=len(b)

print(f"Number of Words:{c}")

d=b[::-1]
e=" ".join(d)
print(f"Reversed sentence:{e}")

f="-".join(b)
print(f"Modified sentence:{f}")
