# Python Network 0

## Table of Content
- [What is `curl`?](What-is-`curl`?)
- [Common `curl` options to know](Common-`curl`-options-to-know)


### What is `curl`?
`curl` is a command-line tool and library for transferring data with URLs. It supports protocols like HTTP, HTTPS, FTP, FTPS, and more. `curl` allows users to send and receive data over these protocols, making it useful for testing APIs, downloading files, and performing other network-related tasks directly from the command line.

### Common `curl` options to know
Here are some common `curl` options that are useful to know:

1. **-X, --request**: Specify the HTTP method (GET, POST, PUT, DELETE, etc.).
   
2. **-H, --header**: Add HTTP headers to the request.

3. **-d, --data**: Send data in a POST request.

4. **-i, --include**: Include HTTP headers in the output.

5. **-o, --output**: Write output to a file or stdout.

6. **-s, --silent**: Silent mode (suppress progress meter and error messages).

7. **-L, --location**: Follow redirects.

8. **-b, --cookie**: Send cookies from a file or string.

9. **-c, --cookie-jar**: Save cookies to a file after receiving them.

10. **-u, --user**: HTTP authentication username and password.

11. **-I, --head**: Sends an HTTP HEAD request to a server, retrieving the headers for a URL without downloading the response's body.
