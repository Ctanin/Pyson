import os
Double_Quotation_Mark='"'   #双引号常量
Is_Enter=False   #换行标志

def Find_Outside_Command(command):   #Pyson伪指令检测并执行
    if command == "help":
        print("Type help() for interactive help, or help(object) for help about object.")
        return True   #返回True则检测到伪指令
    if command == "copyright":
        print("Copyright (c) 1919-2019 Pyson Software Foundation.\nAll Rights Reserved.\n")
        print("Copyright (c) 1981 ctanin.github.io/pyson.github.io.\nAll Rights Reserved.\n")
        print("Copyright (c) 1919-2810 Minicrash Play Company.\nAll Rights Reserved.\n")
        print("Copyright (c) 1919-1145 Small Seal Script Company, Democratic Kampuchea.\nAll Rights Reserved.")
        return True
    if command == "credits":
        print("    Thanks to Dr.Haoyang Zhang, Pol Pot, jvav.top, ctanin.github.io/pyson.github.io and a cast of thousands\n   for supporting Pyson development.  See ctanin.github.io/pyson.github.io for more information.")
        return True
    if command =="license":
        print("Type license() to see the full license text")
        return True
    if command == "about":
        os.system("about.exe")
        return True
    return False

def Check_Command_Syntax(command):   #检测语法错误
    if command[-1] == ';':   #检测是否使用了英文分号
        print("[Error] stray ';' in program")
        return True
    if command[-1] != '；':   #检测是否有中文分号
        print("[Error] expected '；' after '"+command+"'")
        return True   #返回True则检测到语法错误
    if command.find("import") != -1:   #检测是否使用了import
        print("[Error] "+Double_Quotation_Mark+"import"+Double_Quotation_Mark+" not defined")
        return True
    if command[0:4] == "print" and command[5] != 'f':   #检测是否使用了print函数
        print("[Error] "+Double_Quotation_Mark+"print"+Double_Quotation_Mark+" not found,Dr.Haoyang,Zhang adviced you to use "+Double_Quotation_Mark+"printf"+Double_Quotation_Mark)
        return True
    if command.find("input") != -1:   #检测是否使用了input函数
        print("[Error] "+Double_Quotation_Mark+"input"+Double_Quotation_Mark+" not found,Dr.Haoyang,Zhang adviced you to use "+Double_Quotation_Mark+"scanf"+Double_Quotation_Mark)
        return True
    return False

def Correct_Command(command):   #使Pyson命令能正常执行
    global Is_Enter
    answer=""
    if command.find("printf") != -1:
        answer=command[:5]+command[6:]
    if command.find("scanf") != -1:
        answer=command.replace("scanf","input")
    if command.find("include") != -1:
        answer=command.replace("include","import")
    if command.find("endl") != -1:
        if answer != command:
            answer=answer.replace("endl","")
            Is_Enter=True
        else:
            answer=command.replace("endl","")
            Is_Enter=True
    answer=answer[:-1]
    return answer

#main函数
print("Pyson 0.0.0 (Pre Version) (tags/v0.0.0, February  24 2024, 17:05:00) [MacDOS v.1919 114 bit (Intel64)] on Jvav32")
print("Type "+Double_Quotation_Mark+"help"+Double_Quotation_Mark+", "+Double_Quotation_Mark+"copyright"+Double_Quotation_Mark+", "+Double_Quotation_Mark+"credits"+Double_Quotation_Mark+" or "+Double_Quotation_Mark+"license"+Double_Quotation_Mark+" for more information.")
while True:
    Is_Enter=False   #初始化换行标志
    command=input(">>> ")
    if command == "exit":
        break
    if Find_Outside_Command(command) == True:
        continue
    if Check_Command_Syntax(command) == True:
        continue
    try:
        exec(Correct_Command(command))
        if Is_Enter == True:
            print("\n",sep='',end='')
    except BaseException as ERROR:  #打印错误信息
        print("[Error] ",sep='',end='')
        print(ERROR)
os.system("pause")