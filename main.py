import os

files = os.listdir()


def separatelist(extlist):
    for item in files:
        if os.path.splitext(item)[1] == '':
            files.remove(item)
    lst = [file for file in files if os.path.splitext(file)[1].lower() in extlist]
    for file in lst:
        files.remove(file)
    a = os.path.basename(__file__)
    if a in files:
        files.remove(a)
    return lst


def create_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
        if folder_name in files:
            files.remove(folder_name)


def move(movelist, extlist='.other', msg='others'):
    if not movelist:
        print(f"{msg} are not here!!!\n")
    elif extlist[0] == '.png':
        for elmnt in movelist:
            os.replace(elmnt, f'images/{elmnt}')
    elif extlist[0] == '.mp4':
        for elmnt in movelist:
            os.replace(elmnt, f'videos/{elmnt}')
    elif extlist[0] == '.doc':
        for elmnt in movelist:
            os.replace(elmnt, f'documents/{elmnt}')
    elif extlist[0] == '.mp3':
        for elmnt in movelist:
            os.replace(elmnt, f'musics/{elmnt}')
    elif extlist[0] == '.exe':
        for elmnt in movelist:
            os.replace(elmnt, f'binaries/{elmnt}')
    elif extlist[0] == '.c':
        for elmnt in movelist:
            os.replace(elmnt, f'codes/{elmnt}')
    elif extlist[0] == '.lnk':
        for elmnt in movelist:
            os.replace(elmnt, f'shortcuts/{elmnt}')
    elif extlist[0] == '.other':
        for elmnt in movelist:
            os.replace(elmnt, f'others/{elmnt}')


if __name__ == '__main__':
    count = 0
    img_ext = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.ico']
    vdo_ext = ['.mp4', '.mkv', '.wmv', '.avi', '.f4v', '.flv']
    doc_ext = ['.doc','.docx', '.pdf', '.ppt', '.pptx', '.txt', '.xls', '.xlsx', '.rft', '.ott', '.odt', '.ods', '.odp', '.csv', '.djvu']
    exe_ext = ['.exe', '.bat', '.dll', '.msi', '.bin']
    msc_ext = ['.mp3', '.m4a', '.flac', '.wav', '.cvs', '.dts']
    code_ext = ['.c', '.py', '.html', '.cpp', '.css', '.js', '.java', '.ejs', '.json', '.php', '.vb', '.xml', '.rb', '.pl', '.sh', '.sql']
    srt_ext = ['.lnk']

    images = separatelist(img_ext)
    videos = separatelist(vdo_ext)
    documents = separatelist(doc_ext)
    musics = separatelist(msc_ext)
    binaries = separatelist(exe_ext)
    codes = separatelist(code_ext)
    shortcuts = separatelist(srt_ext)
    others = [file for file in files]

    if images:
        create_folder('images')
        count += 1
    move(images, img_ext, 'images')

    if videos:
        create_folder('videos')
        count += 1
    move(videos, vdo_ext, 'videos')

    if documents:
        create_folder('documents')
        count += 1
    move(documents, doc_ext, 'documents')

    if musics:
        create_folder('musics')
        count += 1
    move(musics, msc_ext, 'musics')

    if binaries:
        create_folder('binaries')
        count += 1
    move(binaries, exe_ext, 'binaries')

    if codes:
        create_folder('codes')
        count += 1
    move(codes, code_ext, 'codes')

    if shortcuts:
        create_folder('shortcuts')
        count += 1
    move(shortcuts, srt_ext, 'shortcuts')

    if others:
        create_folder('others')
        count += 1
    move(others)

    if count == 0:
        print("\n\t everything is sorted!!!")
    elif count == 1:
        print("1 type of file has sorted!!!")
    else:
        print(f"{count} types of files have sorted!!!")

    input("\n Enter any key to exit: ")
    print("\n\t bye....")
