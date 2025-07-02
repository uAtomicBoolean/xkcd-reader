# xkcd-reader
A very basic [xkcd](https://xkcd.com/) reader made with Python and [Slint](https://slint.dev/) made when I was bored.  
It downloads each xkcd comics once as a temporary file and then use the caching from `functools.cache` to get them.  
I did not test it on Windows and MacOS so it might not work on these platforms.

## How to use
You can use the `Previous`, `Random` and `Next` buttons to navigate in the comics.  
You can also open the web page of the current comic by clicking on its title or image.  