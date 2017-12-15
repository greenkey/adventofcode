package main

import (
	"fmt"
	"os"
	"strconv"
)

const DIVISOR = 2147483647

type Generator struct {
	previous int64
	factor   int64
}

func (g *Generator) next() {
	g.previous = (g.previous * g.factor) % DIVISOR
}

func (g Generator) leftmost16() string {
	s := fmt.Sprintf("%016b", g.previous)
	return s[len(s)-16:]
}

func main() {

	startA, _ := strconv.Atoi(os.Args[1])
	genA := Generator{factor: 16807, previous: int64(startA)}

	startB, _ := strconv.Atoi(os.Args[2])
	genB := Generator{factor: 48271, previous: int64(startB)}

	pairs := 0
	for i := 0; i < 40000000; i++ {
		if genA.leftmost16() == genB.leftmost16() {
			pairs++
		}
		genA.next()
		genB.next()
	}
	fmt.Println(pairs)
}
