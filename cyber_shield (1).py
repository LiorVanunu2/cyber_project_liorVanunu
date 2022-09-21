PATH = "\Desktop\פרויקט סייבר-20220914T071231Z-001\פרויקט סייבר\סבב א\נספחים\Logs"
import os
import datetime

EVENT_INDEX_TIME = 0
EVENT_INDEX_IP = 1
EVENT_INDEX_ACTION = 2
EVENT_INDEX_NAME = 3
VALID_INDEX_NAME = 0
VALID_INDEX_IP = 1
VALID_INDEX_TIME = 2


def get_path():
    path = input("Enter a path")
    return path


def read_log_files(path):
    list_documents = []
    for file in os.listdir(path):
        list_documents.append(file)
    return list_documents


def read_file_loge(path, list_logs):
    for file in list_logs:
        text_f = open(path + "\\" + file, "r")
        print(text_f.read())


def make_list_file(path, list_logs):
    list_event = []
    for file in list_logs:
        file_data = []
        file = open(path + "\\" + file, "r")
        lines = file.read().split('\n')
        lines = lines[:-1]
        for line in lines:
            line_split = line.split(': ')
            file_data.append(line_split[1])
        list_event.append(file_data)
    return list_event


def list_valid_behavior():
    file_valid = open('valid.txt', "r")
    list_lines = file_valid.read().split('\n')
    list_behavior = []
    for line in list_lines:
        line_split = line.split(' ')
        list_behavior.append(line_split)
    return list_behavior
def return_behavior_user(name, list_behavior):
    for b in list_behavior:
        if b[VALID_INDEX_NAME]==name:
            return b

def suspicous_event(list_event, list_behavior):

    for event in list_event:
        if event[EVENT_INDEX_ACTION]=="Log In":
            list_b=return_behavior_user(event[EVENT_INDEX_NAME], list_behavior)
            # if event[EVENT_INDEX_TIME]== list_b[]

# def read_file():
#     folderpath = "C:\Users\pc\PycharmProjects\cyber_lior\\valid.txt"
#     inputlst = [os.listdir(folderpath)]
#     filenamelist = []
#     list_data = []
#     for filename in os.listdir(folderpath):
#         if filename.endswith(".txt"):
#             filenamelist.append(filename)
#     for i in range(len(filename)):
#         file = open(filename[i])
#         # read the file as a list
#         data = file.readline()
#         # close the file
#         file.close()
#         list_data.append(data)
#     return list_data


# def Search_exceptional_events():
#     log_list_data = read_log_files()
#     list_data = read_file()
#     for i in range(len(log_list_data)):
#         log_list_data[i]


def main():
    path = get_path()
    list_logs = read_log_files(path)
    read_file_loge(path, list_logs)
    list_event = make_list_file(path, list_logs)
    list_behavier = list_valid_behavior()
    print(list_event)
    print(list_behavier)



if __name__ == '__main__':
    main()
