package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

func readFile(filename string) (numbers [][]int) {
	dat, _ := ioutil.ReadFile("input")
	lines := strings.Split(string(dat), "\n")
	for _, line := range lines {
		numberStrings := strings.Split(line, "\t")
		numberInts := make([]int, len(numberStrings))
		for i, s := range numberStrings {
			numberInts[i], _ = strconv.Atoi(s)
		}
		numbers = append(numbers, numberInts)
	}
	return
}

// MinMax get both min and max of an int slice
func MinMax(ns []int) (min, max int) {
	min = math.MaxInt64
	for _, n := range ns {
		if n < min {
			min = n
		}
		if n > max {
			max = n
		}
	}
	return
}

func main() {
	numbers := readFile("input")

	var total, minN, maxN int
	for _, line := range numbers {
		minN, maxN = MinMax(line)
		total += maxN - minN
	}
	fmt.Println(total)

	total = 0
	for _, line := range numbers {
		for i := range line {
			for j := range line {
				if i != j && line[i]%line[j] == 0 {
					total += line[i] / line[j]
				}
			}
		}
	}
	fmt.Println(total)
}
