import re

# 注意search与findall中的“（）”的含义是不一样的
# findall中的“（）”表示的是分组，最终返回的只有括号里的内容
# 而search与match中的“（）”，只有在.group（1）命令语句中才会返回正则表达式中第一个括号中匹配到的内容
# 以此类推，.group（2）返回正则表达式中第二个括号匹配到的内容
# 且.group()与.group(0)的运行结果相同


if __name__ == '__main__':
    '''
    
    string = "Let's study one two three five four six seven eight nine ten"
    pattern = "(one)|(two)|(three)|(four)|(five)|(six)"
    matchList = re.findall(pattern, string) #加上了"|"号
    print(matchList)
    '''
    string = "3 min 46 ms sec 300 "
    matchList = re.findall(r"(\d{0,}) (min)|(sec)|(ms)", string)
    print(matchList)