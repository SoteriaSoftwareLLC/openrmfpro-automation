# Python3 example application using simple cgi-bin

To launch the application, from the ./applications/python/ folder run the below command. And access with a browser to `http://localhost:8000/cgi-bin/listTemplates.py` for example. 

```
python3 -m http.server --cgi
```

This includes a `myVariables.py` file that has the 3 below variables in it for the root URL, application key, and bearer token generated. This is in place of ENVIRONMENT variables in a framework or however you wish to pass and use the information securely.

```
rootURL = "http://openrmfpro.mycompany.com:8080"
applicationKey = "myApplicationKey"
bearerToken = "hvs.CAESIBP1QjNLqckAk1PlNyMqqJTlxxxxxxxxxxqTDV6Y05uOVhkTXREdlZlSHpjOUt0Q0U"
```