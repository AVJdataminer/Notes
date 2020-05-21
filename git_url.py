# create raw github url for direct link to users
import sys
#name = sys.argv[1]
input_url = input("Enter the github url: ")
y = input_url.replace('/blob','')
x = y.replace('github.com','raw.githubusercontent.com')
print("raw url: ", x )