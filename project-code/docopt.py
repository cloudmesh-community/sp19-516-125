        """
        ::

          Usage:
                storage [--storage=SERVICE] put FILENAME DESTDIR
                storage [--storage=SERVICE] get FILENAME DESTDIR
                storage [--storage=SERVICE] delete FILENAME
                storage [--storage=SERVICE] size FILENAME
                storage [--storage=SERVICE] info FILENAME
                storage [--storage=SERVICE] create FILENAME
                storage [--storage=SERVICE] search FILENAME
                storage [--storage=SERVICE] createdir DIRNAME DESTDIR
                storage [--storage=SERVICE] listdir DIRNAME
                storage [--storage=SERVICE] deletedir DIRNAME


          This command creates, deletes, and returns information on directories and files in cloud storage services.

          Arguments:
              FILE      a file name
              DESTDIR   destination directory for uploads and downloads
              SOURCEDIR source directory for syncing directories
              DIRNAME name of new folder


          Example:
            set storage=box
            storage put FILENAME DESTDIR

            is the same as 

            storage  --storage=box put FILENAME DESTDIR


        """
