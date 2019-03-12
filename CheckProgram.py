import subprocess

import json
import platform


def createjson(arrayDpkg):
    """RETURN JSON"""
    jsonArray = []

    for Lindex in range(0, len(arrayDpkg) - 1):
        my_json = json.dumps({arrayDpkg[Lindex][1]: [arrayDpkg[Lindex][2],
                                                     arrayDpkg[Lindex][3]]})
        jsonArray.append(my_json)

        return jsonArray


def processingData(dataarray):
    for index in range(5, len(dataarray)):

        tempData = []
        for Lindex in dataarray[index].split(" "):
            if Lindex != "":
                tempData.append(Lindex)
        ClearList.append(tempData)

    return ClearList


def displayTable(data):

    for Lindex in range(0, len(data) - 1):

        print(Lindex, data[Lindex][1], "ver: {} ".format(data[Lindex][2]), data[Lindex][3])


if "__main__" == __name__:

    if platform.system() == "Linux":
        # Get system data from unema / hostname
        hostName = str(subprocess.check_output(['hostname']))
        uname = str(subprocess.check_output(['uname', '-v'])).split(" ")

        # Get programs list  from dpkg -l
        outputResult = str(subprocess.check_output(['dpkg', '-l']))
        StripResFromNewLineChar = outputResult.split('\n')
        GeneralArrayAfterStriped = StripResFromNewLineChar[0].split("\\n")

        flag = True

        print("[*] Hostname - {}.".format(hostName))
        print("[*] System version - {}.".format(uname[2]))  # platform.uname()
        print("[*] Found - {} program(s).".format(len(GeneralArrayAfterStriped)))
        inp: str = input("Do you want display all?[y/n]:")

        while flag and 'n' != inp.lower():
            print()
            print("[*] Hostname - {}.".format(hostName))
            print("[*] System version - {}.".format(uname[2]))  # platform.uname()
            print("[*] Found - {} program(s).".format(len(GeneralArrayAfterStriped)))
            ClearList = []
            table = processingData(GeneralArrayAfterStriped)
            createjson(ClearList)
            print()
            if inp == 'y':
                displayTable(ClearList)
            else:
                flag = False
                exit(-1)

            inp = input("Do you want display all?[y/n]:")
        else:
            exit(-1)
