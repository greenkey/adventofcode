package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func findHexDistance(x, y int) (distance int) {
	x, y = abs(x), abs(y)
	if x != y {
		return y + (x-y)/2
	}
	return x
}

func findPathDistance(dirs []string) (dist, maxDistance int) {
	var x, y int
	for _, dir := range dirs {
		if dir == "n" {
			y += 2
		}
		if dir == "s" {
			y -= 2
		}
		if dir == "ne" {
			y++
			x++
		}
		if dir == "sw" {
			y--
			x--
		}
		if dir == "se" {
			x++
			y--
		}
		if dir == "nw" {
			y++
			x--
		}
		if findHexDistance(x, y) > maxDistance {
			maxDistance = findHexDistance(x, y)
		}
	}

	return findHexDistance(x, y), maxDistance
}

func main() {

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line := scanner.Text()
		directions := strings.Split(line, ",")

		fmt.Println(findPathDistance(directions))

	}

}
