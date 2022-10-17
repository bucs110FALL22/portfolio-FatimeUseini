def percentage_to_letter(score):
  if score >="90":
    lscore= "A"
    return lscore
  if score >"80":
    lscore= "B"
    return lscore
  if score >"70":
    lscore= "C"
    return lscore
  if score >"60":
    lscore= "D"
    return lscore
  if score <"60":
    lscore= "F"
    return lscore
score= input("Input your score.:")
score= percentage_to_letter(score)
print(score)
#def is_passing(letter=none):
