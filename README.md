# modern

A minimalist tiling desktop environment using i3 and some XFCE components.

## Why?

i3 is great, but manually setting up all the dependencies isn't. Modern provides opinionated defaults for i3 and related core desktop components.

## Goals

Configuration not required.

Avoid gnome-keyring-daemon and gnome-settings-daemon and gnome-session.

Not stomp on any other packages or modify any system settings on behalf of the user.

## Caveats

At the moment the touchpad detection / setup code isn't very good.

The code could be more modular, modern-session does most of the work in a large bash script.

# Building

`debuild -us -uc` in the `modern-metapackages` directory.
