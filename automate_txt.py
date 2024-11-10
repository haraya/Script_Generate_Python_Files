# Code of automation txt into new folder
import os


folder_name = "Name of the Folder"
def Generate_Python_files(input_file):
    try:

        os.makedirs(folder_name, exist_ok=True)

        with open(input_file,'r') as file:
            data = file.read()

            sections = data.split("---")

            for i, section in enumerate(sections):
                if section.strip():

                    lines = section.strip().splitlines()
                    title_line = lines[0] if lines else print(f"File_{i+1}")

                    if "title:" and " " in title_line:
                       title_line= title_line.replace("title:", "")
                       title_line=  title_line.replace(" ", "_")

                    content = "\n".join(lines[1:])
                    if "." in content:
                        content = content.replace(".", ".\n#")

                if i<10:
                    output_filename = os.path.join(folder_name, f"0{i+1}{title_line}.py")

                elif i>=10:
                    output_filename = os.path.join(folder_name, f"{i}{title_line}.py")


                #print(output_filename)
                with open(output_filename,'w') as output_file:
                    output_file.write(f"# {content}")

                print(f"Created file: {title_line}")




    except FileNotFoundError:
        print("Error with the file")

Generate_Python_files("example.txt")