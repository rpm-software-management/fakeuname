/*
 * Copyright (C) 2019 Red Hat, Inc.
 *
 * Licensed under the GNU Lesser General Public License Version 2.1
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

#define _GNU_SOURCE
#include <unistd.h>
#include <sys/syscall.h>
#include <sys/utsname.h>

#include <string.h>
#include <stdlib.h>

/**
 * Override uname syscall to return fake kernel release stored in
 * FAKE_KERNEL_RELEASE environment variable
 * Usage: FAKE_KERNEL_RELEASE=1.2.34 LD_PRELOAD=./fakeuname.so uname -a
 */
extern int uname(struct utsname *un)
{
    int ret;
    const char* s = getenv("FAKE_KERNEL_RELEASE");

    ret = syscall(SYS_uname, un);
    if (ret == 0 && s) {
        strncpy(un->release, s, _UTSNAME_RELEASE_LENGTH - 1);
    }

    return ret;
}
