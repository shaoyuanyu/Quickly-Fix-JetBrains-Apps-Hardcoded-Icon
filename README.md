# Quickly Fix JetBrains Apps Hardcoded Icon

## The problem

`Icon` for the toolbox & applications installed through it are hardcoded on Linux.

This means the icons of JetBrains apps wouldn't change when you (using GNOME tweaks or whatever tools to) change your [freedesktop icon theme](https://freedesktop.org/wiki/Specifications/icon-theme-spec/).

That makes the apps standout a lot in a themed environment. (Honestly, they are even ugly.)

After 7 years they still haven't handled with this issue, which could have been fixed easily. :(

See more about this issue:
https://youtrack.jetbrains.com/issue/TBX-1470/Icon-for-the-toolbox-applications-installed-through-it-are-hardcoded-on-Linux

## The tool

This tool is for fixing the hardcoding-icon problem **temporarily**.

Unfortunately you have to run this script **every** time you start your `JetBrains-Toolbox` app or update any of your JetBrains apps
because the `.desktop` files will be covered with hardcoded `Icon` paths. :(