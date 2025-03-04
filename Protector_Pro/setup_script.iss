[Setup]
AppName=Protector Pro
AppVersion=1.0
DefaultDirName={pf}\Protector Pro
DefaultGroupName=Protector Pro
OutputDir=.

[Files]
Source: "dist\main.exe"; DestDir: "{app}"

[Icons]
Name: "{group}\Protector Pro"; Filename: "{app}\main.exe"