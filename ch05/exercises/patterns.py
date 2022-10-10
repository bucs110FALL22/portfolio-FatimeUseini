star="*"
star1="*"
star_pyramid=int(input("how many rows?:"))
  
for i in range(star_pyramid):
  i= (star_pyramid-4)+i
  print(star*i)
  

r_star_pyramid=int(input("how many rows?:"))
for i in range(r_star_pyramid):
  i= star_pyramid-i
  print(star1*i)
  