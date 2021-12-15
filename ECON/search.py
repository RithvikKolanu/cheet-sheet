searchquery = input("enter")
print("")
def search_34(query):
    listofchapters = ['chapter 1.txt', 'chapter 2.txt', 'chapter 3.txt', 'chapter 4.txt', 'chapter 5.txt', 'chapter 6.txt', 'chapter 7.txt', 'chapter 8.txt', 'chapter 9.txt', 'chapter 10.txt', 'chapter 11.txt', 'chapter 12.txt', 'chapter 13.txt', 'chapter 14.txt', 'chapter 15.txt', 'chapter 16.txt', 'chapter 17.txt', 'chapter 18.txt', 'chapter 19.txt', 'chapter 20.txt', 'chapter 21.txt', 'chapter 22.txt', 'chapter 23.txt', 'chapter 24.txt', 'chapter 25.txt', 'chapter 26.txt', 'chapter 27.txt', 'chapter 28.txt', 'chapter 29.txt', 'chapter 30.txt', 'chapter 31.txt', 'chapter 32.txt', 'chapter 33.txt', 'chapter 34.txt']
    results_list = []
    def search(file):
        with open(file, "r") as a_file:
            all_lines = a_file.readlines() 
            index_match = len(all_lines) - 1 
            for index, line in enumerate(all_lines):
                if line[0].isnumeric() == True and query.strip().lower() in line[3:].strip().lower():
                    sub_lines = (all_lines[index:index + 9])
                    for x in sub_lines:
                        if x[0:6] == "Answer": 
                            results_list.append([line, x])
                elif index == index_match:
                    return False
        a_file.close()
    for chapter in listofchapters:
        if search("chapters/"+chapter) != False:
            print(chapter)
            search(chapter)
            print("")
    return results_list
search_34(searchquery)
       
    



