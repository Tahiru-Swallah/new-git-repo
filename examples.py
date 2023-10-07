 #WORKING WITH FILES AND DIRECTORIES

""" import os
import datetime
def filter_files():
    dir_ = "html files"
    store_files = []
    for files in os.listdir(dir_):
        full_name = os.path.join(dir_, files)
        if os.path.isfile(full_name):
            store_files.append(files)
    return store_files

def getSize():
    new = filter_files()
    store_info = []
    os.chdir("html files")
    for index, name in enumerate(new):
        store_info.append(name + " " + str(os.path.getsize(name)) + "MB")
        result = os.getcwd()
    return store_info, result
print(getSize())



import os 
import datetime

def new_file(filename):
    with open(filename, "w") as file:
        pass
    timestamp = os.path.getmtime(filename)
    print(timestamp)
    now = datetime.datetime.fromtimestamp(timestamp)
    return ("{:%y-%m-%d}".format(now))
print(new_file("newfile.txt"))

def parent_directory():
    relative_parent = os.path.join(os.getcwd(), "new_dir")
    return os.path.abspath("../new_dir")
print(parent_directory()) """


#CSV FILE MODULE EXAMPLES

""" import csv

f = open("newfile.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name,phone,role))
f.close() """

import csv
""" hosts = [["workstation.local","192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts) """

""" with open("hosts.csv") as hosts:
    reader = csv.DictReader(hosts)
    for row in reader:
        print("{} has {} users".format(row["name"], row["user"])) """

""" users = [{"name":"Sol Mansi", "username":"solm", "department":"IT Infrastructure"},
{"name":"Charlie Grey", "username":"greyc", "department":"User Experience Research"},
{"name":"Lio Nelson", "username":"lion", "department":"Development"}]

keys = ["name","username","department"]
with open("by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users) """

""" with open("by_department.csv") as by_department:
    reader = csv.DictReader(by_department)
    for row in reader:
        print(row)
        print("name: {}, username: {}, department: {}".format(row["name"], row["username"], row["department"])) """

""" import os

def create_file(filename):
    with open(filename, "a") as file:
        file.write("name, color, type\n")
        file.write("carnation, pink, annual\n")
        file.write("daffodil, blue, perennial\n")
def contents_of_file(filename):
    return_string = ""

    create_file(filename)

    with open(filename) as file:
        rows = csv.reader(file)
        for row in rows:
            name, color, type = row
            return_string += "a {} {} is {}\n".format(name, color, type)
    return return_string
print(contents_of_file("flowers.csv")) """


""" import os

def get_image():
    store_dir = []
    for folder in os.listdir("html files"):
        full_path = os.path.join("html files", folder)
        if os.path.isdir(full_path):
            store_dir.append(folder)
    return store_dir

def access_image():
    images = get_image()
    store_images = []
    os.chdir("html files")
    for img in os.listdir(images[images.index("img")]):
        store_images.append(img)
    return store_images

def create_folder():
    pics = access_image()
    os.chdir("D:")
    os.chdir("images")
    print(os.getcwd())
    for pic in pics:
        with open(pic, "w") as pictures:
            pictures.write(pic)
create_folder() """


import csv
import os
import logging
""" users = [{"Full Name":"Audrey Miller", "Username":"audreym", "Department":"Development"},
         {"Full Name":"Arden Garcia", "Username":"ardeng", "Department":"Sales"},
         {"Full Name":"Bailey Sousa", "Username":"sousa", "Department":"Human Resources"},
         {"Full Name":"Blake Thomas", "Username":"blake", "Department": "IT infrastructure"}]
keys = ["Full Name", "Username", "Department"]

with open("report.csv", "w+") as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users) """

