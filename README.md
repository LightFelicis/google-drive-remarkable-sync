# Remarkable with Google Drive sync tool

Sync PDFs stored in Google Drive with Remarkable device.

## Preparation

1. Create credentials for your Google API and place them in this project root directory. Tutorial can be found here: [link](https://developers.google.com/workspace/guides/create-project)
2. Install Python libraries
   
    ``` Python
          pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib TinyDB
    ```
3. Download rmapi from [official repository](https://github.com/juruen/rmapi/releases/) and unzip it in this project root directory.

## Usage

```
python3 rmsync.py
```
