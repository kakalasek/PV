class GeneratorKrasovychJezer():
   
    jezera = [
        ["Dyje", ["Křivé jezero","Květné jezero","Kutnar","Mahenovo jezero"]],
        ["Labe", ["Babinecká tůň","Hrbáčkovy tůně"]],
        ["Bílina", ["Komořanské jezero"]],
        ["(bez řeky)", ["Antošovické jezero", "Holásecká jezera","Krňák","Kurfürstovo rameno","Malá říčka","Podhradská tůň"]]
    ]
 
    def __iter__(self):
        self.i = 0
        self.j = 0
        return self
    
    def __next__(self):
        if self.j > (len(GeneratorKrasovychJezer.jezera[self.i][1])-1):
            self.i = self.i + 1
            self.j = 0

        if self.i > (len(GeneratorKrasovychJezer.jezera)-1):
            raise StopIteration
        
        append = GeneratorKrasovychJezer.jezera[self.i][0]
        pomocna = GeneratorKrasovychJezer.jezera[self.i][1][self.j]
        self.j = self.j + 1
        return pomocna + "(" + append + ")"
        


for jezero in GeneratorKrasovychJezer():
    print(jezero)

