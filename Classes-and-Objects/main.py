class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score ):
        self.name=str(name)
        self.age=int(age)
        self.tracks=list(tracks)
        self.score=float(score)

Head_boy = Student("Emmanuel", 26, ["FE","BE"], 90.90)
Head_girl = Student ("Emmanuella", 22, ["UI", "UX"], 89.6)
print ("HEAD BOY INFORMATION")
print ("Name:  ", Head_boy.name)
print ("Age: ", Head_boy.age)
print ("tracks: ", Head_boy.tracks)
print ("Score :", Head_boy.score)

print ('''________________________________
''')
print ("HEAD GIRL INFORMATION")
print ("Name:  ", Head_girl.name)
print ("Age: ", Head_girl.age)
print ("tracks: ", Head_girl.tracks)
print ("Score :", Head_girl.score)
