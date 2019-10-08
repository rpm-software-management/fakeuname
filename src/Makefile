CFLAGS = -fPIC -Wall -Wextra -O2 -g # C flags
LDFLAGS = -shared  # linking flags
TARGET_LIB = fakeuname.so # target lib

SRCS = fakeuname.c # source files
OBJS = $(SRCS:.c=.o)

.PHONY: all clean

all: ${TARGET_LIB}

$(TARGET_LIB): $(OBJS)
	gcc ${LDFLAGS} -o $@ $^

$(SRCS:.c=.d):%.d:%.c
	gcc $(CFLAGS) -MM $< >$@

include $(SRCS:.c=.d)

clean:
	-rm -f ${TARGET_LIB} ${OBJS} $(SRCS:.c=.d)
