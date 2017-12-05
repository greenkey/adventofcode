package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func readFile(filename string) (numbers []int) {
	dat, _ := ioutil.ReadFile("input")
	lines := strings.Split(string(dat), "\n")
	for _, line := range lines {
		n, _ := strconv.Atoi(line)
		numbers = append(numbers, n)
	}
	return
}

func cpu1(instructions []int) (jumps int) {
	var next int
	for i := 0; i < len(instructions) && i >= 0; {
		next += instructions[i]
		instructions[i]++
		jumps++
		i = next
	}
	return
}

func cpu2(instructions []int) (jumps int) {
	var next int
	for i := 0; i < len(instructions) && i >= 0; {
		next += instructions[i]
		if instructions[i] >= 3 {
			instructions[i]--
		} else {
			instructions[i]++
		}
		jumps++
		i = next
	}
	return
}

func main() {

	fmt.Println(cpu1(readFile("input")))
	fmt.Println(cpu2(readFile("input")))

}