def get_files():
    store_file = []
    
    with open("report.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            store_file.append(row)
    return store_file

def process_data():
    department_list = []
    for employee_list in get_files():
        department_list.append(employee_list["Department"])

    department_data = {}
    for department_name in department_list:
        department_data[department_name] = department_list.count(department_name)
        
    return department_data
    
def write_report():
    with open("report.txt", "w") as file:
        for name, value in process_data().items():
            file.write(name + ":" + str(value)+"\n")
""" write_report()  """

""" import os
import csv
def get_dict():

    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    dict_ = {}

    for q,a in zip(questions,answers):
        dict_[q] = a
    return dict_

def create_csv():
    with open("quest.csv") as f:
        writer = csv.DictReader(f)
        for row in writer:
            print(row["name"])
create_csv() """



""" import os

def get_folder():
    new = "..\Desktop"
    store = []
    for folder in os.listdir(new):
        folders = os.path.join(new, folder)
        if os.path.isdir(folders):
            store.append(folder)
    return store
print(get_folder()) """

""" def say_love():
    count = 5
    guessed = False
    print("==== Welcome to lovers joint game ===== \n")
    while not guessed and count > 0:
        name = input("Guess Tahiru's girlfriend name to win a prize, You have only five chances: ").capitalize()
        if name == "Rafia" or name == "Rafiya":
            print(f"You guessed right {name} is Tahiru's lover ❤💕")
            guessed = True
        else:
            print(f"oops {name} is not the girl")
            count -= 1
    if count <= 0:
        print("You have lost the game!!!")

def main():
    say_love()
    while input("Play Again (Y/N): ").upper() == "Y":
        say_love()
if __name__ == "__main__":
    main()  """




""" import csv

def get_file():
    with open("newfile.txt") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row["Tahiru"])
get_file() """

import os

def see_files():
    name = os.listdir("E:")
    store_folder = []
    os.chdir("E:")
    for i in name:
        file_name = os.path.join(os.getcwd(), i)
        if os.path.isdir(file_name):
            store_folder.append(i)
    return store_folder

def get_files():
    list_folder = see_files()
    store_file = []
    for i in os.listdir(list_folder[list_folder.index("Dwn Apps")]):
        files = os.path.join("Dwn Apps", i)
        if os.path.isfile(files):
            store_file.append(i)
    return store_file


def read_file():
    file = get_files()
    os.chdir("Dwn Apps")
    print(os.getcwd())
    with open(file[1]) as text:
        print(text.readlines())
""" read_file() """


from tkinter import *
from tkinter import filedialog
import os
import subprocess
import re
import os
import datetime as dt
from datetime import time
from datetime import date

class Files:
    def __init__(self):
        self.window = Tk()
        self.window.title("Files")
        self.window.resizable(0,1)
        self.right_files()
        self.openfile()
        self.frame()
        self.time_func()
        self.run()

    def openfile(self):
        try:
            filed = filedialog.askopenfilename(title="Open file", filetypes=("all files, *.*"))
            file = filed.split("/")[-1]
            os.chdir(filed.replace("/"+file, ""))
            
            os.system(file)
        except:
            print("Run VSCODE as administrator")

    def time_func(self):
        ## to get the file name and file path. 
        try:
            filed = filedialog.askopenfilename(title="Open file", filetypes=(("text files", "*.txt"),("all files", "*.*")))
            file = filed.split("/")[-1]
            os.chdir(filed.replace("/"+file, ""))

        ## This line of code check the date and time the file was clicked.

            timestamp = os.path.getctime(file)
            now = dt.datetime.fromtimestamp(timestamp)
            show_time = now.time()
            show_date = now.date()
            print("The file was downloaded or created on {} at {}".format(show_date, show_time))
        except Exception as e:
            print(e)
        
        ## This handle the errors the code might encounter using try and exception error handling method.
        
    def frame(self):
        frame = Frame(self.window)
        frame.pack()
    
    def right_files(self):
        button = Button(self.window, text="click", command=self.openfile)
        button.pack()

        button = Button(self.window, text="Check time", command=self.time_func)
        button.pack()

    def run(self):
        self.window.mainloop()
        
""" if __name__ == "__main__":
    files = Files()
    files.run() """

""" import re

def tranform_record(record):
    new_record = re.sub(r"[a-zA-Z ](\d{3})-(\d{3})-(\d{4})",r" (\1) \2-\3",record)
    return new_record
print(tranform_record(("My number is 212-345-1234.")))
print(tranform_record(("Please call 888-555-9999.")))
print(tranform_record(("123-123-1234"))) """

import csv
import os
import re

def contain_domain(address, domain):
    domain_pattern = r'[\w\.-]+@'+domain+'$'
    if re.match(domain_pattern, address):
        return True
    return False

def replace_domain(address, old_domain, new_domain):
    old_domain_pattern = r"" + old_domain + "$"
    address = re.sub(old_domain_pattern, new_domain, address)
    return address

def main():
    old_domain, new_domain = "abc.edu", "xyz.edu"
    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = [] 
    logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w", datefmt="%d-%b-%s")
    with open("write.csv", "r") as file:
        user_data_list = list(csv.reader(file))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]

        for email_address in user_email_list:
            if contain_domain(email_address, old_domain):
                old_domain_email_list.append(email_address)
                replaced_email = replace_domain(email_address,old_domain,new_domain)
                new_domain_email_list.append(replaced_email)
        
        email_key = "" + "Email Address"
        email_index = user_data_list[0].index(email_key)
            
        for user in user_data_list[1:]:
            for old_domain, new_domain in zip(old_domain_email_list,new_domain_email_list):
                if user[email_index] == "" + old_domain:
                    user[email_index] = "" + new_domain
        logging.info(user_data_list)
        with open("report_file.csv", "w+", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerows(user_data_list)

""" main() """


""" import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop() """

""" def to_seconds(hours, minutes, seconds):
    return hours*3600 + minutes*60 + seconds

print("Welcome to this time converter")

cont = "y"

while(cont.lower() == "y"):
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))

    print("This is {} seconds".format(to_seconds(hours, minutes,seconds)))
    print()
    cont = input("Do you want to do another convertion? [y to continue] ")

print("Good bye!") """


""" import shutil
import os
import logging
file_size = os.path.getsize("report.txt")
convert = file_size / (1024 * 1024)
logger = logging.getLogger("log")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s [%(message)s]")
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.debug(convert)
disk_storage = shutil.disk_usage("E:")
to_megabyte = disk_storage.used / (1024 * 1024 * 1024)
to_free = disk_storage.free / (1024 * 1024 * 1024)
logger.info(to_megabyte)
logger.warning(to_free)
logger.error("No error found")
logger.critical("No critical condition found") """
""" print(f"Used space is {to_megabyte: .2f} GB")
print(f"Available space is {to_free: .2f} GB")
to_gigabyte = disk_storage.total / (1024 * 1024 * 1024)
print(f"Total space is {to_gigabyte: .2f} GB") """

""" import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/try/", my_env["PATH"]])

result = subprocess.run(["try"], env=my_env) """



def character_frequency(filename):
    try:
        f = open(filename)
    except OSError:
        return None
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters

import csv
def validate_user(username, minlen):
    assert type(username) == str, "Username must be a string" 
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

def count_dict():
    username = {}
    store_here = []
    myList = ["name","name","age","location","address","address"]
    for name in myList:
        username[name] = myList.count(name)
    for name in username.items():
        store_here.append(name)
    with open("csv_file.csv", "w", newline="") as file:
        f = csv.writer(file)
        f.writerow(("first", "second"))
        f.writerows(store_here)


""" import csv
import operator
users = [{"log_type":"ERROR", "username":"(solm)", "department":"IT Infrastructure"},
{"log_type":"INFO", "username":"(greyc)", "department":"User Experience Research"},
{"log_type":"ERROR", "username":"(lion)", "department":"Development"}]

user_dict = {}
for user in users:
    username = user["username"]
    if username not in user_dict:
        user_dict[username.strip("()")] = {"INFO": 0, "ERROR": 0}
    user_dict[username.strip("()")][user["log_type"]] += 1
sorted_data = sorted(user_dict.items()) """



def find_item(list, item):
  if len(list) == 0:
    return False

  middle = len(list)//2

  if list[middle - 1] == item:
    return True

  if item > list[middle]:
    return find_item(list[:middle], item)
  else:
    return find_item(list[middle+1:], item)
  return False

#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

""" print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False """
    

def binary_search(list, key):
    #Returns the position of key in the list if found, -1 otherwise.

    #List must be sorted:
    list.sort()
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
            print("checking the left side")
        if list[middle] < key:
            print("checking the right side")
            left = middle + 1
    return -1 

""" print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 5))
print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 7))
print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 10))
print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 11)) """


def binary_search(list, val):
    lower_bound = 0
    upper_bound = len(list) - 1

    while lower_bound <= upper_bound:
        mid = (lower_bound+upper_bound) // 2

        if list[mid] == val:
           print(f"The key: {val} found at position {mid + 1} of the list")
        if list[mid] > val:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1
    return f"Sorry the key: {val} not found in the list"
list = ["Amar","Usatz","Naa","Ukasha","Salim","Aziz","Fuseini"]

binary_search(sorted(list), "Ukasha")
    
