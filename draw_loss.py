#test loss
def draw_loss(dir):
    k=[]
    regex = "(loss = )[-+]?([0-9]*\.[0-9]+|[0-9]+)"
    regexobject = re.compile(regex)
    with open(dir) as file:
        line=file.readline()
        while line:
            #here add
            try:
                k.append(float(regexobject.search(line).group(2)))
            except:
                1
            line=file.readline()
    return k
