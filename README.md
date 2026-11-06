
Precompiled Qemu Kernel Images

## Kernels carrying fixes that are not upstream yet

The CI boots these with a kernel patch that has not been accepted yet.  The
patch lies next to the images; rebuild them with it applied, or the tests below
come back.

| Images | Patch | What it fixes |
|---|---|---|
| `kernel-sparc.img`, `kernel-sparc-smp.img` (6.5.10), `kernel-sparc-leon3.img` (6.18.37) | `kernel-sparc32-protnone.patch` | sparc32 took PROT_NONE ptes for swap entries; a fork after `mprotect(PROT_NONE)` copied a bogus swap entry and the guest hung (`tst-ipc-ctl-buffers`) |

## Changing an image means changing its qemu command line

A kernel without an MMU takes the size of its RAM from its config alone.  On
m68k, `head.S` sets `_ramend` to `CONFIG_RAMBASE + CONFIG_RAMSIZE`; the U-Boot
handover in `arch/m68k/kernel/uboot.c` reads only the initrd and the command
line and skips the `board_info` pointer, and there is no `mem=`.  Neither qemu
nor a real boot loader can tell the kernel how much RAM there is.

qemu puts the initrd at the end of *its* RAM, the kernel expects its own.  If
`-m` does not match the config, the kernel dies before the console is up and
the CI sees nothing but "Timeout: Keine Daten verfügbar".  This happened with
`kernel-m68k-68000.img`: 512 MiB since 07f40e1, while the workflow still ran
the m68328 machine with its default of 128 MiB.

So:

- When a change to an image needs a different qemu command line (RAM size,
  machine, `-cpu`, ...), change `qemu_cmd` in the uclibc-ng workflow in the
  same step.  The `.README` next to the image is not read by the CI.
- A green run after an upload does not prove the new image ran.  The runners
  were handed the old m68k-68000 image from raw.githubusercontent for a week;
  both builds have the same size, so the download log looked the same.  Check
  the `Linux version ... #N <date>` line in the next run's boot log against
  your build.
- To reproduce a CI run locally, use the qemu the CI uses: a binary in
  `qemu-bin/` replaces the one from `qemu-inst.tar.xz`.
