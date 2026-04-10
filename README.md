# server-jars 📦

This is a git repository that contains the server jars for multiple Minecraft versions. It is used and maintained by the [ThreadMC](https://github.com/threadmc) project. The repository is structured to allow easy access to the server jars for different Minecraft versions, including **only** official server jars at the moment. Unofficial server jars are not yet included in this repository.

## Usage 🚀

To use the server jars in this repository, you can clone the repository and navigate to the `versions` directory. Each version has its own directory containing the `server.jar` file and a JSON file with metadata about the version.

## Structure 🗂️
The repository is structured as follows:

```
versions
├── 26.1.2
│   ├── server.jar
│   └── 26.1.2.json
├── 26.1.1
│   ├── server.jar
│   └── 26.1.1.json
├── 26.1
│   ├── server.jar
│   └── 26.1.json
├── 1.21.11
│   ├── server.jar
│   ├── mojang-mappings.txt
│   └── 1.21.11.json
├── 1.21.10
│   ├── server.jar
│   ├── mojang-mappings.txt
│   └── 1.21.10.json
├── 1.21.9
│   ├── server.jar
│   ├── mojang-mappings.txt
│   └── 1.21.9.json
├── 1.21.8
│   ├── server.jar
│   ├── mojang-mappings.txt
│   └── 1.21.8.json
├── 1.21.7
│   ├── server.jar
│   ├── mojang-mappings.txt
│   └── 1.21.7.json
├── 1.21.6
│   ├── server.jar
│   ├── mojang-mappings.txt
│   └── 1.21.6.json
├── 1.21.5
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.21.5.json
├── 1.21.4
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.21.4.json
├── 1.21.3
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.21.3.json
├── 1.21.2
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.21.2.json
├── 1.21.1
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.21.1.json
├── 1.21
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.21.json
├── 1.20.6
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.20.6.json
├── 1.20.5
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.20.5.json
├── 1.20.4
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.20.4.json
├── 1.20.3
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.20.3.json
├── 1.20.2
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.20.2.json
├── 1.20.1
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.20.1.json
├── 1.20
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.20.json
├── 1.19.4
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.19.4.json
├── 1.19.3
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.19.3.json
├── 1.19.2
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.19.2.json
├── 1.19.1
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.19.1.json
├── 1.19
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.19.json
├── 1.18.2
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.18.2.json
├── 1.18.1
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.18.1.json
├── 1.18
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.18.json
├── 1.17.1
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.17.1.json
├── 1.17
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.17.json
├── 1.16.5
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.16.5.json
├── 1.16.4
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.16.4.json
├── 1.16.3
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.16.3.json
├── 1.16.2
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.16.2.json
├── 1.16.1
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.16.1.json
├── 1.16
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.16.json
├── 1.15.2
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.15.2.json
├── 1.15.1
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.15.1.json
├── 1.15
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.15.json
├── 1.14.4
│   ├── server.jar
│   ├── mojang-mappings.txt
│   ├── mojang-mappings.tiny
│   └── 1.14.4.json
├── 1.14.3
│   ├── server.jar
│   └── 1.14.3.json
├── 1.14.2
│   ├── server.jar
│   └── 1.14.2.json
├── 1.14.1
│   ├── server.jar
│   └── 1.14.1.json
├── 1.14
│   ├── server.jar
│   └── 1.14.json
├── 1.13.2
│   ├── server.jar
│   └── 1.13.2.json
├── 1.13.1
│   ├── server.jar
│   └── 1.13.1.json
├── 1.13
│   ├── server.jar
│   └── 1.13.json
├── 1.12.2
│   ├── server.jar
│   └── 1.12.2.json
├── 1.12.1
│   ├── server.jar
│   └── 1.12.1.json
├── 1.12
│   ├── server.jar
│   └── 1.12.json
├── 1.11.2
│   ├── server.jar
│   └── 1.11.2.json
├── 1.11.1
│   ├── server.jar
│   └── 1.11.1.json
├── 1.11
│   ├── server.jar
│   └── 1.11.json
├── 1.10.2
│   ├── server.jar
│   └── 1.10.2.json
├── 1.10.1
│   ├── server.jar
│   └── 1.10.1.json
├── 1.10
│   ├── server.jar
│   └── 1.10.json
├── 1.9.4
│   ├── server.jar
│   └── 1.9.4.json
├── 1.9.3
│   ├── server.jar
│   └── 1.9.3.json
├── 1.9.2
│   ├── server.jar
│   └── 1.9.2.json
├── 1.9.1
│   ├── server.jar
│   └── 1.9.1.json
├── 1.9
│   ├── server.jar
│   └── 1.9.json
├── 1.8.9
│   ├── server.jar
│   └── 1.8.9.json
├── 1.8.8
│   ├── server.jar
│   └── 1.8.8.json
├── 1.8.7
│   ├── server.jar
│   └── 1.8.7.json
├── 1.8.6
│   ├── server.jar
│   └── 1.8.6.json
├── 1.8.5
│   ├── server.jar
│   └── 1.8.5.json
├── 1.8.4
│   ├── server.jar
│   └── 1.8.4.json
├── 1.8.3
│   ├── server.jar
│   └── 1.8.3.json
├── 1.8.2
│   ├── server.jar
│   └── 1.8.2.json
├── 1.8.1
│   ├── server.jar
│   └── 1.8.1.json
├── 1.8
│   ├── server.jar
│   └── 1.8.json
├── 1.7.10
│   ├── server.jar
│   └── 1.7.10.json
├── 1.7.9
│   ├── server.jar
│   └── 1.7.9.json
├── 1.7.8
│   ├── server.jar
│   └── 1.7.8.json
├── 1.7.7
│   ├── server.jar
│   └── 1.7.7.json
├── 1.7.6
│   ├── server.jar
│   └── 1.7.6.json
├── 1.7.5
│   ├── server.jar
│   └── 1.7.5.json
├── 1.7.4
│   ├── server.jar
│   └── 1.7.4.json
├── 1.7.3
│   ├── server.jar
│   └── 1.7.3.json
├── 1.7.2
│   ├── server.jar
│   └── 1.7.2.json
├── 1.6.4
│   ├── server.jar
│   └── 1.6.4.json
├── 1.6.2
│   ├── server.jar
│   └── 1.6.2.json
├── 1.6.1
│   ├── server.jar
│   └── 1.6.1.json
├── 1.5.2
│   ├── server.jar
│   └── 1.5.2.json
├── 1.5.1
│   ├── server.jar
│   └── 1.5.1.json
├── 1.4.7
│   ├── server.jar
│   └── 1.4.7.json
├── 1.4.6
│   ├── server.jar
│   └── 1.4.6.json
├── 1.4.5
│   ├── server.jar
│   └── 1.4.5.json
├── 1.4.4
│   ├── server.jar
│   └── 1.4.4.json
├── 1.4.2
│   ├── server.jar
│   └── 1.4.2.json
├── 1.3.2
│   ├── server.jar
│   └── 1.3.2.json
├── 1.3.1
│   ├── server.jar
│   └── 1.3.1.json
├── 1.2.5
│   ├── server.jar
│   └── 1.2.5.json
├── 1.2.4
│   └── 1.2.4.json
├── 1.2.3
│   └── 1.2.3.json
├── 1.2.2
│   └── 1.2.2.json
├── 1.2.1
│   └── 1.2.1.json
├── 1.1
│   └── 1.1.json
└── 1.0
    └── 1.0.json
```
