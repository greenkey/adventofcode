package main

import (
	"fmt"
	"io/ioutil"
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

func biggest(bank []int) (index, big int) {
	for i, n := range bank {
		if n > big {
			index = i
			big = n
		}
	}
	return
}

func bankSignature(bank []int) (s string) {
	bite := make([]byte, len(bank))
	for i := range bank {
		bite[i] = byte(bank[i])
	}
	return string(bite)
}

func main() {

	banks := readFile("input")
	for _, b := range banks {
		combinations := make(map[string]int)
		cicleCombination := 0
		for {
			if combinations[bankSignature(b)] == 1 {
				fmt.Println(len(combinations))
				cicleCombination++
				if cicleCombination == 2 {
					break
				}
				combinations = make(map[string]int)
			}
			combinations[bankSignature(b)] = 1
			i, n := biggest(b)
			b[i] = 0
			for n > 0 {
				i = (i + 1) % len(b)
				b[i]++
				n--
			}
		}

	}

}
