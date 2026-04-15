# zmk-crescent

Reusable Crescent chord layout module for ZMK.

## Dependencies

- [`zmk-helpers`](https://github.com/urob/zmk-helpers) for `ZMK_COMBO` and key-label conventions

## Prerequisites

This module assumes your keyboard uses the zmk-helpers key labeling conventions
(e.g., `LT4` for left top pinky, `RT1` for right top index, etc.).

Default finger-to-position mapping:

| Finger | Key | Default Position |
|--------|-----|-----------------|
| Left pinky | C | LT4 |
| Left ring | R | LT3 |
| Left middle | S | LT2 |
| Left index | T | LT1 |
| Left thumb | Space | LT0 |
| Right thumb | N | RH0 |
| Right index | A | RT1 |
| Right middle | E | RT2 |
| Right ring | U | RT3 |
| Right pinky | I | RT4 |

## Usage

1. Add this repository as a west project (commonly at `modules/zmk/crescent`)
2. In your keymap, include key-labels for your keyboard
3. Define a layer called `CRESCENT` and assign it a layer number
4. Include the Crescent combos DTSI file

Example:

```c
#include <zmk-helpers/helper.h>
#include <zmk-helpers/key-labels/34.h>

#define CRESCENT 0

#include <zmk-crescent/crescent.dtsi>

ZMK_LAYER(crescent,
  &none &none &none &none &none &none &none &none &none &none
  &none &none &none &none &none &none &none &none &none &none
  &none &none &none &none &none &none &none &none &none &none
                    &none &none &none &none
)
```

## West Configuration

Add to your `west.yml`:

```yaml
- name: zmk-crescent
  remote: hunner
  revision: main
  path: modules/zmk/crescent
```

Or for local development:

```yaml
- name: crescent
  remote: local  # file:///home/user/Documents/git
  revision: main
  path: modules/zmk/crescent
  submodules: false
```

Note: when using a local path, west resolves the module root from the `zmk/`
subdirectory, so the `url-base` should point to the parent of the `crescent`
repo (e.g., `file:///home/user/Documents/git`).

## Overriding Positions

Define `CRESCENT_POS_*` macros before including `crescent.dtsi` to map
to different key positions:

```c
#define CRESCENT_POS_C 0
#define CRESCENT_POS_R 1
#define CRESCENT_POS_S 2
#define CRESCENT_POS_T 3
#define CRESCENT_POS_SPACE 4
#define CRESCENT_POS_N 10
#define CRESCENT_POS_A 5
#define CRESCENT_POS_E 6
#define CRESCENT_POS_U 7
#define CRESCENT_POS_I 8

#include <zmk-crescent/crescent.dtsi>
```

## Combo Timing

Adjust `CRESCENT_COMBO_TERM` (default: 50ms) before including the DTSI:

```c
#define CRESCENT_COMBO_TERM 40
#include <zmk-crescent/crescent.dtsi>
```
