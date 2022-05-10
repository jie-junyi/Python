import re

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