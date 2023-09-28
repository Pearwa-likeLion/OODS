#Premier League Score by Pearwa Tuss

# เช็คค่า value ของ key => win if win[i] == win[i+1] เช็ค ความต่างของ scroed and conceded
# หลังจากนั้น append key to list แล้วค่อยจัดเข้า dict 

# version 2 
# สร้าง dict เก็บทุกอย่างก่อน แล้วเอา dict ใส่เข้าไปใน list 
# ทำการ sort แล้วค่อย print ออกมาด้วยการ วนลูปใน list
# ______________________________________________________________________________________________

#version 3
# ทำ ทุกอย่างเป็น object แล้วเอาไปใส่ใน list แล้ว sort

class footballTeam:
    def __init__(self, name, wins : int, loss : int, draws : int, scored : int, conceded : int):
        self.name = name
        self.wins = wins
        self.loss = loss
        self.draws = draws
        self.scored = scored
        self.conceded = conceded
        self.points = 3 * int(self.wins) + 0 * int(self.loss) + 1 * int(self.draws)
        self.gd = int(self.scored) - int(self.conceded)
    
    def __str__(self):
        return str(self.name)

def sorted(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if l[j].points < l[j+1].points:
                l[j] , l[j+1] = l[j+1] , l[j]
            elif l[j].points == l[j+1].points:
                if l[j].gd < l[j+1].gd: l[j] , l[j+1] = l[j+1] , l[j]
    return l

def printSortedTeam(l):
    print("== results ==")
    for team in l:
        print(f"['{team.name}'",end=", ")
        print('{' + f"'points': {team.points}" +'}, ' + '{' + f"'gd': {team.gd}" + '}]')
        

inp = input("Enter Input : ").split("/")
l = []
for data in inp:
    d = data.split(",")
    l.append(footballTeam(d[0], d[1], d[2], d[3], d[4], d[5]))

printSortedTeam((sorted(l)))
