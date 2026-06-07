#!/usr/bin/env python3
import json
import os


IMAGES_DIR = "images"


def main() -> None:
    owner = os.environ["OWNER"].lower()
    images = []

    for name in sorted(os.listdir(IMAGES_DIR)):
        directory = os.path.join(IMAGES_DIR, name)
        dockerfile = os.path.join(directory, "Dockerfile")

        if os.path.isdir(directory) and os.path.isfile(dockerfile):
            images.append(
                {
                    "directory": directory,
                    "tag": f"ghcr.io/{owner}/{name.lower()}:latest",
                }
            )

    if not images:
        raise SystemExit("No image directories with Dockerfile found")

    print(json.dumps(images))


if __name__ == "__main__":
    main()
