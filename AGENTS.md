# AGENTS.md

## Project shape
Order management service for a logistics platform. Handles order lookup,
status tracking, and batch processing. Written in Python.

## Build and test
pytest tests/ -x --tb=short

## Task protocol
Before starting any task, ask any questions needed to avoid wrong assumptions.
Do not guess. If anything about the task is ambiguous, ask first.

## Done definition
All tests pass. No new warnings. Diff touches the minimum number of files.
