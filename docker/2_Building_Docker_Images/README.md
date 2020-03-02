# Building Docker Images

## Basics: How is an image created?

To build your own Docker images, you need to create a [Dockerfile](https://docs.docker.com/engine/reference/builder/).

In this folder, we have already included a `Dockerfile`. Take a look.

And when you are ready to build, run the following command.

```
docker build -t custom-dsr .
```

```
docker run --rm custom-dsr
```

## Exercise: Creating your own Docker image

- Use this Dockerfile as reference
- Use `ubuntu:16.04` as base image
- Install python 3.7
- Create a python file `hello.py` that outputs "Hello World"
- Make sure that this python file is executed on running the image
