# Example Code for dotnet core to push and pull data from OpenRMF<sup>&reg;</sup> Professional
The examples here assume you have OpenRMF® Professional v2.7 or higher installed, the external API setup and turned on, and you have at least one Application Integration record setup on the Administration --> External API Integration page. Your user account in Keycloak also must be setup to match the API integration with proper roles and permissions, including the ExternalAPI role to allow interaction from outside the OpenRMF<sup>&reg;</sup> Professional UI. 

Some of the APIs for patch vulnerabilities and the other technology vulnerabilities are version 2.8 or higher. If you have questions please see your customer representative or email Soteria Software Support. You can also contact us on our https://www.soteriasoft.com/ company website as well.

## Building the Examples
Each of the examples is in its own directory structure so you can keep the files and executables separate.  Perform a go build like below to build these simplified examples

```
dotnet build
```

## Running the Examples
Once built you can run the examples on your OS by calling the executable and passing in the required parameters. Most of the time you have to at least pass in the root URL, the application Key and the token for the open API setup for OpenRMF<sup>&reg;</sup> Professional at a minimum. Others you pass in the systemKey from your system package as well. And a few you pass in unique Ids of checklists or history items you are requesting.

```
bin/Debug/net6.0/authentication http://192.168.13.25:8080 soteriaapi hvs.xxxxxxxxxxxxxxxxxxxxxxxx
```

You should get a result written to the console. 

## Passing Command Line Arguments in Debug Mode
In the "args" area of your launch.json in VS Code you can set the passed in argument parameters to test interactively as shown below. 

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": ".NET Core Launch (console)",
            "type": "coreclr",
            "request": "launch",
            "preLaunchTask": "build",
            // If you have changed target frameworks, make sure to update the program path.
            "program": "${workspaceFolder}/bin/Debug/net6.0/authentication.dll",
            "args": ["http://192.168.13.25:8080", "APPLICATIONKEY", "hvs.TOKENINFORMATION"],
            "cwd": "${workspaceFolder}",
            // For more information about the 'console' field, see https://aka.ms/VSCode-CS-LaunchJson-Console
            "console": "internalConsole",
            "stopAtEntry": false
        },
        {
            "name": ".NET Core Attach",
            "type": "coreclr",
            "request": "attach"
        }
    ]
}
```