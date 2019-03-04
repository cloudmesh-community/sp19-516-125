"""
        ::

          Usage:
                storage [--storage=SERVICE] put FILENAME DESTDIR
                storage [--storage=SERVICE] get FILENAME DESTDIR
                storage [--storage=SERVICE] delete FILENAME
                storage [--storage=SERVICE] size FILENAME
                storage [--storage=SERVICE] info FILENAME
                storage [--storage=SERVICE] create FILENAME
                storage [--storage=SERVICE] sync SOURCEDIR DESTDIR
                storage [--storage=SERVICE] search FILENAME
                storage [--storage=SERVICE] add FOLDERNAME DESTDIR
                

          This command does some useful things.

          Arguments:
              FILE      a file name
              DESTDIR   destination directory for uploads and downloads
              SOURCEDIR source directory for syncing directories
              FOLDERNAME name of new folder
              

          Options:
              -f      specify the file

          Example:
            set storage=box
            storage  put FILENAME

            is the same as 

            storage  --storage=box put FILENAME


        """
