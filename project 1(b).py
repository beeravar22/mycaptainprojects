a=input("enter the filename::")
extension=a.split('.')
if extension[-1]=='py':
    print("python")
else:
    print("not defined")