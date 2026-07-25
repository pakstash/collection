# Container Images

This repository contains OCI image recipes for running desktop applications in containers with [pakstak](https://github.com/pakstak/pakstak).

The recipes are automatically built and published periodically to `ghcr.io/pakstash/<IMAGE_NAME>:latest`.

Example:

```sh
pakstak install mpv ghcr.io/pakstash/mpv:latest
```

The published images are standard OCI images and are not pakstak-specific, so they can be used with any container engine.

## Recommendations

You can find additional recommendations, examples, or other information in the image directories.
Command examples typically reside in `images/<IMAGE_NAME>/examples`, and general information resides in `images/<IMAGE_NAME>/README.md`.

## Using and contributing

The published images are currently simple (as in "low effort") images based on slim official Debian Docker images, usually built with APT. They are meant to become smaller and include only the necessary dependencies in the future.

You are encouraged to clone this repository as a template for building and publishing your own images. GitHub currently provides free Actions usage, and GHCR currently provides free storage for the resulting published images.
Contributions back to this repository are welcome as well.

## Building and publishing

The GitHub Actions workflow discovers runtimes from `runtimes/` and application images from `images/`. Runtime directories are ordered with an `NNNN_name` prefix; the prefix controls build order while the published runtime image name uses only `name`.

On the scheduled workflow, all runtimes are built and pushed first, sequentially, so application images can depend on them. Application images are then built and pushed with a matrix job, so they run in parallel. Manual workflow runs can optionally build only selected application images by passing comma-separated image names; runtime publishing is skipped in that case.

## License

Licensed under either of [Apache License, Version 2.0](LICENSE-APACHE) or
[MIT license](LICENSE-MIT) at your option.

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall
be dual licensed as above, without any additional terms or conditions.
