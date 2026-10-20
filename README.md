
Precompiled Qemu Kernel Images

## Kernels carrying fixes that are not upstream yet

The CI boots these with a kernel patch that has not been accepted yet.  The
patch lies next to the images; rebuild them with it applied, or the tests below
come back.

| Images | Patch | What it fixes |
|---|---|---|
| `kernel-sparc.img`, `kernel-sparc-smp.img` (6.5.10), `kernel-sparc-leon3.img` (6.18.37) | `kernel-sparc32-protnone.patch` | sparc32 took PROT_NONE ptes for swap entries; a fork after `mprotect(PROT_NONE)` copied a bogus swap entry and the guest hung (`tst-ipc-ctl-buffers`) |
