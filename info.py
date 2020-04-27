file = open('C:\\LibrusBot\\Info.txt', 'r')

#[0] librus login
#[1] librus password
#[2] bot token
settings = file.readlines()

app = [s.replace('\n', '') for s in settings]

print(app)