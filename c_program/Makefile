HOST_DIR := host
BUILDDIR ?= build

HOST_TARGET := ${BUILDDIR}/checksum_host

HOST_SOURCES := $(wildcard ${HOST_DIR}/*.c)

.PHONY: all clean test

__dirs := $(shell mkdir -p ${BUILDDIR})

COMMON_FLAGS := -Wall -Wextra -Werror -g -Wno-unused-parameter -Wno-sign-compare -Wno-unused-function
HOST_FLAGS := ${COMMON_FLAGS} -std=c11 -O3 `dpu-pkg-config --cflags --libs dpu` -DNR_TASKLETS=${NR_TASKLETS} -DNR_DPUS=${NR_DPUS}

all: ${HOST_TARGET}

${HOST_TARGET}: ${HOST_SOURCES}
	$(CC) -o $@ ${HOST_SOURCES} ${HOST_FLAGS}

clean:
	$(RM) -r $(BUILDDIR)

test_c: ${HOST_TARGET}
	./${HOST_TARGET}

