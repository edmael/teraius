# TERAIUS - TElegram RAndom Image Uploader Script
A very basic (and poorly written, probably) script that uploads a random image from a series of folder-organized gallery to Telegram, once every time you run it. This is script uses [Telethon](https://github.com/LonamiWebs/Telethon) to connect to Telegram.

The code is (let me emphatize that) dirty and it's used to randomly post an image using my name in a number of given groups. The script basically does this:

* get a list of all the folders in the `images` folder
* chooses a random folder between them and check if it's empty
* pick a random image in the first non-empty folder found
* post the image in a chat with a caption that says how many images are still in that folder
* move the posted image to the `uploaded` folder so that it won't get posted again

There are many improvements that can be done to this code and you're very welcome to do that with a pull request!

## How to use
A simple `python teraius.py` will run the script just fine, but you need to edit it first.

* create an `images` and `uploaded` folder where you plan to keep the script
* populate the `images` folders with sub-folders
* go to [my.telegram.org](https://my.telegram.org) and get your API keys
* edit `teraius.py` and insert your API keys
* get the [Entity](https://docs.telethon.dev/en/latest/concepts/entities.html?highlight=entity) you want to post the images to (I need to make this easier, right now I've commented out the command you can use to do it, check line 33) and insert it in the `client.send_file` on line 34

To test the script you can send the image to yourself by using the `'me'` Entity: this way the image get sent directly to you.