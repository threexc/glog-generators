# glog-generators

Random content generators for the [Many Rats on
Sticks](https://drive.google.com/file/d/1wOAkBOCUSjnthMEnIsPVT1LSOCQzd88j/view)
game system, also known as GLOG v2.

## Rust

### GLOG v2 Character Generator

Run the `stats` binary with e.g.:

3d6: `cargo run --bin stats -- --dice 3 --faces 6`

4d6 drop lowest: `cargo run --bin stats -- --dice 4 --faces 6 --lowest 1`

Defaults to 3d6.

Run the CLI with:

```
cargo run --bin cli
```

or run the web version:

```
cargo run --bin web --features web
```

## Python

### hexfiller

Generate a high-level content map for square or hexagonal grid, 
