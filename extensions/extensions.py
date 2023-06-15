#accept input from a user
fileName = input("Extension: ")

def extension(b):
    match b :
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

if fileName.count(".") == 0:
    print("application/octet-stream")

elif fileName.count(".") == 1:
    a, b = fileName.split(".")
    b = b.lower().strip()
    extension(b)
elif fileName.count(".") == 2:
    a, c , b = fileName.split(".")
    b = b.lower().strip()
    extension(b)