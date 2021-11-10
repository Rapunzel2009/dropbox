from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        with open(file_from,'rb')as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token='FCSp7tqIhOMAAAAAAAAAAWngbwKoeELCmexExp8GWzhMWhJpD6ufADVofXAHea1B'
    transferData=TransferData(access_token)
    
    file_from="frenxh.pdf"
    file_to='/test/frenxh.pdf'

    transferData.upload_file(file_from, file_to)
    print("file has been uploaded")

main()

      

        
   