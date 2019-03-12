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
                storage [--storage=SERVICE] create dir DIRNAME DESTDIR
                storage [--storage=SERVICE] list dir DIRNAME
                storage [--storage=SERVICE] delete dir DIRNAME


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
