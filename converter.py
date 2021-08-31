import os

from lxml import etree,html

def file_reader(directory):

    for filename in os.listdir(directory):
    
        f = os.path.join(directory, filename)
    
        if os.path.isfile(f):
            
            convert_to_xml(f)

def convert_to_xml(filename):

    base = os.path.basename(filename)

    xml_file = os.path.join(os.path.dirname(filename),os.path.splitext(base)[0] + '.xml')
    
    with open(filename, 'r', encoding='utf-8') as inp:
        
        htmldoc = html.fromstring(inp.read()) 

    with open(xml_file,'wb') as out:

        out.write(etree.tostring(htmldoc))

def main():

    print("Press 1 to: Convert multiple HTML files within the same directory.")

    print("Press 2 to: Convert a single HTML file.")

    userChoice = int(input("Your choice: "))

    if userChoice == 1:

        path = str(input("Please give the path to the HTML files: "))

        file_reader(path)

        print(f"[+] Files converted successfully to {path}")

    
    if userChoice == 2:

        path = str(input("Please give the path to the HTML file: "))

        convert_to_xml(path)

        print(f"[+] File converted successfully to {path}")

    else:

        print("Please provide a valid input and run the program again.")

        exit()


if __name__ == '__main__':
    
    main()