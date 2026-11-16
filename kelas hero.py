class Hero:
    def __init__(self, nama, atribut, skil, demage):
        self.nama = nama
        self.atribut = atribut
        self.skil = skil
        self.demage = demage
        print()
        
class assasin(Hero):
    def kelas_hero(self):
        print("    KELAS ASSASIN             ")
        print(f"Nama     <•>  {self.nama}    ")
        print(f"Atribut  <•>  {self.atribut} ")
        print(f"Skil     <•>  {self.skil}    ")
        print(f"DEMAGE   <•>  {self.demage}  ")
   
class mage(Hero):
    def kelas_hero(self):
        print("     KELAS MAGE               ")
        print(f"Nama     <•>  {self.nama}    ")
        print(f"Atribut  <•>  {self.atribut} ")
        print(f"Skil     <•>  {self.skil}    ")
        print(f"DEMAGE   <•>  {self.demage}  ")
        
class tenk(Hero):
    def kelas_hero(self):
        print("    KELAS TENGKER             ")
        print(f"Nama     <•>  {self.nama}    ")
        print(f"Atribut  <•>  {self.atribut} ")
        print(f"Skil     <•>  {self.skil}    ")
        print(f"DEMAGE   <•>  {self.demage}  ")
        
class marksman(Hero):
    def kelas_hero(self):
        print("    KELAS MARKSMAN            ")
        print(f"Nama     <•>  {self.nama}    ")
        print(f"Atribut  <•>  {self.atribut} ")
        print(f"Skil     <•>  {self.skil}    ")
        print(f"DEMAGE   <•>  {self.demage}  ")
        
class figter(Hero):
    def kelas_hero(self):
        print("    KELAS FIGTER              ")
        print(f"Nama     <•>  {self.nama}    ")
        print(f"Atribut  <•>  {self.atribut} ")
        print(f"Skil     <•>  {self.skil}    ")
        print(f"DEMAGE   <•>  {self.demage}  ")
        
class support(Hero):
    def kelas_hero(self):
        print("    KELAS SUPPORT             ")
        print(f"Nama     <•>  {self.nama}    ")
        print(f"Atribut  <•>  {self.atribut} ")
        print(f"Skil     <•>  {self.skil}    ")
        print(f"DEMAGE   <•>  {self.demage}  ")

hero1 = assasin(
    "mucen", "sword", "lightning speed",
    "physical demage"
);hero1.kelas_hero()

hero2 = mage(
    "coli", "magic wand", "thunder fire",
    "magic damage"
);hero2.kelas_hero()

hero3 = tenk(
    "garoga", "flavor and mace", "split the ground",
    "physical demage"
);hero3.kelas_hero()

hero4 = marksman(
    "stely", "arrow", "rain of explosive arrows",
    "physical demage"
);hero4.kelas_hero()

hero5 = figter(
    "simon", "sword", "thunder sword",
    "magic damage"
);hero5.kelas_hero()

hero6 = support(
    "cilin", "healing wand", "continuous healing",
    "magic demage"
);hero6.kelas_hero()


    
    
