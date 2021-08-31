import os

from lxml import etree,html

def file_reader(directory):

    for filename in os.listdir(directory):
    
        f = os.path.join(directory, filename)
    
        if os.path.isfile(f):
            
            convert_to_xml(f)

def convert_to_xml(filename):

    base = os.path.basename(filename)

    xml_file = (os.path.dirname(filename) + '/' + os.path.splitext(base)[0] + '.xml')
    
    with open(filename, 'r', encoding='utf-8') as inp:
        
        htmldoc = html.fromstring(inp.read()) 

    with open(xml_file,'wb') as out:

        out.write(etree.tostring(htmldoc))

def main():

    userChoice = str(input("Your choice:"))

    if choice == 1:

        path = str(input("Please give the path to the HTML files: "))

        file_reader(path)

        print(f"[+] Files converted successfully to {path}")

    
    if choice == 2:

        path = str(input("Please give the path to the HTML file: "))

        convert_to_xml(path)

        print(f"[+] File converted successfully to {path}")

    else:

        print("Please provide a valid input and run the program again.")

        exit()


if __name__ == '__main__':
    
    main()