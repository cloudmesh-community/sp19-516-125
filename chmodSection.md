##CHMOD
---
The chmod command, first seen in AT&T Unix version 1, is a shortening of ‘change mode’ and changes the access permissions 
for a given file system object(s). It uses the following syntax:
```
chmod [options] mode[,mode] file1 [file2…]
```
The option parameters modify how the process runs, including what information is outputted to the shell: 
| Option:	              | Description:                                      |
| --------------------- | ------------------------------------------------- |
| -f, --silent, --quiet |	Forces process to continue even if errors occur   |
| -v, --verbose	        | Outputs for every file that is processed          |
| -c, --changes         |	Outputs when a file is changed                    |
| --reference=RFile	    | Uses RFile instead of Mode values                 |
| -R, --recursive	      | Make changes to objects in subdirectories as well |
| --help	              | Show help                                         |
| --version	            | Show version information

Modes specify which rights to give to which users. Potential users include the user who owns the file, users in the file’s Group, other users not in the file’s Group, and all, and are abbreviated as ‘u’, ‘g’, ‘o’, and ‘a’ respectively. More than one user can be specified in the same command, such as 
```
chmod –v ug(operator)(permissions) file.txt
```
If no user is specified, the command defaults to ‘a’. Next, a ‘+’ or ‘-‘ indicates whether permissions should be added or removed for the selected user(s). The permissions are as follows:
| Permission:	| Description:                                             |
| ----------- | -------------------------------------------------------- |
|r            |	Read                                                     |
|w	          | Write                                                    |
|x	          | Execute file or access directory                         |
|X	          | Execute only if the object is a directory                |
|s	          | Set the user or group ID when running                    |
|t	          | Restricted deletion flag or sticky mode                  |
|u	          | Specifies the permissions the user who owns the file has |
|g	          | Specifies the permissions of the group                   |
|o	          | Specifies the permissions of users not in the group      |
More than one permission can be also be used in the same command as follows:
```
chmod –v o+rw file.txt
```
Multiple files can also be specified:
```
chmod a-x,o+r file1.txt file2.txt
```
