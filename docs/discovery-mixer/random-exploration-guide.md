# Random Exploration Guide

## Purpose

Random exploration is a constrained discovery mode.
It is used to search inside supported structural classes, not to generate arbitrary equations.

## What It Can Be Used For

- finding failures with clean repair paths
- finding stronger-versus-weaker target splits
- discovering threshold crossings
- generating benchmark scenarios worth saving
- stress testing augmentation logic

## Reproducibility Rule

Every random run uses a user-visible seed.
If a discovered case is interesting, it can be replayed exactly and exported.

## Current Search Families

- restricted-linear search
- periodic modal search
- diagonal/history search

## Search Objectives

- `find a failing case with a repair`
- `accept the first supported case`

## Reading Random Results

A random result is only worth keeping if:

- the generated case is well-typed
- the regime verdict is consistent across recomputation
- the recommended repair is testable or at least structurally interpretable
- the exported case reproduces the same outcome with the same seed

## What This Mode Does Not Claim

- exhaustive search
- theorem discovery by itself
- arbitrary counterexample generation outside supported families
