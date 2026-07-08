# Steam

This image provides minimal dependencies for [Steam](https://store.steampowered.com/about/).

## Installation

The installer is not included in this image.

You can download the installer as a compressed tarball from [here](https://repo.steampowered.com/steam/archive/stable/steam_latest.tar.gz).

Extract it into `$HOME/.var/container/steam/`. This should create `$HOME/.var/container/steam/steam-launcher`.

You can now install it with the [example installation command](examples/install).

After the installation process is complete, you can remove `$HOME/.var/container/steam/steam-launcher` directory.

## Running

[Example command](examples/run).

Feel free to modify and/or contribute back another example.
