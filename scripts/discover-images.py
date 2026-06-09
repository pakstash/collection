#!/usr/bin/env python3
import argparse
import json
import os
import re
import subprocess


IMAGES_DIR = "images"
RUNTIMES_DIR = "runtimes"
RUNTIME_NAME_RE = re.compile(r"^\d{4}_(.+)$")


def image_entry(owner: str, directory: str, name: str) -> dict[str, str]:
    return {
        "directory": directory,
        "name": name,
        "tag": f"ghcr.io/{owner}/{name.lower()}:latest",
    }


def discover_images(owner: str) -> list[dict[str, str]]:
    images = []

    for name in sorted(os.listdir(IMAGES_DIR)):
        directory = os.path.join(IMAGES_DIR, name)
        dockerfile = os.path.join(directory, "Dockerfile")

        if os.path.isdir(directory) and os.path.isfile(dockerfile):
            images.append(image_entry(owner, directory, name))

    if not images:
        raise SystemExit("No image directories with Dockerfile found")

    return images


def discover_runtimes(owner: str) -> list[dict[str, str]]:
    runtimes = []

    if not os.path.isdir(RUNTIMES_DIR):
        return runtimes

    for directory_name in sorted(os.listdir(RUNTIMES_DIR)):
        directory = os.path.join(RUNTIMES_DIR, directory_name)
        dockerfile = os.path.join(directory, "Dockerfile")

        if not os.path.isdir(directory) or not os.path.isfile(dockerfile):
            continue

        match = RUNTIME_NAME_RE.fullmatch(directory_name)
        if not match:
            raise SystemExit(
                f"Runtime directory {directory!r} must use NNNN_name format"
            )

        runtimes.append(image_entry(owner, directory, match.group(1)))

    return runtimes


def discover(owner: str) -> dict[str, object]:
    return {
        "owner": owner,
        "runtimes": discover_runtimes(owner),
        "images": discover_images(owner),
    }


def get_owner() -> str:
    return os.environ["OWNER"].lower()


def print_manifest() -> None:
    print(json.dumps(discover(get_owner())))


def print_github_outputs() -> None:
    manifest = discover(get_owner())
    print(f"owner={manifest['owner']}")
    print(f"runtimes={json.dumps(manifest['runtimes'])}")
    print(f"images={json.dumps(manifest['images'])}")


def build_runtimes() -> None:
    manifest = discover(get_owner())
    owner = manifest["owner"]

    for runtime in manifest["runtimes"]:
        directory = runtime["directory"]
        tag = runtime["tag"]

        subprocess.run(
            [
                "docker",
                "build",
                "--file",
                f"{directory}/Dockerfile",
                "--tag",
                tag,
                "--build-arg",
                f"OWNER={owner}",
                ".",
            ],
            check=True,
        )
        subprocess.run(["docker", "push", tag], check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        choices=("manifest", "github-outputs", "build-runtimes"),
        nargs="?",
        default="manifest",
    )
    args = parser.parse_args()

    if args.command == "manifest":
        print_manifest()
    elif args.command == "github-outputs":
        print_github_outputs()
    elif args.command == "build-runtimes":
        build_runtimes()


if __name__ == "__main__":
    main()
