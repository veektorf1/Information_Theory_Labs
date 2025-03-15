def read_pdf(filename):
    with open(filename,"rb") as file:
        for line in file:
            print(line)

        
read_pdf("wiki.pdf")