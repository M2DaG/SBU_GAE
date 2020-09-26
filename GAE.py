'''
A multiple choice quiz program for Python Beginners.
'''

import random
questions = {
    "When an integer is added or subtracted to a float, what is the product?":{"correct":"a", "answers":['Float','Int','String','Dict','Tuple']},
    "What is 14 % 3?":{"correct":"b", "answers":[1,2,4,3,12]},
    "What is 14 // 3?":{"correct":"e", "answers":[3, 2, 12, 5, 4]},
    "Is not(3<4) True or False?":{"correct":"a", "answers":['False','True']},
    "What is abs(-3.2)?":{"correct":"c", "answers":[-3,-3.2,3.2,3,1.6]},
    "<variable> = <expression> is the general format for an..":{"correct":"b", "answers":['Control Statement', 'Assignment Statement','For Loop','Nested Loop','Operator Statement']},
    "= is an _____ statement. == is an equality operator":{"correct":"a", "answers":['Assignment','equals','arithmetic','operator','nice']},
    "Variable names can be: lowercase and uppercase, the underscore character, 0-9 except the first character. Which of the following are invalid?: myList, 5list, _list, list-3, listG, l_2":{"correct":"e", "answers":['myList, _list','listG, l_2','l_2, myList','myList, _list','5list, list-3']},
    "True or False: The folowing are reserved keywords for the Python language.. False, break, else, if, not, while, None, class, except, import":{"correct":"b", "answers":['False','True']},
    "Strings < and > compare strings using ____":{"correct":"a", "answers":['dictionary order','iteration','length','width','nesting']},
    "'hello * world' concatenates to...":{"correct":"a", "answers":['an error', 'hello world', 'h w l o e ...']},
    "String s * int k gives us...":{"correct":"e", "answers":['sksk','s s k k','ks','sk','k copies of string s']},
    "If s = 'hello', s[4] returns..":{"correct":"b", "answers":['h','o','e','l','ll']},
    "How do you make an empty list?":{"correct":"c", "answers":['()','list = empty','[]','{}','""']},
    "How do you check if rabbit is in list pets?":{"correct":"e", "answers":['pets(rabbit)','find(rabbit)','pets(0)','rabbit.find','"rabbit" in pets']},
    "Are lists mutable?":{"correct":"a", "answers":['Yes','No']},
    "How can I make index 1 in list pets 'Cymric Cat'?":{"correct":"a", "answers":['pets[1]="Cymric Cat"','pets = "Cymric Cat"','Index1 = "Cymric Cat"','pets[0]="Cymric Cat"', 'pets[-3] = "Cymric Cat"']},
    "Is a string mutable?":{"correct":"c", "answers":['Yes, we can change invidual values','Sometimes, depends on the input','No, we cannot change individual characters of a strings value']},
    "How can we change the spelling of a string myCat?":{"correct":"b", "answers":['myCat = new(spelling)','myCat = "NewSpelling"', 'We cannot change the spelling','erase.myCat, new.myCat', 'myCat = Catmy']},
    "True or False: are tuples immutable?":{"correct":"a", "answers":['True','False']},
    "Do tuples use parenthesis () or brackets []?":{"correct":"a", "answers":['Tuples use parenthesis()','Tuples use brackets[]']},
    "Can a tuple be indexed?":{"correct":"b", "answers":['No, they are immutable','Yes, for accessing items']},
    "How do you make a one-item tuple?":{"correct":"d", "answers":['Days = ("Mo")', 'tup = ("Mo")', '"(Mo)"',"Days = ('Mo',)",'tuple("Mo")']},
    "How would you add 'dog' to list pets?":{"correct":"a", "answers":['pets.append("dog")','pets.dog','pets.add("dog")','add.pets("dog")','pets[1]="dog"']},
    "How would you count the number of times 'dog' is in list pets?":{"correct":"c", "answers":['len(dog in pets)', 'len(pets(dog))', 'pets.count(dog)', 'count.dog(pets)', 'pets in dog(#)']},
    "How would you return the index of the first occurence of 'cat' in list pets?":{"correct":"a", "answers":['pets.index(cat)','index.pets(cat)','cats.index(pets)','pets.cat(index)']},
    "How would you add 'fish' into pets before index 3":{"correct":"d", "answers":['pets.insert(fish)', 'pets.fish(insert)', 'pets.insert(0:3,"fish")', 'pets.insert(3,"fish")', 'fish.insert(3, "pets")']},
    "How would you remove last item in list pets?":{"correct":"d", "answers":['pets.subtract()','pets.remove()','pets.minus()','pets.pop()','pets.popoff()']},
    "How would you remove first occurences of 'gerbil' in list pets?":{"correct":"d", "answers":['pets.pop()','pets.anti("gerbil")','remove.pets(gerbil)', 'pets.remove("gerbil")', 'pets.minus("gerbil")']},
    "True or False: append() is a method":{"correct":"b", "answers":['True, it can be called on its own','False, it cannot be called on its own']},
    "Can you sort a list containing numbers and strings?":{"correct":"b", "answers":['Yes, it returns them both in lexicographic order','No, this results in an error']},
    "What are the only 2 tuple methods?":{"correct":"a", "answers":['count(), and index()', 'pop(), and append()','len() and min()','max() and min()','insert(), and drop()']},
    "Which of the following is labeled the wrong type?":{"correct":"e", "answers":['3:Int','3.0:Float','"hello world":String','[1,1,2,3,5,8]:List','8.0:Int']},
    "What Python func can be used to determine object's type?":{"correct":"a", "answers":['type()','len()','info()','help()','whatis()']},
    "True or False: Every Python type is a class":{"correct":"a", "answers":['True. Every value in Pythion is stored in an object','False. No objects in Python are stored in objects']},
    "2.0 ** 1024 will result in":{"correct":"b", "answers":['2048','an error, product too large','an error, product too small', 'pi', '0']},
    "Dividing an int by another int will result in a type":{"correct":"a", "answers":['float','string','tuple','list','index']},
    "Which of these commands results in an incorrect default?":{"correct":"d", "answers":['x = int() : x = 0', 's = str() : s = ""', 'lst = list(): lst = []', 'a = tup(): a = ()']},
    "True or False: True + 5 = 6?":{"correct":"a", "answers":['True','False']},
    "Can an int be converted to a float?":{"correct":"b", "answers":['No.','Yes, except for big calculations (2**10000+3.0)']},
    "Can a float be converted to an int?":{"correct":"b", "answers":['Yes, except for big calculations (2*100000+3.0**2.1)', 'No']},
    "What does int(3.4) yield?":{"correct":"c", "answers":['3.4','-3.4','3','three','"3"']},
    "What does str(-2.72) yield?":{"correct":"d", "answers":['-2.72','2.72','2','"-2.72"','-2']},
    "What is the advantage of using fractions over float type?":{"correct":"a", "answers":['Range of values represented by fractions.fraction is much larger than floats limitation','fractions approximate floats better','floats are only served with ice cream','floats are harder to keep grounded']},
    "Why not always use fractions over float?":{"correct":"c", "answers":['floats evaluate slower than fractions','fractions cannot represent ints', 'floats evaluate much faster than fractions', 'fractions are incomplete numbers','fractions should be seldom used']},
    "What is a module?":{"correct":"d", "answers":['File containing C#','A special float value','An iteration type','A file containing python code','a string']},
    "Which side is input() always used on for an assignment statement?":{"correct":"b", "answers":['left','right']},
    "What type will input() always eval to?":{"correct":"e", "answers":['int','float','fraction','tuple','string']},
    "What is eval() used for?":{"correct":"c", "answers":['converts int into string', 'evaluates the module', 'evaluates string as python expression', 'evaluates your code', 'evaluates lexicographic order of a list']},
    "If <condition>: \n     <indented code block> \n<non-indented statement> \n \nThis code is an example of what?\n":{"correct":"a", "answers":['One way decision control structure>', 'Two way decision control structure', 'Three way decision control structure']},
    "If <condition>: \n     <indented code block> \nelse: \n    <indented code block 2>\n<non-indented statement> \n \nThis code is an example of what?\n":{"correct":"b", "answers":['One way decision control structure>', 'Two way decision control structure', 'Three way decision control structure']},
    "For <variable> in <sequence>: \n   <indented code block>\n<non-indented code block>\nThis code is an example of what?":{"correct":"a", "answers":['For loop statement', 'If loop statement', 'Iteration statement', 'Nesting statement', 'Good coding']},
    "Combining a for loop and an if loop is an example of a:":{"correct":"d", "answers":['Iteration structure', 'One way decision control structure', 'If-for loop control structure', 'Nesting control flow structure', 'Control for if loop structure']},
    "for c in phrase:\n     if c in 'aeiou':\n      print(c)\n This code is an example of... ":{"correct":"a", "answers":['Nesting control flow structure','While loop','Range loop','Assignment statement','Phrase structure']},
    "for i in range(10):\n      print(i)\nThis code yields:":{"correct":"b", "answers":['12345678910','0123456789','iiiiiiiiii','012345678910','9807654321']},
    "range(2,5) yields...":{"correct":"c", "answers":['2,3,4,5','5,4,3', '2,3,4','2,4,5', '5,5']},
    "range(1,14,3) yields...":{"correct":"a", "answers":['1,4,7,10,13','1,3,14','1,2,3,4,5,6,7,8,9,10,11,12,13,14','14,11,8,5,2','14,3,1']},
    "def <function name>(<0 or more variables>):\n      <indented function body>\nThis is the format of..":{"correct":"a", "answers":['Function definition statement', 'Iteration statement', 'Method statement', 'Nesting statement', 'If-for control loop']},
    "How do we add more than one input argument?":{"correct":"c", "answers":['input() + input()', 'argument.append()', 'define a distinct variable name for every argument', 'define an argument for every variable']},
    "Why would a developer use return over print?":{"correct":"e", "answers":['Return gives you a more accurate output','Return prints the statement, print does not', 'Return does not need to be imported', 'Print is slower', 'Print prints the computed value, but does not return it for later use ']},
    "Print(f(3))\ndef f(x)\n    return x ** 2 +1\nWhy does this result in an error?":{"correct":"b", "answers":['Printed before a return is called','Called a function before it is defined','Only floats can be defined','Only floats can be multiplied','Python needs to be updated']},
    "What is a docstring?":{"correct":"a", "answers":['A special comment that describes what a function does','A line that surrounds your code','A string that evaluates your document','A special function you can import']},
    "Where is a socstring placed?":{"correct":"e", "answers":['At the end of your code','In the middle of your code','In the filename of the code','next to a series of ####','Directly below first line of a function definition']},
    "Which object types are immutable":{"correct":"c", "answers":['bool, string, list, int','float, complex, int, string', 'bool, int, float, complex','string, bool, float, int']},
    "Is a list mutable or immutable":{"correct":"a", "answers":['mutable','immutable']},
    "Is a string type mutable or immutable?":{"correct":"b", "answers":['mutable','immutable']},
    "A = [3,4,5]\nB=A\nB[1] = 8\nWhat is A?":{"correct":"e", "answers":['[3,4,5]','[5,8,3]','[8,5,3]','[3,8,5]','[3,8,5]']},
    "How would you swap a = 6, b = 3?":{"correct":"c", "answers":['ab = ba','swap(a,b)','a,b = b,a','reverse(b,a)','b=a']},
    "How can you assign to several variables simultaneously?":{"correct":"c", "answers":['assign(l,j,k,0)','multi(j,k,l,0)','l=j=k=0','0,j=k,l']},
    "What is g(a) in the following program?\na=3\ng(a)\ndef g(x)\n  x=5":{"correct":"b", "answers":['5 because  the variable is a mutable object','3 because the variable is an immutable object','15 because the objects are multiplied','fraction(3,5)']},
    "What happens when the name of a mutable object is passed as the argument of a func call like so:\ndef h(lst):\n    lst[0]=5\nMyList = [3,6,9,12]\nh(myList)":{"correct":"a", "answers":['[5,6,9,12]','[3,6,9,12]','[12,9,6,3]','[4,3,2,1]']},
    "What if string contains both types of quotes?":{"correct":"c", "answers":['Use /quote to display a quote','Be sure to comment out your quote','use escape sequence (backward slash)\" or  (backward slash)\' to indicate quote is not delimiter', 'Use /" to indicate quote is not delimiter']},
    "What do triple quotes do?":{"correct":"b", "answers":['Emphasize your string','Create multiline text','Allow doublespacing','Enable Python 4.0']},
    "S = 'hello'\nWhat is S[3:4]?":{"correct":"d", "answers":['h','o','e','l',' ']},
    "S = 'hello'\nWhat is S[-3:-1]":{"correct":"c", "answers":['he','el','ll','lo','ho']},
    "Pets = ['goldfish','cat','dog']\nWhat is pets[-3:-1]?":{"correct":"b", "answers":["['cat','dog']","['goldfish','cat']","['cat','goldfish']","['dog','goldfish']"]},
    "message = ('top secret')\nHow do you capitalize first letter?":{"correct":"c", "answers":['message.upper()','message.lower()','message.capitalize','You cannot capitalize!']},
    "message = ('top secret')\nHow do you capitalize all letters?":{"correct":"a", "answers":['message.upper()','message.lower()','message.capitalize','You cannot capitalize!']},
    "What does message.replace('top','no') do?":{"correct":"b", "answers":['Makes message ="no secret"','returns an error, to change string must use public=message.replace("top","no")','replaces no with top']},
    "What does translate do?":{"correct":"d", "answers":['translates code into other languages','translates from english to spanish','provides a translation tool for binary','maps characters','nothing']},
    "x = '2;3;4;5'\nWhat does x.split(';') do?":{"correct":"a", "answers":["returns ['2','3','4','5']","returns 2 3 4 5 ","returns [2345]","returns[2 3 4 5]"]},
    "How would you replace an old substring with new?":{"correct":"c", "answers":['s.map(old,new)','s.translate(old,new)','s.replace(old,new)','s.renew(old,new)']},
    "x = '2;3;4;5'\nWhat does x.strip() do?":{"correct":"b", "answers":['strips the delimiter','creates a copy of string x','removes the escape sequence', 'changes mutability']},
    "How can we print (n,r) and seperate them by ';'?":{"correct":"a", "answers":["print(n,r, sep = ';']","print(n,r,;)","sep = ';' print(n,r)","(n,r) sep = ;"]},
    "What is the epoch on unix and mac?":{"correct":"e", "answers":['00:00 Jan 1st 2020, LAX time','00:00:00 of December 31st 1980, Hamburg time','00:00 Feb 1st 1980, Japan time','00:00:00 of March 3rd 1960, Palo Alto time','00:00:00 of January 1st 1970, Greenwhich time']},
    "What is an absolute pathname?":{"correct":"c", "answers":['sequence of files storing info about the code','sequence of directories that must be traversed starting from current working directory','sequence of folders starting from root that must be traversed to get to file','absolute way to find your file relatively']},
    "What is a relative pathname?":{"correct":"b", "answers":['sequence of files storing info about the code','sequence of directories that must be traversed starting from current working directory','sequence of folders starting from root that must be traversed to get to file','absolute way to find your file relatively']},
    "How would you open ('example.txt')?":{"correct":"a", "answers":["infile = open('example.txt')","open.read(example.txt)","infile = open(example.txt)",'infile = example.txt(open)']},
    "What are the 3 arguments for open?":{"correct":"a", "answers":['file name, pathname, mode','mode, pathname, language','file name, python version, OOP','pathname, mode, date']},
    "What is the default read mode?":{"correct":"e", "answers":['open','write','append','append+','read']},
    "What does the r open mode do?":{"correct":"d", "answers":['writing','text mode','reading and writing','reading','append']},
    "What does the w open mode do?":{"correct":"a", "answers":['writing','text mode','reading and writing','reading','append']},
    "What does the a open mode do?":{"correct":"e", "answers":['writing','text mode','reading and writing','reading','append']},
    "What does the r+ open mode do?":{"correct":"c", "answers":['writing','text mode','reading and writing','reading','append']},
    "What does the t open mode do?":{"correct":"b", "answers":['writing','text mode','reading and writing','reading','append']},
    "What does infile.readline() do?":{"correct":"a", "answers":['read file until new line characters or end','write strings to file infile','read n characters from file infile, return chars as string','read file until end of file and return chars read as a list lines','close the file']},
    "What does outfile.write(s) do?":{"correct":"b", "answers":['read file until new line characters or end','write strings to file infile','read n characters from file infile, return chars as string','read file until end of file and return chars read as a list lines','close the file']},
    "What does infile.read(n) do?":{"correct":"c", "answers":['read file until new line characters or end','write strings to file infile','read n characters from file infile, return chars as string','read file until end of file and return chars read as a list lines','close the file']},
    "What does infile.readlines() do?":{"correct":"d", "answers":['read file until new line characters or end','write strings to file infile','read n characters from file infile, return chars as string','read file until end of file and return chars read as a list lines','close the file']},
    "What does file.close() do?":{"correct":"e", "answers":['read file until new line characters or end','write strings to file infile','read n characters from file infile, return chars as string','read file until end of file and return chars read as a list lines','close the file']},
    "Why is outfile.close() important?":{"correct":"c", "answers":['close shuts down your program','your computer will freeze if you do not use close','writes are saved to disk from the buffer','the buffer will not close without calling outfile.close']},
    "What is a built-in exception?":{"correct":"a", "answers":['errors that occur during execution of the program with correct syntax','errors that occur during execution of the program without correct syntax','errors that involve an input output error','errors that occur due to spelling error']},
    "Which error occurs when the float expression evaluates too large?":{"correct":"a", "answers":['Overflow error','Zero Division error', 'Value error', 'IO error', 'Name Error']},
    "Which error occurs when attempting to divide by zero":{"correct":"b", "answers":['Overflow error','Zero Division error', 'Value error', 'IO error', 'Name Error']},    
    "Which error occurs when an operator or function has an argument of right type but incorrect value":{"correct":"c", "answers":['Overflow error','Zero Division error', 'Value error', 'IO error', 'Name Error']},
    "Which error occurs when an I/O operation fails for an I/O reason":{"correct":"d", "answers":['Overflow error','Zero Division error', 'Value error', 'IO error', 'Name Error']},
    "Which error occurs when attempting to evaluate an unassigned identifier":{"correct":"e", "answers":['Overflow error','Zero Division error', 'Value error', 'IO error', 'Name Error']},
    "Trying to open a file for reading that doesn't exist is an example of what?":{"correct":"d", "answers":['Overflow error','Zero Division error', 'Value error', 'IO error', 'Name Error']}
}

