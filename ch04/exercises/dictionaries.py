article= "A new purple M&M has joined the bag!'Purple' is the chocolate candy's first-ever female peanut M&M and its newest character for the first time in a decade, the brand announced Wednesday, Sept. 28. With the new spokescandy working to 'help more people feel they belong,' Purple made her debut with a new song called 'I'm Just Gonna Be Me,' featuring an accompanying music video. Purple’s musical entrance into the candy world 'celebrates all voices, encouraging people around the world to embrace their authentic selves,' M&M's shared."      
substitutions = {
                  "purple": "gray",
                  "Purple": "Gray",
                  "newest": "oldest",
                  "belong":"don't belong",
                  "called": "named",
                  "all":"your moms",
                  "voices":"voice",
                  "authentic": "fake",
                  "decade":"minute",
                  "female":"woman"
}


for key,value in substitutions.items():
    article = article.replace(key,value)

print(article)



  
