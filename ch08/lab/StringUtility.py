class StringUtility:
  def __init__(self,string):
    self.string= string
    
  def __str__(self):
    """
    returns the internal string unchanged
    args= string
    return= returns string 
    """
    return self.string
    
  def vowels(self):
    """
    returns the number of vowels in a string
    args= string
    return = returns string 
    """
    count=0
    for i in self.string:
      if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count= count+1
    if count<5:
      return str(count)
    else:
      return "many"
      
  def bothEnds(self):
    """
    returns the first two and last two letters of a string
    args= string
    return = returns string 
    """
    if len(self.string) >= 2: 
       mystring= self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
       return mystring
    else:
      return('')
      
  def fixStart(self):
    """
    returns an asterisk in place for each repeat of the first letter in each string while leaving the first letter unchanged 
    args= string
    return = returns string 
    """
    if len(self.string)>=1:
      first_ch= self.string[0]
      for i in self.string:
        mystring= self.string[1: ].replace(first_ch,"*")    
      return self.string[0]+ mystring
    else: 
      return ('')

  def asciiSum(self):
    """
    gets the ascii code of each character in a string and then returns the sum of each of these values
    args= string
    return = returns string 
    """
    ascii_codes=[]
    for ch in range(len(self.string)):
      ascii_codes.append(ord(self.string[ch]))
    return sum(ascii_codes)

  def cipher(self):
    """
    increments each character in a string by the length of the string 
    args= string
    return = returns string
    """
    for ch in self.string: 
      mystring= "".join(chr(ord(ch)+len(self.string)) for ch in self.string)
    return mystring 
    
    

                


  
 
        
    
  
    
    
    
  
  