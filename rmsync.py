from gdrivesync.sync import sync_with_local
from gdrivesync.storage import remove_entry, add_or_update
import subprocess

RMAPI_PATH = './rmapi'

def main():
    to_upload = sync_with_local()
    for book in to_upload:
        remove_entry(book['id'])
        file_path = './downloads/' + book['name']
        status = subprocess.call(
            [RMAPI_PATH, "put", file_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        
        if status == 0:
            print("Uploaded successfully 🚀")
            add_or_update(**book)
        elif status == 1:
            print("The book is already on your device, no need to upload")
            add_or_update(**book)
        else:
            print("Upload failed")
            print(status)


if __name__ == '__main__':
    main()
    print("You are all set 🚀")