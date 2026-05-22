# glog-generators

Random content generators for the [Many Rats on
Sticks](https://drive.google.com/file/d/1wOAkBOCUSjnthMEnIsPVT1LSOCQzd88j/view)
game system, also known as GLOG v2. Should be useful for other systems too.

## chargen

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

## hexmap

### hexfiller

Generate a high-level content map for square or hexagonal grid.

The possibilities are `lair`, `portal`, and `ruin`.

An example, using the defaults:

```
+-------------+------------------+-----------+-----------+-----------+------+------------------+-----------+-----------+-----------+
|             |                  |           | lair      | lair ruin |      | lair portal      | lair ruin | lair      | lair      |
+-------------+------------------+-----------+-----------+-----------+------+------------------+-----------+-----------+-----------+
|             | lair portal ruin | lair      | ruin      |           |      |                  | ruin      |           |           |
+-------------+------------------+-----------+-----------+-----------+------+------------------+-----------+-----------+-----------+
| portal ruin | lair             |           | lair ruin | ruin      |      | lair portal      |           |           | lair ruin |
+-------------+------------------+-----------+-----------+-----------+------+------------------+-----------+-----------+-----------+
| lair ruin   | lair             | lair ruin |           | portal    |      |                  | ruin      | ruin      |           |
+-------------+------------------+-----------+-----------+-----------+------+------------------+-----------+-----------+-----------+
|             |                  | ruin      |           |           | ruin |                  | portal    | lair ruin | lair      |
+-------------+------------------+-----------+-----------+-----------+------+------------------+-----------+-----------+-----------+
| ruin        |                  | lair      |           |           |      | lair portal ruin |           |           | lair      |
+-------------+------------------+-----------+-----------+-----------+------+------------------+-----------+-----------+-----------+
|             |                  |           | ruin      |           |      | ruin             | lair      |           |           |
+-------------+------------------+-----------+-----------+-----------+------+------------------+-----------+-----------+-----------+
| lair        | lair             | lair      |           | ruin      | ruin |                  |           |           | ruin      |
+-------------+------------------+-----------+-----------+-----------+------+------------------+-----------+-----------+-----------+
| ruin        | ruin             | ruin      | lair ruin | lair      | lair | ruin             | lair ruin |           | lair      |
+-------------+------------------+-----------+-----------+-----------+------+------------------+-----------+-----------+-----------+
|             |                  | lair      | ruin      | ruin      | lair | ruin             |           | ruin      |           |
+-------------+------------------+-----------+-----------+-----------+------+------------------+-----------+-----------+-----------+
```

And using `hexfiller --rows 5 --cols 5 --lair-rate 0.25 --portal-rate 0.1 --ruin-rate 0.6`:

```
+-----------+------+-----------+------------------+-----------+
|           | lair | lair ruin | ruin             | lair      |
+-----------+------+-----------+------------------+-----------+
| lair      | lair |           |                  | lair ruin |
+-----------+------+-----------+------------------+-----------+
|           | ruin | lair ruin | lair portal ruin | lair ruin |
+-----------+------+-----------+------------------+-----------+
|           |      |           | ruin             | ruin      |
+-----------+------+-----------+------------------+-----------+
| lair ruin | ruin | ruin      | lair ruin        |           |
+-----------+------+-----------+------------------+-----------+
```
