import os

class Application():

    def __init__(self, file_path, file_encoding, line_length):
        self.file_path = file_path
        self.file_encoding = file_encoding
        self.line_length = line_length
        self._is_running = False

    def run(self):
        print("Vítejte v programu na evidenci úkolů!")

        commands = [
            ("Vypsat seznam", 1),
            ("Zobrazit první úkol", 2),
            ("Přidat na seznam", 3),
            ("Smazat celý seznam", 4),
            ("Smazat první úkol", 5),
            ("Ukončit program", 6),
        ]

        self._is_running = True
        while (self._is_running):
            print("=" * self.line_length)
            print("Vyberte příkaz:")
            for label, command_num in commands:
                print("\t" + str(command_num) + ". " + label)

            command_num = None
            while (command_num == None):
                command_num = input("Zadejte číslo příkazu (1-"+ str(len(commands)) +"): ").strip()
                try:
                    command_num = int(command_num)
                    if (not 0 < command_num <= len(commands)):
                        raise Exception()
                except:
                    print("Neplatné zadání musíte zadat číslo mezi 1 až "+ str(len(commands)))
                    command_num = None

            if (command_num == 1):
                print("=" * self.line_length)
                print("Seznam úkolů:")
                i = 0;
                if os.path.exists(self.file_path):
                    with open(self.file_path, "r", encoding=self.file_encoding) as f:
                        for task in f.readlines():
                            i += 1;
                            print("\t" + str(i) + ". " + task.strip())
                if (i == 0):
                    print("\t(žádné úkoly)")

            if(command_num == 2):
                print("=" * self.line_length)
                print("První úkol:")
                i = 0
                if os.path.exists(self.file_path):
                    with open(self.file_path, "r", encoding=self.file_encoding) as f:
                        print("\t" + ". " + f.readline().strip())
                else:
                    print("\t(žádné úkoly)")

            if (command_num == 3):
                print("=" * self.line_length)
                new_task = None
                while (new_task == None):
                    new_task = input("Zadejte nový úkol: ").strip()
                    if (len(new_task) < 1):
                        print("Neplatné zadání musíte zadat nějaký text")
                        new_task = None
                if os.path.exists(self.file_path):
                    mode = "a"
                else:
                    mode = "w"
                with open(self.file_path, mode, encoding=self.file_encoding) as f:
                    f.write(new_task + "\n")
                    f.flush()

            if (command_num == 4):
                check = input("Opravdu checete smazat všechny úkoly [ano/ne]?:")
                if check.casefold().strip() == "ano":
                    if os.path.exists(self.file_path):
                        os.remove(self.file_path)
                    print("=" * self.line_length)
                    print("Seznam ukolů byl smazán.")

            if (command_num == 5):
                check = input("Opravdu checete smazat první úkol [ano/ne]?:")
                if check.casefold().strip() == "ano":
                    if os.path.exists(self.file_path):
                        lines = []
                        with open(self.file_path, "r") as f:
                            lines = f.readlines()
                        
                        with open(self.file_path, "w") as f:
                            f.writelines(lines[1:])
                    print("=" * self.line_length)
                    print("První úkol byl smazán.")

            if (command_num == 6):
                self._is_running = False;
                print("=" * self.line_length)
                print("Program ukončen, nashledanou příště.")