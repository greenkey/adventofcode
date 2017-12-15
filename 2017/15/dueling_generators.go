package main

import (
	"fmt"
	"os"
	"strconv"
)

const DIVISOR = 2147483647

type Generator struct {
	previous int
	factor   int
	criteria int
}

func (g *Generator) next() {
	g.previous = (g.previous * g.factor) % DIVISOR
}

func (g Generator) leftmost16() int {
	return g.previous & 65535
}

func (g *Generator) nextPicky() {
	for {
		g.previous = (g.previous * g.factor) % DIVISOR
		if g.previous%g.criteria == 0 {
			break
		}
	}
}

func main() {

	startA, _ := strconv.Atoi(os.Args[1])
	genA := Generator{
		factor:   16807,
		previous: startA,
	}

	startB, _ := strconv.Atoi(os.Args[2])
	genB := Generator{
		factor:   48271,
		previous: startB,
	}

	pairs := 0
	for i := 0; i < 40000000; i++ {
		if genA.leftmost16() == genB.leftmost16() {
			pairs++
		}
		genA.next()
		genB.next()
	}
	fmt.Println(pairs)

	genA.criteria = 4
	genA.previous = startA
	genB.criteria = 8
	genB.previous = startB

	pairs = 0
	for i := 0; i < 5000000; i++ {
		if genA.leftmost16() == genB.leftmost16() {
			pairs++
		}
		genA.nextPicky()
		genB.nextPicky()
	}
	fmt.Println(pairs)
}
