import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_File(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'HtM0YUjFjNUAAAAAAAAAAdfWo3qWUvSKmLXUYQjRh3SmfUKvi4A8niHqrtLFdN4O'
    t = TransferData(access_token)
    file_from = input("enter the file path: ")
    file_to = input("enter the dropbox path: ")
    t.upload_File(file_from,file_to)
    print("file is moved to dropbox")

if __name__ == '__main__':
    main()