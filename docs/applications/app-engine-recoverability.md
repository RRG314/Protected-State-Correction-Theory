# App / Engine Recoverability Integration

## Purpose

This note records the app-facing uses that are strong enough to keep.

It does not claim that the repository already solves world-state sync or reconstruction in full generality.

## Strongest Kept App-Facing Idea

The strongest justified application concept is a **recoverability engine** for state design.

Given:
- a chosen protected world variable or subsystem state
- a compressed or partial record
- an update cadence or observation horizon
- a candidate recovery architecture

ask:
- is exact reconstruction possible?
- if not, is a weaker protected variable still enough for the product task?
- if not, what additional retained state or measurement is minimally needed?
- if exact static recovery fails, should the design switch to observer-style or asymptotic recovery?

## Legitimate App / Engine Questions

### 1. State-sync sufficiency
- what minimum retained state is required to rebuild the protected gameplay or simulation variable?
- what information can be dropped without losing the protected target?

### 2. Compression safety
- can a coarse representation preserve the protected task variable exactly?
- if not, what weaker protected variable remains safe to expose or cache?

### 3. Observer routing
- if one-shot reconstruction is impossible, is online estimation or incremental correction still viable?

### 4. Ambiguity witness generation
- can two materially different hidden states yield the same transmitted or stored record while changing the protected output?
- if yes, the current compression or sync surface is structurally insufficient

## Good First App Uses

- deciding which world-state features must be included in a coarse sync packet
- deciding whether terrain / road / structure summaries preserve the protected game logic variable
- deciding whether a weaker target, such as navigability or occupancy, can be preserved when exact geometry cannot
- deciding whether exact replay is impossible from the stored record and whether observer-style resimulation is the right fallback

## Boundaries

Do not promote these connections unless an actual state family, record map, and protected variable are written down.

The repo helps once the app problem is formalized.
It does not replace the formalization step.