list_questions = list(questions.items())

random.shuffle(list_questions)

amount_questions = str(len(questions))
print("There are " + amount_questions + " questions")
num_questions = int(input("How many questions would you like to try?:"))

list_questions = list_questions[:num_questions]

shuffled_questions = dict(list_questions)



anslabels = ['a','b','c','d','e']
correct = 0
total = len(questions)

question_num = 0
incorrect_questions = []

input("\nThank you for trying out Mike Garcia's Intro to Programming Quiz!\nPress ENTER to start!\n")


for k, v in shuffled_questions.items():
    
    
    print(k)
    x = 0
    for ans in v["answers"]:
        print(anslabels[x] + ": " + str(ans))
        x += 1
    answer = input("\nType a, b, c, d, or e to select your answer. Then press ENTER.\n")
    if(answer == v["correct"]):
        correct += 1
    else:
      incorrect_questions.append(question_num)
    print("\n")

    question_num += 1 # 

score = str((correct / num_questions) * 100) + "%"
print("Quiz Complete!\nYour score is " + score + " on this quiz.")


for i in incorrect_questions:
  question = list_questions[i][0]
  correct_answer = list_questions[i][1]

  print('\n')
  print(question)
  print(correct_answer["answers"][anslabels.index(correct_answer["correct"])])
