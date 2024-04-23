import os
import shutil
import webbrowser

work_dir = os.getcwd()

def jdk_setup():
    os.system(" sudo -S apt-get remove -y openjdk*")
    os.system(" sudo -S apt update ")
    os.system(" sudo -S apt install -y openjdk-8-jdk openjdk-8-jre")
    # netbeans setup
    os.system(" sudo -S apt update && sudo -S apt upgrade")
    os.system(" sudo -S snap install netbeans --classic")

def mpj_setup():
    os.system("wget https://sourceforge.net/projects/mpjexpress/files/releases/mpj-v0_44.tar.gz/download")
    os.system("mv download mpj.tar.gz")
    os.system("gunzip mpj.tar.gz")
    os.system("tar -xvf mpj.tar")

    temp_path = f'{os.path.expanduser("~")}/temp'
    if not os.path.exists(temp_path):
        os.makedirs(temp_path)
    shutil.move(f"{work_dir}/mpj-v0_44",f"{temp_path}/mpv")


def clone_prac(n):
    os.system("git clone https://github.com/meghadandapat/BE-IT-DS")
    main_path = f'{os.path.expanduser("~")}/Assign{n}'
    if not os.path.exists(main_path):
        os.makedirs(main_path)

    source_folder = f'{work_dir}/BE-IT-DS/Assign{n}'

    for file_name in os.listdir(source_folder):
        source = f'{source_folder}/{file_name}'
        destination = f'{main_path}/{file_name}'
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print('File Copied', file_name)


if __name__ == '__main__':
    jdk_setup()
    os.system("clear")
    n = int(input("Enter Practical Number: "))
    clone_prac(n)
    if n == 3:
        mpj_setup()
        os.system("clear")
        print("MPJ Express Setup is Done: Please Do the Enviroment Variables")

    webbrowser.open(f'https://github.com/Broken-Lab/temp/blob/master/Assign{n}.md')
