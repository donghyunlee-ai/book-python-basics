from mathtools.gcdlcm import gcd
from mathtools.prime import PrimeFinder

print(f"12와 18의 최대공약수: {gcd(12, 18)}")

finder = PrimeFinder()
finder.find_up_to(100)
print(f"100 이하 소수의 개수: {finder.count()}개")

finder.find_up_to(200)
print(f"200 이하 소수의 개수: {finder.count()}개")
