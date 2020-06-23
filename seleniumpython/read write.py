class readFile:

    def reading(self):
        file = open('file.txt')
        # print(file.read())
        # print(file.readline())
        line = file.readline()
        while line != "":
            print(line)
            line = file.readline()
        file.close()

    def reading2(self):
        file = open('file.txt')
        for line in file.readlines():
            print(line)

        file.close()

    def write1(self):
        with open('file.txt', 'r') as reader:
            content = reader.readlines()
            reversed(content)
            with open('file.txt', 'w') as writer:
                for line in reversed(content):
                    writer.write(line)




obj = readFile()
#obj.reading()
#obj.reading2()
obj.write1()
